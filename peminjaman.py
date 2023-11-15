import os
import core
import pandas as pd
from datetime import datetime,date
import data_peminjam as peminjam

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'

def pilih_peminjam(id_peminjam):
    peminjam = core.baca_csv(db_peminjam)
    
    daftar_peminjaman = core.cari_list(core.baca_csv(db_peminjaman), id_peminjam)
    
    print(peminjam)
    print(daftar_peminjaman)

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
        
        
        # me skip baris kolom / header
        if i[0] == "id":
            continue
        
        
        p_id = i[0]
        p_id_peminjam = i[1]
        id_buku = i[2]
        id_admin = i[3]
        
        tanggal_peminjaman = datetime.strptime(i[4], "%d/%m/%Y")
        tanggal_pengembalian = datetime.strptime(i[5], "%d/%m/%Y")
        p_status = i[6]
        denda_terlambat = i[7]
        

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
        
search_keyword = ""

current_page = 1

total_pages = 1

while True:
    core.clear()
    
    data_peminjam = core.baca_csv(db_peminjam)

    if len(search_keyword) > 0:
        data_peminjam = core.cari_list(data_peminjam, search_keyword, 1)
        current_page = 1

    data_peminjam, total_pages = core.pagination(data_peminjam, 10, 1)
    
    
    i = 1
    data = [["No", "Nama", "NIM", "Status", "id"]]
    
    # var untuk ditampilkan
    data_tampil = [["No", "Nama", "NIM", "Status"]]
    
    for baris in data_peminjam:
        
        # me skip baris kolom / header
        if baris[0] == "id":
            continue
        
        status = ""
        for iterasi_status in cari_status(baris[0]):
            status +=  iterasi_status
            
        data.append([i, baris[1], baris[2] , status, baris[0]])
        
        data_tampil.append([i, baris[1], baris[2] , status])
        
        i += 1
        
    
    
    # membuat dataframe dan me-set kolom custom
    df = pd.DataFrame(data_tampil[1:], columns=['No.', 'Nama', 'NIM', 'Status'])


    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*23 + i + "\n"
    
    print(hasil)
    
    print( " "*37 + f"page {current_page} of {total_pages}")
    # 
    
    
    with open('ui/data_peminjaman.txt', 'r') as f:
        print(f.read())
    input_user = int(input("Pilih operasi anda (angka) : "))
    
    
# [1] Pilih Peminjam                                \| 
# [2] Cari Peminjam                                  |
# [3] Tambah Peminjam (konsol)                       |
# [4] Pindah Halaman Ke kiri                         |
# [5] Pindah Halaman Ke kanan                        |
# [6] Kembali                                        |
# [0] Keluar 

    if (input_user == 1):
        no_urut = int(input("Silahkan pilih peminjam menggunakan no urut dari tabel diatas : "))
        id_peminjam = core.cari_list(data, no_urut, 0, True)[0][4]
        pilih_peminjam(id_peminjam)
    elif (input_user ==  2):
        search_keyword = input("Masukan Nama : ")
    elif (input_user ==  3):
        tambah_peminjam()
    elif (input_user ==  4):
        if current_page > total_pages:
            current_page -= 1
    elif (input_user ==  5):
        if current_page < total_pages:
            current_page += 1
    elif (input_user ==  6):
        exit("Program Ditutup")
    else:
        print("Input Tidak Valid!")
    # end match

def tambah_peminjam():
    nama = input("Masukkan Nama: ")
    no = input("Masukkan NIM: ")
    telp = input("Masukkan Nomor Telepon: ")
    id_peminjam_baru = peminjam.tambah_baris_peminjam(nama, no, telp)
    print("Data telah ditambahkan."+'\n')
    while True:
        pilihan = input("Apakah anda ingin langsung memilih Peminjam ini (y/n) ? : ").lower()
        if pilihan == "y":
            pilih_peminjam(id_peminjam_baru)
        elif pilihan == "n":
            search_keyword = ""
            break
        else:
            print("Input tidak valid, hanya menerima 'y' atau 'n' saja!")
            
####################
# Area Setelah memlihi peminjam
    

if __name__ == "__main__":
    aksi_peminjaman()
    baca_baris()
    hapus_baris()
    perbarui_baris()
    tambah_peminjaman()
    tampilkan_peminjaman()
    perbarui_peminjaman()
    hapus_peminjaman()
