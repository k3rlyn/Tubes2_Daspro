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
