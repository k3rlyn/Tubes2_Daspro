from terlarang import *

def login():
    username = input("Username: ")
    password = input("Passowrd: ")
    arr = split_manual("user.csv")
    i = 0
    cek = True
    while cek == True:
        if i > 0:
            if username != arr[i][0]:
                print("Username tidak terdaftar!")
                cek = False
            elif username == arr[i][0] and password != arr[i][1]:
                print(arr[i][1])
                print("Password salah!")
                cek = False
            elif username == arr[i][0] and password == arr[i][1]:
                print("Selamat datang,",arr[i][0])
                cek = False
        i += 1

login()


