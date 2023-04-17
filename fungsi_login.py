from terlarang import *
import random

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

#Fungsi Pengumpulan
def kumpul():
    def jin_pengumpul():
        return random.randint(0,5)
    
    jumlah_batu = jin_pengumpul()
    jumlah_pasir = jin_pengumpul()
    jumlah_air = jin_pengumpul()

    print("Jin menemukan", jumlah_pasir,"pasir,",jumlah_batu, "batu, dan",  jumlah_air,"air")

    #Fungsi Help
    def help(role):
    if role == "belum login":
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. load")
        print("   Untuk memuat file eksternal ke dalam permainan")
        print("3. exit")
        print("   Untuk keluar dari permainan")

    elif role == "Bandung Bondowoso":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin dan candi yang dibuat jin ikut terhapus apabila jin sudah dihapus")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin, yaitu berupa Jin Pengumpul dan Jin Pembangun")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pengumpul untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pembangun untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja dari para jin")
        print("8. laporancandi")
        print("   Untuk mengetahui progress pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")

    elif role == "Roro Jonggrang":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk memeriksa jumlah candi yang berhasil dibangun, mengetahui pemenangnya, dan mengakhiri permainan yang kemudian program akan otomatis terkeluar")
        print("4. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        
    elif role == "Jin Pengumpul":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
       
    elif role == "Jin Pembangun":
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")

    else:
        print("Role yang dimasukkan tidak valid")
