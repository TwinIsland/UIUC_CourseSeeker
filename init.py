from os.path import exists
import eventRec
from cryptography.fernet import Fernet


def new_series():
    key = Fernet.generate_key()
    with open("ENCRY_KEY/KEY", "wb") as a:
        a.write(key)
    a.close()


if not exists("ENCRY_KEY/KEY"):

    while 1:
        ans = input("input: \"COURSESEEKER\" to process, please make sure"
                    " the program is brand new or will cause data loss:\n")
        if ans == "COURSESEEKER":
            break
        else:
            print("input again")

    new_series()
    print("init done\n!!! PLEASE BACKUP YOUR ENCRY_KEY FOLD !!!")
    eventRec.ok_msg(msg="init key")
    input("\npress enter to leave...")
    exit()
else:
    print("already init")
