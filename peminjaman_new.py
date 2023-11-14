import os
import core
import pandas as pd
from datetime import datetime,date

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'



def hapus_baris(nama_file_csv,id):
    data = core.baca_csv(nama_file_csv)
    index_baris = core.cari_index_dengan_id_list(data, id)
    core.hapus_baris_csv(nama_file_csv, index_baris)


def perbarui_baris():
    exit()


# Fungsi Fungsi setelah Memilih Fitur

def tambah_peminjaman():
    nama = input("Masukkan NIM Peminjam: ")
    isbn = input("Masukkan ID Buku: ")
    tglpinjam = input("Masukkan Tanggal Peminjaman: ")
    tglkembali = input("Masukkan Tanggal Kembali: ")
    status = input("Masukkan Status: ")
    print("Data telah ditambahkan."+'\n')

def tampilkan_peminjaman():
    print("Data saat ini:")
    baca_baris(db_peminjaman)
    print("\n")

def perbarui_peminjaman():
    id = input("Masukkan ID Peminjaman yang akan diperbarui: ")
    data = core.cari_id_list(core.baca_csv(db_peminjam), id)
    if data == False:
        print("Data Tidak ada"+'\n')
    else:
        print("NIM Peminjam lama :", data[1])
        nama = input("Masukkan NIM Peminjam yang baru : ")
        print("ID Buku lama :", data[2])
        no = input("Masukkan ID Buku yang baru : ")
        print("Tanggal Peminjaman lama :", data[3])
        telp = input("Masukkan Tanggal Peminjaman yang baru : ")
        print("Tanggal Kembali lama :", data[4])
        telp = input("Masukkan Tanggal Kembali yang baru : ")
        print("Status lama :", data[5])
        telp = input("Masukkan Status yang baru : ")
        perbarui_baris(id, nama, no, telp)
        print("Data telah diperbarui."+'\n')

def hapus_peminjaman():
    id = input("Masukkan ID data yang akan dihapus: ")
    hapus_baris(db_peminjaman,id)
    print("Data telah dihapus."+'\n')
    

def daftar_peminjaman():
    exit()

def tambah_peminjaman_baru():
    exit()

def perbarui_peminjaman():
    exit()

def hapus_peminjamam():
    exit()

def cari_status(id_peminjam):
    # status = ["Tidak Meminjam", "Belum Dikembalikan", "Belum Lunas", "Dikembalikan"]
    
    today = date.today()
    
    # untuk mengurangi repitisi
    def isi_status(status_list, status_str):
        if (status_str not in status_list):
            status_list.append(status_str)
    
    status = []
    meminjam = False
    for i in core.baca_csv(db_peminjaman):
        p_id = i[0]
        p_id_peminjam = i[1]
        id_buku = i[2]
        id_admin = i[3]
        
        tanggal_peminjaman = datetime.strptime(i[4], "%d/%m/%Y")
        tanggal_pengembalian = datetime.strptime(i[5], "%d/%m/%Y")
        p_status = i[6]
        denda_terlambat = i[7]
        # me skip baris kolom / header
        core.dd(i[0])
        
        if i[0] == "id":
            continue
        if id_peminjam == p_id_peminjam:
            meminjam = True
            if ((p_status == "belum dikembalikan") and (today <= tanggal_pengembalian)):
                isi_status(status, "Belum Dikembalikan, ")
            if ((p_status == "belum dikembalikan") and (today > tanggal_pengembalian)):
                isi_status(status, "Telat")
            elif (p_status == "dikembalikan"):
                isi_status(status, "Dikembalikan")
            else:
                isi_status(status, "Error")
                
    if not meminjam:
        isi_status(status, "Tidak Meminjam")
    return status
        
    

while True:
    core.clear()
    
    data_peminjam = core.baca_csv(db_peminjam)

    
    i = 1
    data = [["No.", "Nama", "NIM", "Status", "id"]]
    
    for baris in data_peminjam:
        
        # me skip baris kolom / header
        if baris[0] == "id":
            continue
        status = cari_status(baris[0])
        
        data.append([i, baris[1], baris[2] , status, baris[0]])
        
        i += 1
        
    
    core.dd(data_tampil)
    df = pd.DataFrame(data_peminjam)
    core.dd(df)
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
    