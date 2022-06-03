import time
import eventRec
import iplib
from lxml import etree
import requests

DEFAULT_COURSE_URL = "https://courses.illinois.edu/schedule/2022/fall/CS/233"


class CourseSeeker:
    def __init__(self,
                 courseURL: list,
                 updateFreq=10,
                 endSession=time.time() + 604800,
                 keepSession=False):
        self.courseURL = courseURL
        self.updateFreq = updateFreq
        self.endSession = endSession
        self.keepSession = keepSession

    def beginMission(self):
        while self.keepSession or time.time() < self.endSession:
            return 1
