import time
from datetime import datetime
import pandas as pd
import config.config as config
import utils.courses as courses
import utils.parse as parse
import utils.dataframe_utils as df_utils

def main():
    start = time.perf_counter()
    
    course_data = courses.get_courses()
    courses_dict = parse.parse_course_data(course_data)
    online_courses = parse.filter_online_courses(courses_dict)
    df = df_utils.build_course_dataframe(online_courses)
    feed_df = df_utils.reformat_dataframe(df, config.TEMPLATE_COLUMNS)

    current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    report_file_name = f"./reports/readygo_online_{current_time}.xlsx"
    with pd.ExcelWriter(report_file_name, engine="openpyxl") as writer:
        feed_df.to_excel(writer, sheet_name="Feed", index=False)

    end = time.perf_counter()
    seconds = end - start
    elapsed = seconds / 60

    print(f'Elapsed time: {elapsed:.2f} minutes')

if __name__ == "__main__":
    main()