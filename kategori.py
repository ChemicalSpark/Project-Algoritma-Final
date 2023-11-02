import csv

def list_kategori():
    with open('database/kategori.csv', 'r') as db_kategori:
        read = db_kategori.read()
        print(read)

def tambah_kategori():
    print("Tambahkan Kategori!")
    add_kategori = input("Masukkan kategori: ")

def hapus_kategori():
    pass

list_kategori()