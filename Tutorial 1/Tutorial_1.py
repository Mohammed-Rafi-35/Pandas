import pandas as pd

def TASK_1(DATAFRAME_1):
    CHECK = pd.DataFrame({'Apple': [69, 27, 27, 27], 'Banana': [45, 67, 78, 45], 'Cherry': [34, 68, 48, 57]})

    if DATAFRAME_1.equals(CHECK):
        return "Correct Answer!"
    else:
        return "Incorrect Answer!"
