import usr
import eventRec

user = usr.User()

print("id          Code")
print("------------------------")
for sId in user.get_id_list():
    print(str(sId) + "          " + user.get_pwd_by_id(sId))
print("------------------------")
print("del [id]: Remove User\n"
      "add [id] [pwd]: Add User\n"
      "cp [id] [pwd]: Change Pwd\n"
      "exit: End")

whitelist = ['del', 'add', 'cp', 'exit']
while True:
    ip = str(input("\n<<<")).split(" ")
    if ip[0] in whitelist:
        if ip[0] == "del":
            if ip[1] not in user.get_id_list():
                print("-->No matching User")
                continue
            else:
                user.remove_usr(ip[1])
                eventRec.ok_msg(msg="remove user: " + ip[1])
        elif ip[0] == "add" and len(ip) == 3:
            user.add_usr(ip[1], ip[2])
            eventRec.ok_msg(msg="add user: " + ip[1])
        elif ip[0] == "cp" and len(ip) == 3:
            if ip[1] not in user.get_id_list():
                print("-->No matching User")
                continue
            user.change_pwd(ip[1], ip[2])
            eventRec.ok_msg(ip[1], "change pwd")
        elif ip[0] == "exit":
            break
        else:
            print("-->Invalided Input")
            continue
        print("\nid          Code")
        print("------------------------")
        for sId in user.get_id_list():
            print(str(sId) + "          " + user.get_pwd_by_id(sId))
        print("------------------------")
    else:
        print("-->Invalided Input")
