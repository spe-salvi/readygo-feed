import time
from datetime import datetime
import pandas as pd
import config.config as config
import utils.courses as courses
import utils.enrollments as enrollments
import utils.parse as parse
import utils.dataframe_utils as df_utils

def main():
    start = time.perf_counter()
    
    course_data = courses.get_courses()
    courses_dict = parse.parse_course_data(course_data)
    online_courses = parse.filter_online_courses(courses_dict)

    cancelled_courses = []
    for course_id in online_courses.keys():
        # print(f'Checking enrollments for course {course_id}')
        cancelled_courses.append(enrollments.get_enrollments(course_id))

    if config.NO_CANCELLED_COURSES:
        online_courses = {cid: details for cid, details in online_courses.items() if cid not in cancelled_courses}

    df = df_utils.build_course_dataframe(online_courses)
    feed_df = df_utils.reformat_dataframe(df, config.TEMPLATE_COLUMNS)

    current_time = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    report_file_name = f"./reports/readygo_online_{current_time}.csv"
    
    feed_df.to_csv(report_file_name, index=False, encoding='utf-8-sig')

    end = time.perf_counter()
    seconds = end - start
    elapsed = seconds / 60

    print(f'Elapsed time: {elapsed:.2f} minutes')

if __name__ == "__main__":
    main()