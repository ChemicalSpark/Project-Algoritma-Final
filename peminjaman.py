import os
import core
import pandas as pd
from datetime import datetime,date
import data_peminjam as peminjam

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'


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
    

# UNTUK BAGIAN NAMBAH PEMINJAMAN 

def pilih_peminjam(id_peminjam):
        
    data_peminjam = core.cari_list(core.baca_csv(db_peminjam), id_peminjam, 0)
    search_keyword = ""
    current_page = 1
    total_pages = 1

    while True:
        daftar_buku = core.baca_csv(db_buku)
        
        data_buku = [["No", ""]]

    exit()


###########
# UNTUK MENGELOLA PEMINJAM

def kelola_peminjam():
    peminjam = core.baca_csv(db_peminjam)
    daftar_peminjaman = core.cari_list(core.baca_csv(db_peminjaman), id_peminjam, 0)
    
    # Mengonversi data menjadi DataFrames
    df_peminjam = pd.DataFrame(data_peminjam, columns=['id', 'Nama', 'NIM', 'Status', 'Status Lunas', 'Jumlah Dikembalikan'])
    df_peminjaman = pd.DataFrame(data_peminjaman, columns=['No.', 'Judul', 'Kategori', 'Tgl Dipinjam', 'Deadline', 'Status', 'Telat Hari', 'Denda'])
        
    print("Identitas Peminjam")
    print("+-------------------------------------------------------------+")
    print(f"| Nama\t\t: {peminjam_terpilih['Nama'].values[0]}\t\t\t  |")
    print(f"| NIM\t\t: {peminjam_terpilih['NIM'].values[0]}\t\t\t  |")
    print(f"| Status\t: {peminjam_terpilih['Status'].values[0]} | {peminjam_terpilih['Status Lunas'].values[0]}\t\t  |")
    print(f"| Jumlah\t: {peminjam_terpilih['Jumlah Dikembalikan'].values[0]}\t\t\t  |")
    print("+-------------------------------------------------------------+")
    
    print("\nDaftar Peminjaman", peminjam_terpilih['Nama'].values[0])
    print(df_peminjaman.to_string(index=False))
        
        
        

    # Contoh penggunaan
    id_peminjam_yang_ditampilkan = '1'  # Ganti ini dengan ID yang diinginkan
    tampilkan_peminjam_dan_peminjaman(df_peminjam, df_peminjaman, id_peminjam_yang_ditampilkan)

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
        
        # jika ada data 
        if id_peminjam == p_id_peminjam:
            meminjam = True # menunjukan jika peminjam ada data peminjaman
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
          
          
def aksi_utama():  
    search_keyword = ""

    current_page = 1

    total_pages = 1

    while True:
        core.clear()
        
        data_peminjam = core.baca_csv(db_peminjam)

        if len(search_keyword) > 0:
            data_peminjam = core.cari_list(data_peminjam, search_keyword, 1)
            current_page = 1

        data_peminjam, total_pages = core.pagination(data_peminjam, 7, current_page)
        
        
        i = 1
        data = []
        
        # var untuk ditampilkan
        data_tampil = [["No", "Nama", "NIM", "Status"]]
        
        for baris in data_peminjam:
            if baris[0] == "id":
                continue # me skip baris kolom / header
            
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
        
        with open('ui/data_peminjaman.txt', 'r') as f:
            print(f.read())
        input_user = int(input("Pilih operasi anda (angka) : "))

        if (input_user == 1):
            no_urut = int(input("Silahkan pilih peminjam menggunakan no urut dari tabel diatas : "))
            id_peminjam = core.cari_list(data, no_urut, 0, True)[0][4]
            pilih_peminjam(id_peminjam)
        elif (input_user ==  2):
            search_keyword = input("Masukan Nama : ")
        elif (input_user ==  3):
            tambah_peminjam()
        elif (input_user ==  4):
            if current_page > 1:
                current_page -= 1
        elif (input_user ==  5):
            if current_page < total_pages:
                current_page += 1
        elif (input_user ==  6):
            exit("Program Ditutup")
        else:
            print("Input Tidak Valid!")


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
