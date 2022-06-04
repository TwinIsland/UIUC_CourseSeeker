import requests as re
import json
import pickle
import time
import eventRec
import random


def update_lib():
    print("updating IpLib...")
    c = json.loads(re.get("https://proxylist.geonode.com/api/proxy-list")
                   .content
                   .decode("utf-8"))

    proxy = []
    for i in c["data"]:
        if i["protocols"][0] in ["http", "https"]:
            proxy.append({i["protocols"][0]: i["ip"] + ':' + i["port"]})
        else:
            proxy.append({"http": i["protocols"][0] + "://" + i["ip"] + ':' + i["port"]})

    proxy.append(time.time())

    with open("pool", "wb") as a:
        a.write(pickle.dumps(proxy))


def get_header():
    return {"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
            "Safari/537.36",
            "Accept-Language": "gzip, deflate"}


class IpLib:
    try:
        with open("pool", "rb") as a:
            res = list(pickle.loads(a.read()))
        if time.time() - res[-1] > 43200:
            update_lib()
            eventRec.ok_msg(msg="ip pool update")
            res = pickle.loads(open("pool", "rb").read())
    except FileNotFoundError:
        update_lib()
        res = list(pickle.loads(open("pool", "rb").read()))

    res.pop()

    def get_ip(self):
        return random.choice(self.res)
