# © 2022-2024 Copyright SES AI
# Author: Daniel Cogswell
# Email: danielcogswell@ses.ai

import sys
import mmap
import struct
import logging
import tempfile
import zipfile
import re
from datetime import datetime, timezone
import xml.etree.ElementTree as ET
import pandas as pd

from .utils import _generate_cycle_number, _count_changes
from .dicts import rec_columns, dtype_dict, aux_dtype_dict, state_dict, \
    multiplier_dict, aux_chl_type_columns

logger = logging.getLogger('newarenda')


def read_ndax(file, software_cycle_number=False, cycle_mode='chg'):
    """
    Function to read electrochemical data from a Neware ndax binary file.

    Args:
        file (str): Name of an .ndax file to read
        software_cycle_number (bool): Regenerate the cycle number field
        cycle_mode (str): Selects how the cycle is incremented.
            'chg': (Default) Sets new cycles with a Charge step following a Discharge.
            'dchg': Sets new cycles with a Discharge step following a Charge.
            'auto': Identifies the first non-rest state as the incremental state.
    Returns:
        df (pd.DataFrame): DataFrame containing all records in the file
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        zf = zipfile.PyZipFile(file)

        # Read version information
        try:
            version_info = zf.extract('VersionInfo.xml', path=tmpdir)
            with open(version_info, 'r', encoding='gb2312') as f:
                config = ET.fromstring(f.read()).find('config/ZwjVersion')
            logger.info(f"Server version: {config.attrib['SvrVer']}")
            logger.info(f"Client version: {config.attrib['CurrClientVer']}")
            logger.info(f"Control unit version: {config.attrib['ZwjVersion']}")
            logger.info(f"Tester version: {config.attrib['MainXwjVer']}")
        except Exception:
            pass

        # Read active mass
        try:
            step = zf.extract('Step.xml', path=tmpdir)
            with open(step, 'r', encoding='gb2312') as f:
                config = ET.fromstring(f.read()).find('config')
            active_mass = float(config.find('Head_Info/SCQ').attrib['Value'])
            logger.info(f"Active mass: {active_mass/1000} mg")
        except Exception:
            pass

        # Find all auxiliary channel files
        # Auxiliary files files need to be matched to entries in TestInfo.xml
        # Sort by the numbers in the filename, assume same order in TestInfo.xml
        aux_data = []
        for f in zf.namelist():
            m = re.search(r"data_AUX_(\d+)_(\d+)_(\d+)\.ndc", f)
            if m:
                aux_data.append((f, list(map(int, m.groups()))))
            else:
                m = re.search(r".*_(\d+)\.ndc", f)
                if m:
                    aux_data.append((f, [int(m.group(1)), 0, 0]))

        # Sort by the three integers
        aux_data.sort(key=lambda x: x[1])
        aux_filenames = [f for f, _ in aux_data]

        # Find all auxiliary channel dicts in TestInfo.xml
        aux_ch_dict = {f: {} for f in aux_filenames}
        if aux_filenames:
            try:
                step = zf.extract('TestInfo.xml', path=tmpdir)
                with open(step, 'r', encoding='gb2312') as f:
                    testinfo = ET.fromstring(f.read()).find('config/TestInfo')

                aux_dicts = [k.attrib for k in testinfo if "Aux" in k.tag] if testinfo is not None else []

                # Map filenames to dicts, assume files are in same order as TestInfo.xml
                if len(aux_dicts) == len(aux_filenames):
                    aux_ch_dict = dict(zip(aux_filenames, aux_dicts))
                else:
                    logger.warning("Different number of aux channels in files and TestInfo.xml")
            except Exception:
                logger.exception("Found aux files, but could not read TestInfo.xml")

        # Try to read data.ndc
        if 'data.ndc' in zf.namelist():
            data_file = zf.extract('data.ndc', path=tmpdir)
            data_df = read_ndc(data_file)
        else:
            raise NotImplementedError("File type not yet supported!")

        # Some ndax have data spread across 3 different ndc files. Others have
        # all data in data.ndc.
        # Check if data_runInfo.ndc and data_step.ndc exist
        if all(i in zf.namelist() for i in ['data_runInfo.ndc', 'data_step.ndc']):

            # Read data from separate files
            runInfo_file = zf.extract('data_runInfo.ndc', path=tmpdir)
            step_file = zf.extract('data_step.ndc', path=tmpdir)
            runInfo_df = read_ndc(runInfo_file)
            step_df = read_ndc(step_file)

            # Merge dataframes
            data_df = data_df.merge(runInfo_df, how='left', on='Index')
            data_df['Step'] = data_df['Step'].ffill()
            data_df = data_df.merge(step_df, how='left', on='Step')

            # Fill in missing data for ndc 11, 14, 17
            if data_df["Time"].isna().any():
                _data_interpolation(data_df)

        # Select fields to return
        data_df = data_df.reindex(columns=rec_columns)

        # Read and merge Aux data from ndc files
        for i, (f, aux_dict) in enumerate(aux_ch_dict.items()):
            aux_file = zf.extract(f, path=tmpdir)
            aux_df = read_ndc(aux_file)

            # Get aux ID from runInfo, if not Aux column, if not -1, -2 etc.
            aux_id = aux_dict.get("AuxID", None)
            if aux_id is None:
                aux_id = (
                    aux_df["Aux"].iloc[0]
                    if "Aux" in aux_df.columns and len(aux_df["Aux"]) > 0
                    else -i-1
                )

            # If ? column exists, first rename name by ChlType (T, t, H)
            if "?" in aux_df.columns and aux_dict.get("ChlType") in aux_chl_type_columns:
                aux_df = aux_df.rename(
                    columns = {"?": aux_chl_type_columns[aux_dict["ChlType"]]},
                )

            # Cast columns to types defined in aux_dtype_dict
            aux_df = aux_df.astype(
                {k: aux_dtype_dict[k] for k in aux_dtype_dict.keys() & aux_df.columns},
            )

            # Drop the Aux column if it exists
            if "Aux" in aux_df.columns:
                aux_df = aux_df.drop(columns=["Aux"])

            # Append the aux ID to all columns except Index
            aux_df = aux_df.rename(
                columns = {col: f"{col}{aux_id}" for col in aux_df.columns if col not in ["Index"]},
            )

            # Merge into data_df on Index
            data_df = data_df.merge(aux_df, how="left", on="Index")

    if software_cycle_number:
        data_df['Cycle'] = _generate_cycle_number(data_df, cycle_mode)

    return data_df.astype(dtype=dtype_dict)


def _data_interpolation(df):
    """
    Some ndax from from BTS Server 8 do not seem to contain a complete dataset.
    This helper function fills in missing times, capacities, and energies.
    """
    logger.info(
        "The output from NewareNDA contains interpolated data in the fields "
        "Time, Timestamp, Capacity, and Energy."
    )
    # Identify the valid data
    nan_mask = df['Time'].notnull()  # 1 = valid, 0 = missing
    nan_groups = nan_mask.cumsum().shift(fill_value=0)  # contiguous nans = same group number

    # Forward fill time differences
    df['dt'] = df['dt'].ffill()

    # The time to add is the cumulative sum of dt over the nan groups
    time_inc = df['dt'].groupby(nan_groups).cumsum() * ~nan_mask
    df['Time'] = df['Time'].ffill() + time_inc
    df['Timestamp'] = df['Timestamp'].ffill() + pd.to_timedelta(time_inc, unit='s')

    # Integrate to get capacity and fill missing values
    capacity = df['dt'] * df['Current(mA)'] / 3600
    capacity_inc = capacity.groupby(nan_groups).cumsum() * ~nan_mask
    df['Charge_Capacity(mAh)'] = (
        df['Charge_Capacity(mAh)'].ffill().abs() + capacity_inc.clip(lower=0).abs()
    )
    df['Discharge_Capacity(mAh)'] = (
        df['Discharge_Capacity(mAh)'].ffill().abs() + capacity_inc.clip(upper=0).abs()
    )

    # Integrate to get energy and fill missing values
    energy = capacity*df['Voltage']
    energy_inc = energy.groupby(nan_groups).cumsum() * ~nan_mask
    df['Charge_Energy(mWh)'] = (
        df['Charge_Energy(mWh)'].ffill().abs() + energy_inc.clip(lower=0).abs()
    )
    df['Discharge_Energy(mWh)'] = (
        df['Discharge_Energy(mWh)'].ffill().abs() + energy_inc.clip(upper=0).abs()
    )


def read_ndc(file):
    """
    Function to read electrochemical data from a Neware ndc binary file.

    Args:
        file (str): Name of an .ndc file to read
    Returns:
        df (pd.DataFrame): DataFrame containing all records in the file
        aux_df (pd.DataFrame): DataFrame containing any temperature data
    """
    with open(file, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # Get ndc file version and filetype
        [ndc_filetype] = struct.unpack('<B', mm[0:1])
        [ndc_version] = struct.unpack('<B', mm[2:3])
        logger.debug(f"NDC version: {ndc_version} filetype: {ndc_filetype}")

        try:
            f = getattr(sys.modules[__name__], f"_read_ndc_{ndc_version}_filetype_{ndc_filetype}")
            return f(mm)
        except AttributeError:
            raise NotImplementedError(f"ndc version {ndc_version} filetype {ndc_filetype} is not yet supported!")


def _read_ndc_2_filetype_1(mm):
    record_len = 94
    identifier = mm[517:525]

    # Read data records
    output = []
    header = mm.find(identifier)
    while header != -1:
        mm.seek(header)
        bytes = mm.read(record_len)
        if bytes[0:1] == b'\x55':
            output.append(_bytes_to_list_ndc(bytes))
        else:
            logger.warning("Unknown record type: "+bytes[0:1].hex())

        header = mm.find(identifier, header + record_len)

    # Postprocessing
    df = pd.DataFrame(output, columns=[
        'Index', 'Cycle', 'Step_Index', 'Status', 'Time', 'Voltage',
        'Current(mA)', 'Charge_Capacity(mAh)', 'Discharge_Capacity(mAh)',
        'Charge_Energy(mWh)', 'Discharge_Energy(mWh)', 'Timestamp'])
    df['Step'] = _count_changes(df['Step_Index'])
    return df


def _read_ndc_2_filetype_5(mm):
    record_len = 94
    identifier = mm[517:525]

    # Read aux records
    aux = []
    header = mm.find(identifier)
    while header != -1:
        mm.seek(header)
        bytes = mm.read(record_len)
        if bytes[0:1] == b'\x65':
            aux.append(_aux_bytes_65_to_list_ndc(bytes))
        elif bytes[0:1] == b'\x74':
            aux.append(_aux_bytes_74_to_list_ndc(bytes))
        else:
            logger.warning("Unknown record type: "+bytes[0:1].hex())

        header = mm.find(identifier, header + record_len)

    # Postprocessing
    aux_df = pd.DataFrame([])
    if identifier[0:1] == b'\x65':
        aux_df = pd.DataFrame(aux, columns=['Index', 'Aux', 'V', 'T'])
    elif identifier[0:1] == b'\x74':
        aux_df = pd.DataFrame(aux, columns=['Index', 'Aux', 'V', 'T', 't'])

    return aux_df


def _read_ndc_5_filetype_1(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    output = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<87s', bytes[125:-56]):
            if i[0][7:8] == b'\x55':
                output.append(_bytes_to_list_ndc(i[0]))

    # Postprocessing
    df = pd.DataFrame(output, columns=[
        'Index', 'Cycle', 'Step_Index', 'Status', 'Time', 'Voltage',
        'Current(mA)', 'Charge_Capacity(mAh)', 'Discharge_Capacity(mAh)',
        'Charge_Energy(mWh)', 'Discharge_Energy(mWh)', 'Timestamp'])
    df['Step'] = _count_changes(df['Step_Index'])
    return df


def _read_ndc_5_filetype_5(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read aux records
    aux65 = []
    aux74 = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<87s', bytes[125:-56]):
            if i[0][7:8] == b'\x65':
                aux65.append(_aux_bytes_65_to_list_ndc(i[0]))
            elif i[0][7:8] == b'\x74':
                aux74.append(_aux_bytes_74_to_list_ndc(i[0]))

    # Concat aux65 and aux74 if they both contain data
    aux_df = pd.DataFrame(aux65, columns=['Index', 'Aux', 'V', 'T'])
    aux74_df = pd.DataFrame(aux74, columns=['Index', 'Aux', 'V', 'T', 't'])
    if (not aux_df.empty) & (not aux74_df.empty):
        aux_df = pd.concat([aux_df, aux74_df.drop(columns=['t'])])
    elif (not aux74_df.empty):
        aux_df = aux74_df

    return aux_df


def _read_ndc_11_filetype_1(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ff', bytes[132:-4]):
            if (i[0] != 0):
                rec.append([1e-4*i[0], i[1]])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=['Voltage', 'Current(mA)'])
    df['Index'] = df.index + 1
    return df


def _read_ndc_11_filetype_5(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    aux = []
    mm.seek(header)

    if mm[header+132:header+133] == b'\x65':
        while mm.tell() < mm_size:
            bytes = mm.read(record_len)
            for i in struct.iter_unpack('<cfh', bytes[132:-2]):
                if i[0] == b'\x65':
                    aux.append([i[1]/10000, i[2]/10])

        # Create DataFrame
        aux_df = pd.DataFrame(aux, columns=['V', 'T'])
        aux_df['Index'] = aux_df.index + 1

    elif mm[header+132:header+133] == b'\x74':
        while mm.tell() < mm_size:
            bytes = mm.read(record_len)
            for i in struct.iter_unpack('<cib29sh51s', bytes[132:-4]):
                if i[0] == b'\x74':
                    aux.append([i[1], i[2], i[4]/10])

        # Create DataFrame
        aux_df = pd.DataFrame(aux, columns=['Index', 'Aux', 'T'])

    return aux_df


def _read_ndc_11_filetype_7(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ii16sb12s', bytes[132:-5]):
            [Cycle, Step_Index, Status] = [i[0], i[1], i[3]]
            if Step_Index != 0:
                rec.append([Cycle+1, Step_Index, state_dict[Status]])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=['Cycle', 'Step_Index', 'Status'])
    df['Step'] = df.index + 1
    return df


def _read_ndc_11_filetype_18(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ixffff8xiiiih', bytes[132:-16]):
            Time = i[0]
            [Charge_Capacity, Discharge_Capacity] = [i[1], i[2]]
            [Charge_Energy, Discharge_Energy] = [i[3], i[4]]
            dt = i[5]
            [Timestamp, Step, Index] = [i[6], i[7], i[8]]
            Msec = i[9]
            if Index != 0:
                rec.append([Time/1000, dt/1000,
                            Charge_Capacity/3600, Discharge_Capacity/3600,
                            Charge_Energy/3600, Discharge_Energy/3600,
                            datetime.fromtimestamp(Timestamp + Msec/1000, timezone.utc), Step, Index])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=[
        'Time', 'dt',
        'Charge_Capacity(mAh)', 'Discharge_Capacity(mAh)',
        'Charge_Energy(mWh)', 'Discharge_Energy(mWh)',
        'Timestamp', 'Step', 'Index']).astype({'Time': 'float'})
    df['Step'] = _count_changes(df['Step'])

    # Convert timestamp to local timezone
    tz = datetime.now().astimezone().tzinfo
    df['Timestamp'] = df['Timestamp'].dt.tz_convert(tz)

    return df


def _read_ndc_14_filetype_1(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ff', bytes[132:-4]):
            if (i[0] != 0):
                rec.append([i[0], 1000*i[1]])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=['Voltage', 'Current(mA)'])
    df['Index'] = df.index + 1
    return df


def _read_ndc_14_filetype_5(mm):
    record_len = 4096
    header = 4096

    # Read data records
    aux = []
    mm.seek(header)
    while mm.tell() < mm.size():
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<f', bytes[132:-4]):
            aux.append(i[0])

    # Create DataFrame
    aux_df = pd.DataFrame(aux, columns=['?'])  # Placeholder - data type found later from TestInfo.xml
    aux_df['Index'] = aux_df.index + 1

    return aux_df


def _read_ndc_14_filetype_7(mm):
    return _read_ndc_11_filetype_7(mm)


def _read_ndc_14_filetype_18(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ixffff8xiiiih8s', bytes[132:-4]):
            Time = i[0]
            [Charge_Capacity, Discharge_Capacity] = [i[1], i[2]]
            [Charge_Energy, Discharge_Energy] = [i[3], i[4]]
            dt = i[5]
            [Timestamp, Step, Index] = [i[6], i[7], i[8]]
            Msec = i[9]
            if Index != 0:
                rec.append([Time/1000, dt/1000,
                            Charge_Capacity*1000, Discharge_Capacity*1000,
                            Charge_Energy*1000, Discharge_Energy*1000,
                            datetime.fromtimestamp(Timestamp + Msec/1000, timezone.utc), Step, Index])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=[
        'Time', 'dt',
        'Charge_Capacity(mAh)', 'Discharge_Capacity(mAh)',
        'Charge_Energy(mWh)', 'Discharge_Energy(mWh)',
        'Timestamp', 'Step', 'Index']).astype({'Time': 'float'})
    df['Step'] = _count_changes(df['Step'])

    # Convert timestamp to local timezone
    tz = datetime.now().astimezone().tzinfo
    df['Timestamp'] = df['Timestamp'].dt.tz_convert(tz)

    return df


def _read_ndc_17_filetype_1(mm):
    return _read_ndc_14_filetype_1(mm)


def _read_ndc_17_filetype_7(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ii16sb8si63s', bytes[132:-64]):
            [Cycle, Step_Index, Status, Index] = [i[0], i[1], i[3], i[5]]
            if Index != 0:
                rec.append([Cycle+1, Step_Index, state_dict[Status]])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=['Cycle', 'Step_Index', 'Status'])
    df['Step'] = _count_changes(df['Step_Index'])
    return df


def _read_ndc_17_filetype_18(mm):
    mm_size = mm.size()
    record_len = 4096
    header = 4096

    # Read data records
    rec = []
    mm.seek(header)
    while mm.tell() < mm_size:
        bytes = mm.read(record_len)
        for i in struct.iter_unpack('<ixffff8xiiiih53s', bytes[132:-64]):
            Time = i[0]
            [Charge_Capacity, Discharge_Capacity] = [i[1], i[2]]
            [Charge_Energy, Discharge_Energy] = [i[3], i[4]]
            dt = i[5]
            [Timestamp, Step, Index] = [i[6], i[7], i[8]]
            Msec = i[9]
            if Index != 0:
                rec.append([Time/1000, dt/1000,
                            Charge_Capacity*1000, Discharge_Capacity*1000,
                            Charge_Energy*1000, Discharge_Energy*1000,
                            datetime.fromtimestamp(Timestamp + Msec/1000, timezone.utc), Step, Index])

    # Create DataFrame
    df = pd.DataFrame(rec, columns=[
        'Time', 'dt',
        'Charge_Capacity(mAh)', 'Discharge_Capacity(mAh)',
        'Charge_Energy(mWh)', 'Discharge_Energy(mWh)',
        'Timestamp', 'Step', 'Index'])

    # Convert timestamp to local timezone
    tz = datetime.now().astimezone().tzinfo
    df['Timestamp'] = df['Timestamp'].dt.tz_convert(tz)

    return df


def _bytes_to_list_ndc(bytes):
    """Helper function for interpreting an ndc byte string"""

    # Extract fields from byte string
    [Index, Cycle, Step_Index, Status] = struct.unpack('<IIBB', bytes[8:18])
    [Time, Voltage, Current] = struct.unpack('<Qii', bytes[23:39])
    [Charge_capacity, Discharge_capacity,
     Charge_energy, Discharge_energy] = struct.unpack('<qqqq', bytes[43:75])
    [Y, M, D, h, m, s] = struct.unpack('<HBBBBB', bytes[75:82])
    [Range] = struct.unpack('<i', bytes[82:86])

    multiplier = multiplier_dict[Range]

    # Create a record
    list = [
        Index,
        Cycle + 1,
        Step_Index,
        state_dict[Status],
        Time/1000,
        Voltage/10000,
        Current*multiplier,
        Charge_capacity*multiplier/3600,
        Discharge_capacity*multiplier/3600,
        Charge_energy*multiplier/3600,
        Discharge_energy*multiplier/3600,
        datetime(Y, M, D, h, m, s)
    ]
    return list


def _aux_bytes_65_to_list_ndc(bytes):
    """Helper function for intepreting auxiliary records"""
    [Aux] = struct.unpack('<B', bytes[3:4])
    [Index] = struct.unpack('<I', bytes[8:12])
    [T] = struct.unpack('<h', bytes[41:43])
    [V] = struct.unpack('<i', bytes[31:35])

    return [Index, Aux, V/10000, T/10]


def _aux_bytes_74_to_list_ndc(bytes):
    """Helper function for intepreting auxiliary records"""
    [Aux] = struct.unpack('<B', bytes[3:4])
    [Index] = struct.unpack('<I', bytes[8:12])
    [V] = struct.unpack('<i', bytes[31:35])
    [T, t] = struct.unpack('<hh', bytes[41:45])

    return [Index, Aux, V/10000, T/10, t/10]
