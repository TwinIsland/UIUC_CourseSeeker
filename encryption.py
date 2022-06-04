from cryptography.fernet import Fernet
from os.path import exists
import eventRec


class Encryption:
    if not exists("ENCRY_kEY/KEY"):
        print("ENCRYPT KEY INIT FAILED !")
        eventRec.fail_msg(msg="encryption init failed")
        exit()
    with open("ENCRY_kEY/KEY", "rb") as a:
        fernet = Fernet(a.read())

    def enc(self, plaintext: str) -> str:
        return self.fernet.encrypt(plaintext.encode()).decode("utf-8")

    def dec(self, ciphertext: str) -> str:
        return self.fernet.decrypt(ciphertext.encode()).decode()
