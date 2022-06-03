import time
import eventRec
import iplib
from lxml import etree
import requests

c = requests.get("https://courses.illinois.edu/schedule/2022/fall/CS/233").content
