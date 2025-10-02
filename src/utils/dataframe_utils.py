import pandas as pd

def build_course_dataframe(courses: dict) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(courses, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'course_id'}, inplace=True)
    return df
    
def reformat_dataframe(df: pd.DataFrame, columns: list) -> pd.DataFrame:

    return df[columns]