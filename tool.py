import config
import re
import superviseCourse


def get_course_info(course_name: str, crn: str) -> dict:
    course_title, course_number = re.split(r'(\d+)', course_name.upper())[:2]
    return {"url": config.Config.semester_root + course_title + '/' + course_number,
            "crn": crn}


def is_valid_course(course: dict[str, str]) -> bool:
    course_s = superviseCourse.SuperviseCourses(course, "ADMIN")
    ans = course_s.update_course_spec()
    del course_s
    return ans

