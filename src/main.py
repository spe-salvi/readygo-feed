import time
from config.config import *
import utils.courses as courses
import utils.parse as parse
import utils.dataframe_utils as df_utils

def main():
    start = time.perf_counter()
    
    course_data = courses.get_courses()
    courses_dict = parse.parse_course_data(course_data)
    online_courses = parse.filter_online_courses(courses_dict)
    df = df_utils.build_course_dataframe(online_courses)
    print(df)


    end = time.perf_counter()
    seconds = end - start
    elapsed = seconds / 60

    print(f'Elapsed time: {elapsed:.2f} minutes')

if __name__ == "__main__":
    main()