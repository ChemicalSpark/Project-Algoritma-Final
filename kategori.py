import csv
import pandas as pd

def list_kategori():
    df = pd.read_csv('database/kategori.csv')
    print(df)

def tambah_kategori():
    id_kategori = 1
    print("Tambahkan Kategori!")
    add_kategori = input("Masukkan kategori: ")
    
    
        

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
        tambah_kategori()
    case 3:
        pass