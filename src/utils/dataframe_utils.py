import pandas as pd

def build_course_dataframe(courses: dict) -> pd.DataFrame:
    df = pd.DataFrame.from_dict(courses, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'course_id'}, inplace=True)
    return df
    
def reformat_dataframe(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    # Ensure we're working on a copy
    df = df.copy()

    # Map your course data to sisCourseIds (your parse_course_data sets sis_course_id)
    if "sis_course_id" in df.columns:
        df["sisCourseIds"] = df["sis_course_id"]
    else:
        df["sisCourseIds"] = ""

    # Add any missing template columns
    for col in columns:
        if col not in df.columns:
            df[col] = ""

    # Return dataframe with columns in the right order
    return df[columns]