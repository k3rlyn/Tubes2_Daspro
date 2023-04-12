#Fungsi ini berfungsi untuk mengubah isi dari file csv. menjadi matriks dan masih mengandung ; dab \n
def isi_arr(file):
    f = open(file,"r")
    huruf = f.read(1)
    arr =[]
    while(huruf):
        arr += huruf
        huruf = f.read(1)
    return arr

#fungsi ini bisa dipakai buat mengetahui berapa jumlah barsi dari isi file .csv
def jmlh_baris(file):
    f = open(file,"r")
    huruf = f.read(1)
    i = 1
    arr =[]
    jmlh_enter = 0
    jmlh_tk = 0
    while(huruf):
        arr += huruf
        huruf = f.read(1)
        i += 1
        if huruf == ";":
            jmlh_tk += 1
        if huruf == "\n":
            jmlh_enter += 1
    return jmlh_enter

#Fungsi ini bisa dipakai buat split() secara manual, dalam kasus ini hanya berlaku untuk ;
def split_manual(file):
    arr = isi_arr(file)
    jmlh_enter = jmlh_baris(file)
    real_split = []
    arr_split = []
    temp =""
    j = 0
    k = 0
    for i in range(jmlh_enter):
        while(arr[j] != "\n"):
            if arr[j] != ";":
                temp += arr[j]
            elif arr[j] == ";":
                arr_split += [temp]
                temp = ""
            j += 1
        arr_split += [temp]
        real_split += [arr_split]
        arr_split = []
        temp =""
        j += 1
    
    return real_split

print(split_manual("user.csv"))

#keunggulan fungsi ini bisa mengetahui ada berapa baris
#tidak ada ;
#tidaka 


    
    
    


