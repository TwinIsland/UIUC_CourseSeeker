from os.path import exists
import eventRec
import rsa


def new_series():
    publicKey, privateKey = rsa.newkeys(2048)
    publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8')
    privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8')
    with open("ENCRY_kEY/PUB.PEM", "w") as a:
        a.write(publicKeyPkcs1PEM)
    a.close()
    with open("ENCRY_kEY/KEY.PEM", "w") as a:
        a.write(privateKeyPkcs1PEM)
    a.close()
    eventRec.ok_msg(msg="encryption key generated")


if not exists("ENCRY_kEY/PUB.PEM") or not exists("ENCRY_kEY/KEY.PEM"):

    while 1:
        ans = input("input: \"COURSESEEKER\" to process, please make sure"
                    " the program is brand new or will cause data loss:\n")
        if ans == "COURSESEEKER":
            break
        else:
            print("input again")

    print("init key...")
    new_series()
    print("init done\n!!! PLEASE BACKUP YOUR ENCRY_KEY FOLD !!!")
    eventRec.ok_msg(msg="init key")
    input("\npress enter to leave...")
    exit()
else:
    print("already init...")
