from terlarang import *

def login():
    username = input("Username: ")
    password = input("Password: ")
    arr = split_manual("user.csv")
    login_status = False
    username = ''
    count = 0
    for i in arr: #menggantikan fungsi len()
        count += 1
    for i in range(count):
        if username == arr[i][0]:
            if password == arr[i][1]:
                print("Selamat datang,", arr[i][0])
                login_status = True
                username = arr[i][0]
                return username, login_status #di setiap kondisi if harus ada return karena tidak diperbolehkan menggunakan "break"
            else:
                print("Password salah!")
                return username, login_status
    
    print("Username tidak terdaftar!") #ketika pengecekan username di line 13 tidak terpenuhi maka akan keluar loop dan berarti name tidak terdaftar
    return username, login_status
        

def logout(login_status) :
    if login_status == True :
        login_status = False 
        print("Keluar dari akun")
        return(login_status)
    else : #blm login
        print("Maaf anda belum login")
        return(login_status)


