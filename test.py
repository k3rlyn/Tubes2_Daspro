from terlarang import *

def login():
    username = input("Username: ")
    password = input("Password: ")
    arr = split_manual("user.csv")
    login_status = False
    user = ""
    for i in range(len(arr)):
        if username == arr[i][0]:
            if password == arr[i][1]:
                print("Selamat datang,", arr[i][0])
                login_status = True
                user = arr[i][0]
                return user, login_status
            else:
                print("Password salah!")
                return user, login_status
        else:
            print("Username tidak terdaftar!")
            return user, login_status
