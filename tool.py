import config
import requests
import re
import iplib
from bs4 import BeautifulSoup
import json


def get_course_info(course_name: str, crn: str) -> dict:
    course_title, course_number = re.split(r'(\d+)', course_name.upper())[:2]
    return {"url": config.Config.semester_root + course_title + '/' + course_number,
            "crn": crn}


def is_valid_course(course: dict[str, str]) -> bool:
    ip_pool = iplib.IpLib()
    url, uid = course["url"], course["crn"]
    html = requests.get(url,
                        proxies=ip_pool.get_ip(),
                        headers=iplib.get_header()).content.decode("utf-8")

    soup = BeautifulSoup(html, 'lxml')
    course_desc = str(soup.find_all('script', attrs={'type': 'text/javascript'})[1])
    course_desc = "[" + course_desc.split("[")[1].split("]")[0] + "]"
    course_desc = json.loads(course_desc)
    for i in course_desc:
        if i["crn"] == str(course["crn"]):
            return True
    return False


print(get_course_info("cs225", "62137"))
print(is_valid_course(get_course_info("cs225", "62137")))
