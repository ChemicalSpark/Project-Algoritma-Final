import csv
import pandas as pd

def list_kategori():
    df = pd.read_csv('database/kategori.csv')
    print(df)

def tambah_kategori(new_kategori):
    with open('database/kategori.csv','r') as file:
        data = [row.strip().split(',') for row in file.readlines()]
        length = len(data)
        data_temp = f"{length},{new_kategori}\n"
    with open('database/kategori.csv','a') as add_kategori:
        add_kategori.write(data_temp)
        
def hapus_kategori():
    pass
print("[KATEGORI]")
print("Menu: ")
print("""1. List Kategori
2. Tambah Kategori
""")
user = int(input("Pilihan: "))
match user:
    case 1:
        list_kategori()
    case 2:
        print("Masukkan kategori baru!")
        user = input("Kategori: ")
        tambah_kategori(user)
    case 3:
        pass