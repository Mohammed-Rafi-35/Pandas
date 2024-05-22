import pandas as pd

def import_check( DATA ):
    CHECK = pd.read_csv('./Data Sets/AppleStore.csv')

    if CHECK.equals( DATA ):
        return 'Correct'
    else:
        return 'Incorrect'
    
def TASK_1( DATA_1 ):
    CHECK = pd.read_csv("./Data Sets/YouTube.csv")

    if CHECK.equals( DATA_1 ):
        return 'Correct'
    else:
        return 'Incorrect'
    
def TASK_2( DATA_2 ):
    CHECK = pd.read_csv("./Data Sets/YouTube.csv")

    if DATA_2.equals( CHECK.head(10) ):
        return 'Correct'
    else:
        return 'Incorrect'
    
def TASK_3( DATA_3 ):
    CHECK = pd.read_csv("./Data Sets/YouTube.csv")

    if DATA_3.equals( CHECK.tail(20) ):
        return 'Correct'
    else:
        return 'Incorrect'