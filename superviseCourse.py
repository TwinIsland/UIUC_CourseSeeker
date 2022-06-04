import time
import eventRec
import iplib
import requests
from bs4 import BeautifulSoup
import json


class SuperviseCourses:
    def __init__(self,
                 course: dict[str, str],
                 user: str,
                 updateFreq=10,
                 endSession=time.time() + 604800,
                 keepSession=False,
                 retry=5,
                 forceExit=20):
        self.course = course
        self.updateFreq = updateFreq
        self.endSession = endSession
        self.keepSession = keepSession
        self.ip_pool = iplib.IpLib()
        self.course_spec = {}
        self.retry = retry
        self.user = user
        self.forceExit = forceExit

    def update_course_spec(self):
        url, uid = self.course["url"], self.course["crn"]
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
                return True
        return False

    def get_status(self):
        try:
            if self.update_course_spec():
                soup = BeautifulSoup(self.course_spec["status"], "lxml")
                return int(soup.find(class_="hide").text)
            else:
                print("invalid content, retry: " + str(self.retry))
                self.retry -= 1
                self.forceExit -= 1
                return -1
        except Exception as e:
            print("internet error - {}, retry: ".format(str(e)) + str(self.retry))
            eventRec.fail_msg(self.user, "internet error with " + str(e))
            self.retry -= 1
            self.forceExit -= 1
            return -1

    def start(self):
        print(eventRec.rec_msg(self.user, "start supervising..."))
        while self.forceExit >= 0 and self.keepSession or (time.time() < self.endSession and self.retry >= 0):
            if self.get_status() == 1:
                print(eventRec.ok_msg(self.user, "find course: " + self.course_spec["crn"]))
                return True
            time.sleep(self.updateFreq)
        print(eventRec.ok_msg(self.user, "session end"))
        if self.retry < 0:
            eventRec.fail_msg(self.user, "run out of retry")
        if self.forceExit < 0:
            eventRec.fail_msg(self.user, "run out of force retry")
        return False


test = SuperviseCourses({"url": "https://courses.illinois.edu/schedule/2022/fall/CS/233",
                         "crn": 64548},
                        user="test")

test.start()
