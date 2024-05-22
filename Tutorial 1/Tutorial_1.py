import pandas as pd

def TASK_1(DATAFRAME_1):
    CHECK = pd.DataFrame({'Apple': [69, 27, 27, 27], 'Banana': [45, 67, 78, 45], 'Cherry': [34, 68, 48, 57]})

    if DATAFRAME_1.equals(CHECK):
        return "Correct Answer!"
    else:
        return "Incorrect Answer!"


def TASK_2(DATAFRAME_2):
    CHECK = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

    if DATAFRAME_2.equals(CHECK):
        return "Correct Answer!"
    else:
        return "Incorrect Answer!"
    
    
def TASK_3( SERIES_1 ):
    CHECK = pd.Series( [57, 32, 26, 67, 56] )

    if SERIES_1 == CHECK:
        return 'Correct Answer!'
    else:
        return 'Incorrect Answer!'
    
def TASK_4( DATAFRAME ):
    DATA = {'Apple': [15, 30], 'Banana': [15, 45], 'Cherry': [10, 20]}
    INDEX = ['Sales 2023', 'Sales 2024']

    CHECK = pd.DataFrame(DATA, index = INDEX )

    if CHECK.equals(DATAFRAME):
        return 'Correct Answer'
    else:
        return 'Incorrect Answer'