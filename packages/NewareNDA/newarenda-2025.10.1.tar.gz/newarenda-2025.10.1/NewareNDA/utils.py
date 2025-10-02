import logging

logger = logging.getLogger('newarenda')


def _generate_cycle_number(df, cycle_mode='chg'):
    """
    Generate a cycle number to match Neware.

    cycle_mode = chg: (Default) Sets new cycles with a Charge step following a Discharge.
        dchg: Sets new cycles with a Discharge step following a Charge.
        auto: Identifies the first non-rest state as the incremental state.
    """

    # Auto: find the first non rest cycle
    if cycle_mode.lower() == 'auto':
        cycle_mode = _id_first_state(df)

    # Set increment key and non-increment/off key
    if cycle_mode.lower() == 'chg':
        inkey = 'Chg'
        offkey = 'DChg'
    elif cycle_mode.lower() == 'dchg':
        inkey = 'DChg'
        offkey = 'Chg'
    else:
        logger.error(f"Cycle_Mode '{cycle_mode}' not recognized. Supported options are 'chg', 'dchg', and 'auto'.")
        raise KeyError(f"Cycle_Mode '{cycle_mode}' not recognized. Supported options are 'chg', 'dchg', and 'auto'.")

    # Identify the beginning of key incremental steps
    inc = (df['Status'] == 'CCCV_'+inkey) | (df['Status'] == 'CC_'+inkey) | (df['Status'] == 'CP_'+inkey)

    # inc series = 1 at new incremental step, 0 otherwise
    inc = (inc - inc.shift()).clip(0)
    inc.iat[0] = 1

    # Convert to numpy arrays
    inc = inc.values
    status = df['Status'].values

    # Increment the cycle at a charge step after there has been a discharge, or vice versa
    cyc = 1
    Flag = False
    for n in range(len(inc)):
        # Get Chg/DChg status
        try:
            method, state = status[n].split('_', 1)
        except ValueError:
            # Status is SIM or otherwise. Set Flag
            Flag = True if status[n] == 'SIM' else Flag

        else:
            # Standard status type
            if inc[n] & Flag:
                # Increment the cycle number and reset flag when flag is active and the incremental step changes
                cyc += 1
                Flag = False
            elif state == offkey:
                Flag = True

        finally:
            inc[n] = cyc

    return inc


def _count_changes(series):
    """Enumerate the number of value changes in a series"""
    a = series.diff()
    a.iloc[0] = 1
    return (abs(a) > 0).cumsum()


def _id_first_state(df):
    """Helper function to identify the first non-rest state in a cycling profile"""
    nonrest_states = df[df['Status'] != 'Rest']['Status']

    # If no non-rest cycles exist, just pick a mode; it doesn't matter.
    if len(nonrest_states) > 0:
        first_state = nonrest_states.iat[0]
    else:
        return 'chg'

    try:
        _, cycle_mode = first_state.split('_', 1)
    except ValueError:
        # Status is SIM or otherwise. Set mode to chg
        logger.warning("First Step not recognized. Defaulting to Cycle_Mode 'Charge'.")
        cycle_mode = 'chg'

    return cycle_mode.lower()
