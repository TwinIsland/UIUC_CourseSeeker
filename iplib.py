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
    proxy = list(zip(ip_list, port_list))
    proxy.append(time.time())

    with open("pool", "wb") as a:
        a.write(pickle.dumps(proxy))


def get_header():
    return "{'content-type': 'application/json'}"


class IpLib:
    try:
        with open("pool", "rb") as a:
            res = list(pickle.loads(a.read()))
        print(res)
        if time.time() - res[-1] > 86400:
            updateLib()
            eventRec.ok_msg(msg="ip pool update")
            res = pickle.loads(open("pool", "rb").read())
    except FileNotFoundError:
        updateLib()
        res = list(pickle.loads(open("pool", "rb").read()))

    res = res.pop()

    def get_ip(self):
        return random.choice(self.res)
