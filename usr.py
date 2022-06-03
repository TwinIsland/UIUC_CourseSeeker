import json
import encryption

def get_cookies_address(sId):
    return "UsrLib/" + sId + '.pkl'


class User:
    with open("UsrLib/Usr.json", 'r') as usr:
        usrDict = json.loads(usr.read())
    usr.close()
    encrypt = encryption.Encryption()

    def __update_database(self):
        with open("UsrLib/Usr.json", 'w') as usr:
            usr.write(json.dumps(self.usrDict))
        usr.close()

    def get_pwd_by_id(self, sId):
        return self.encrypt.dec(self.usrDict[sId]['pwd'])

    def add_usr(self, sId, pwd):
        self.usrDict[sId] = {
            "pwd": self.encrypt.enc(pwd),
        }
        self.__update_database()

    def remove_usr(self, sId):
        self.usrDict.pop(sId)
        self.__update_database()

    def change_pwd(self, sId, pwd):
        self.usrDict[sId] = {
            "pwd": self.encrypt.enc(pwd)
        }
        self.__update_database()

    def get_id_list(self):
        return self.usrDict.keys()
