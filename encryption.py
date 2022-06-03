import rsa
from os.path import exists
import eventRec


class Encryption:
    if not exists("ENCRY_kEY/PUB.PEM") or not exists("ENCRY_kEY/KEY.PEM"):
        print("ENCRYPT KEY INIT FAILED !")
        eventRec.rec_msg("encryption init failed")
        exit()
    with open("ENCRY_kEY/PUB.PEM", "r") as a:
        publicKeyReloaded = rsa.PublicKey.load_pkcs1(a.read().encode('utf8'))
    a.close()
    with open("ENCRY_kEY/KEY.PEM", "r") as a:
        privateKeyReloaded = rsa.PrivateKey.load_pkcs1(a.read().encode('utf8'))
    a.close()

    def enc(self, plaintext: str) -> bytes:
        return rsa.encrypt(plaintext.encode(), self.publicKeyReloaded)

    def dec(self, ciphertext: bytes) -> str:
        return rsa.decrypt(ciphertext, self.privateKeyReloaded).decode()
