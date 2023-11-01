import csv

def list_kategori():
    with open('database/kategori.csv', 'r') as db_kategori:
        read = db_kategori.read()
        print(read)

def tambah_kategori():
    pass

def hapus_kategori():
    pass

list_kategori()