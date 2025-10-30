import config.config as config
from utils.retry_request import retry_get

def get_enrollments(course_id):
    url = f'{config.API_URL}/v1/courses/{course_id}/enrollments'
    enrollment_data = retry_get(url, {})

    if len(enrollment_data) == 0:
        print(f'No enrollment data for course {course_id}')
        return course_id
    return