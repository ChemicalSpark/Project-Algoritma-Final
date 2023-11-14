import os
import core
import pandas as pd
from datetime import datetime,date

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'


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
        

# 


while True:
    core.clear()
    
    data_peminjam = core.baca_csv(db_peminjam)

    
    i = 1
    data = [["No.", "Nama", "NIM", "Status", "id"]]
    
    # var untuk ditampilkan
    data_tampil = [["No.", "Nama", "NIM", "Status"]]
    
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
    
    # 
    
    
    with open('ui/data_peminjaman.txt', 'r') as f:
        print(f.read())
    input_user = int(input("Pilih operasi anda (angka) : "))
    

        if ():
            daftar_peminjaman()
        elif ():
            tambah_peminjaman_baru()
        elif ():
            perbarui_peminjaman()
        elif ():
            hapus_peminjamam()
        elif ():
            break
        elif ():
            exit("Program Ditutup")
        elif ():
            print("Input Tidak Valid!")
    # end match


####################
# Area Setelah memlihi peminjam

