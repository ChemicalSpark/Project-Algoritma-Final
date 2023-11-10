import os
import core


def tampilkan_daftar():
    exit()

def daftar_peminjaman():
    exit()


def tambah_peminjaman_baru():
    exit()

def perbarui_peminjaman():
    exit()

def hapus_peminjamam():
    exit()



while True:
    core.clear()
    with open('ui/data_peminjaman.txt', 'r') as f:
        print(f.read())
    input_user = int(input("Pilih operasi anda (angka) : "))
    
    match (input_user):
        case 1 :
            daftar_peminjaman()
        case 2 :
            tambah_peminjaman_baru()
        case 3 :
            perbarui_peminjaman()
        case 4 :
            hapus_peminjamam()
        case 9 :
            break
        case 0 :
            exit("Program Ditutup")
        case _ :
            print("Input Tidak Valid!")
    # end match
    