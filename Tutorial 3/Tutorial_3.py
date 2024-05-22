import pandas as pd
import Tutorial_3

RAMEN = pd.read_csv('./Data Sets/ramen-ratings.csv')

def TASK_1( OUT ):

    if OUT.equals( RAMEN.head(10) ):
        return 'Correct'
    else:
        return 'Incorrect'