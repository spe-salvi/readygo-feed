import config.config as config
from utils.retry_request import retry_get

def get_courses():
    url = f'{config.API_URL}/v1{config.FUS_ACCOUNT}/courses?search_term={config.SEARCH_TERM}'
    params = {"enrollment_term_id": config.TERM}
    course_data = retry_get(url, params=params)
    return course_data