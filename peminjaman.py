import os
import core
import pandas as pd
from datetime import datetime,date
import data_peminjam as peminjam

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'
db_kategori   = "database/kategori.csv"

limit_per_page = 7

# UNTUK BAGIAN JALUR NAMBAH PEMINJAMAN SETELAH

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

def input_peminjaman(id_buku, id_peminjam):
    exit()



def tambah_peminjaman(id_peminjam):
    
    search_keyword = ""
    current_page = 1
    total_pages = 1
    
    kembali = False
    
    while True:
        core.clear()
        daftar_buku = tampilkan_daftar_buku(search_keyword, current_page, total_pages)
        with open('ui/peminjaman/pilih_buku.txt', 'r') as f:
            print(f.read())
            
        while True:        
            input_user = int(input("Pilih operasi (angka) : "))
            
            buku = core.cari_list(daftar_buku, input_user, 0)
            
            match input_user:
                case 1:
                    if (len(buku) == 0):
                        print("no buku yang anda pilih Tidak ada")
                    else:    
                        pilihan_user = input(f"apakah anda yakin memilih buku no {input_user} (y/t) :" )
                        
                        if pilihan_user.lower() != 'y':
                            break
                        else:
                            core.dd(buku)
                            # input_peminjaman(buku[3], )
                    
                case 2:
                    if current_page > 1:
                        current_page -= 1
                case 3:
                    if current_page < total_pages:
                        current_page += 1
                case 4:
                    break
                case 0:
                    exit()
                case _ :
                    input("input tidak valid!\ntekan enter untuk melanjutkan")
                    
        if kembali:
            break        
    


def tampilkan_daftar_buku(search_keyword = "", current_page = 1, total_pages = 1):

    daftar_buku = core.baca_csv(db_buku)
    
    if len(search_keyword) > 0:
        daftar_buku = core.cari_list(daftar_buku, search_keyword, 2, True)
        current_page = 1

    daftar_buku, total_pages = core.pagination(daftar_buku, limit_per_page, current_page)
    
    daftar_kategori = core.baca_csv(db_kategori)
        
    data_buku = [["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah", "id"]]
    
    i = 1
    for baris in daftar_buku:
        
        nama = baris[2]
        nama_kategori = core.cari_id_list(daftar_kategori, baris[1])
        penulis = baris[3]
        penerbit = baris[4]
        jumlah = baris[5]
        
        data_buku.append([i, nama, nama_kategori, penulis, penerbit, jumlah])
        i += 1



    df = pd.DataFrame(data_buku[1:8], columns=["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah"])

    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*10 + i + "\n"
    
    print(hasil)
    
    print( " "*37 + f"page {current_page} of {total_pages}")
    
    return data_buku


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



def tampilkan_daftar_peminjam_dan_status(search_keyword = "", current_page = 1, total_pages = 1):
    core.clear()
    data_peminjam = core.baca_csv(db_peminjam)

    if len(search_keyword) > 0:
        data_peminjam = core.cari_list(data_peminjam, search_keyword, 1)
        current_page = 1

    data_peminjam, total_pages = core.pagination(data_peminjam, limit_per_page, current_page)
    
    
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
        
    
    
    # membmode == uat dataframe dan me-set kolom custom
    df = pd.DataFrame(data_tampil[1:], columns=['No.', 'Nama', 'NIM', 'Status'])


    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*23 + i + "\n"
    
    print(hasil)
    
    print( " "*37 + f"page {current_page} of {total_pages}")
    
    return data, current_page, total_pages
    
          
def aksi_peminjaman(mode = "kelola"):  

    search_keyword = ""
    current_page = 1
    total_pages = 1

    while True:
        daftar_peminjam, current_page, total_pages = tampilkan_daftar_peminjam_dan_status(search_keyword, current_page, total_pages)
        
        with open('ui/peminjaman/aksi_peminjaman.txt', 'r') as f:
            print(f.read())
        input_user = int(input("Pilih operasi anda (angka) : "))

        if (input_user == 1):
            no_urut = int(input("Silahkan pilih peminjam menggunakan no urut dari tabel diatas : "))
            id_peminjam = core.cari_list(daftar_peminjam, no_urut, 0, True)[0][4]
            
            if (mode == "kelola"):
                kelola_peminjam()
            elif (mode == "tambah"):
                tambah_peminjaman(id_peminjam)
            # elif (mode =="hapus"):
                
            # elif (mode == "update"):
            
            
            
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
            break
        elif (input_user ==  7):
            exit("Program Ditutup")
        else:
            input("input tidak valid!\ntekan enter untuk melanjutkan")

# merupakan fungsi yang akan dijalankan pertama kali
def aksi_utama():

    while True:
        with open('ui/catalibra.txt', 'r') as f:
            print(f.read())
        with open('ui/peminjaman/aksi_utama.txt', 'r') as f:
            print(f.read())
        
        input_user = int(input("| > Pilih: "))
        
        match input_user:
            case 1:
                aksi_peminjaman("tambah")
            case 2:
                aksi_peminjaman("update")
            case 3:
                aksi_peminjaman("hapus")
            case 4:
                aksi_peminjaman("kelola")
            case 5:
                break
            case 0:
                exit()
            case _ : 
                input("input tidak valid!\ntekan enter untuk melanjutkan")

    
####################
# Area Setelah memlihi peminjam
    

if __name__ == "__main__":
    aksi_utama()
    aksi_peminjaman()
    baca_baris()
    hapus_baris()
    perbarui_baris()
    tambah_peminjaman()
    tampilkan_peminjaman()
    perbarui_peminjaman()
    hapus_peminjaman()
