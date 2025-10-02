

def parse_course_data(course_data):
    courses_dict = {}
    for course in course_data:
        courses_dict[course.get('id')] = {
            'course_code': course.get('course_code'),
            'course_name': course.get('name')
        }
    return courses_dict

def filter_online_courses(courses_dict):
    online_courses = {}
    for course_id, details in courses_dict.items():
        course_code = details.get('course_code', '')
        if 'OL-1' not in course_code and 'OL-2' not in course_code and 'UNV-800' not in course_code:
            online_courses[course_id] = details
    return online_courses