from terlarang import *
from fungsi_login import *
from test import *

users = read_csv_file('data_csv\\user.csv', separator=';')
candi = read_csv_file('data_csv\\candi.csv', separator=';')
#bahan_bangunan = read_csv_file('data_csv\\bahan_bangunan.csv', separator=';')

login_status = False
username = ""

while True:
    masukan = input(">>> ")
    if masukan == "login":
        username,login_status = login(users=users,login_status=login_status,username=username)
    else : 
      ("test awal")
