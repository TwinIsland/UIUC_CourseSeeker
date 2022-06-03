import time
import eventRec
import iplib
import requests
from bs4 import BeautifulSoup
import json
import pprint

DEFAULT_COURSE_URL = "https://courses.illinois.edu/schedule/2022/fall/CS/233"


class SuperviseCourses:
    def __init__(self,
                 course: dict,
                 updateFreq=10,
                 endSession=time.time() + 604800,
                 keepSession=False,
                 retry=5):
        self.course = course
        self.updateFreq = updateFreq
        self.endSession = endSession
        self.keepSession = keepSession
        self.ip_pool = iplib.IpLib()
        self.course_spec = ""
        self.retry = retry

    def start(self):
        url, uid = self.course["url"], self.course["crn"]
        try:
            html = requests.get(url,
                                proxies=self.ip_pool.get_ip(),
                                headers=iplib.get_header()).content.decode("utf-8")

            soup = BeautifulSoup(html, 'lxml')
            course_desc = str(soup.find_all('script', attrs={'type': 'text/javascript'})[1])
            course_desc = "[" + course_desc.split("[")[1].split("]")[0] + "]"
            course_desc = json.loads(course_desc)
            for i in course_desc:
                if i["crn"] == str(self.course["crn"]):
                    self.course_spec = i
                    del course_desc
                    break
            pprint.pprint(self.course_spec)
        except Exception as e:
            print(e)
            if self.retry:
                eventRec.fail_msg(msg="internet retry fail: " + str(e))
                exit()
            self.retry -= 1
            print("internet error, retry: " + str(self.retry))
            time.sleep(2)
        # while self.keepSession or time.time() < self.endSession:


test = SuperviseCourses({"url": "https://courses.illinois.edu/schedule/2022/fall/CS/233",
                         "crn": 72276})
test.start()
