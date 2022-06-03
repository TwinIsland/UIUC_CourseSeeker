import requests as re
import json
import pickle
import time
import random
import eventRec


def updateLib():
    print("updating IpLib...")
    c = json.loads(re.get("https://proxylist.geonode.com/api/proxy-list")
                   .content
                   .decode("utf-8"))

    ip_list = [i["ip"] for i in c["data"]]
    port_list = [i["port"] for i in c["data"]]
    proxy = {}
    for i in range(len(ip_list)):
        proxy[ip_list[i]] = port_list[i]
    proxy["sessionTime"] = time.time()

    with open("pool", "wb") as a:
        a.write(pickle.dumps(proxy))


def get_header():
    return "{'content-type': 'application/json'}"


class IpLib:
    try:
        with open("pool", "rb") as a:
            res = dict(pickle.loads(a.read()))
        if time.time() - res["sessionTime"] > 86400:
            updateLib()
            eventRec.ok_msg(msg="ip pool update")
            res = pickle.loads(open("pool", "rb").read())
    except FileNotFoundError:
        updateLib()
        res = dict(pickle.loads(open("pool", "rb").read()))

    res.pop("sessionTime")

    def get_ip(self):
        return random.choice(self.res)
