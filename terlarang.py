#Fungsi ini berfungsi untuk mengubah isi dari file csv. menjadi matriks dan masih mengandung ; dab \n
def isi_arr(file):
    f = open(file,"r")
    huruf = f.read(1)
    arr =[]
    while(huruf):
        arr += huruf
        huruf = f.read(1)
    f.close()
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
    f.close()
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

#fungsi ini bisa dipakai untuk mengaplikasikan fungsi len 
def length(x) :
    length = 0
    for i in range (x) :
        length += 1
    return length 

#fungsi ini bisa dipakai untuk mengaplikasikan fungsi append 
def add(x,y):
    new_list = [0 for i in range(length(x)+1)]
    for i in range(length(x)):
        new_list[i] = x[i]
    new_list[-1] = y
    return new_list

#karena tidak diperbolehkan menggunakan import.csv maka akan dibuat sebuah fungsi yang akan membaca file csv 
def read_csv_file(filename, separator=','):
    result_list = []
    with open(filename, 'r') as file:
        for line in file:
            row = split_manual(line, separator)
            result_list = add(result_list, row)
    return result_list

#keunggulan fungsi ini bisa mengetahui ada berapa baris
#tidak ada ;
#tidaka 


    
    
    


