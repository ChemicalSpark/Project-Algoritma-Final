import csv
import pandas

def list_kategori():
    with open('Project-Algoritma-Final/database/kategori.csv', 'r') as db_kategori:
        read = db_kategori.read()
        print(read)

def tambah_kategori():
    id_kategori = 1
    print("Tambahkan Kategori!")
    add_kategori = input("Masukkan kategori: ")
    with open('Project-Algoritma-Final/database/kategori.csv', 'a') as write_kategori:
        write_kategori.write(add_kategori)
        

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