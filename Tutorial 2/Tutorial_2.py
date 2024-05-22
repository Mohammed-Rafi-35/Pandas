import pandas as pd

def import_check( DATA ):
    CHECK = pd.read_csv('./Data Sets/AppleStore.csv')

    if CHECK.equals( DATA ):
        return 'Correct'
    else:
        return 'Incorrect'