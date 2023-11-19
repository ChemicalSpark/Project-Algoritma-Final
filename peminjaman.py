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

denda_perhari = 30000

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

def validasi_tanggal(tanggal_string):
    try:
        tanggal_obj = datetime.strptime(tanggal_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def input_peminjaman(id_buku, id_peminjam):
    
    tanggal_pinjam = date.today().strftime("%d/%m/%Y")
    tanggal_tenggat = ""
    while True: 
        tanggal_tenggat = input("Silahkan Masukan Waktu Tenggat Peminjaman DD/MM/YYYY contoh : 12/08/2034 \n> ")
        if validasi_tanggal(tanggal_tenggat) == False:
            print("Format tanggal Tidak Valid! mohon coba lagi!")
        else:
            break

    daftar_peminjaman_i = core.baca_csv(db_peminjaman)[::-1]

    id_peminjam_baru = 1
    
    if daftar_peminjaman_i[0][0] != "id":
        id_di_db = int(daftar_peminjaman_i[0][0])
        id_peminjam_baru += id_di_db
    
    baris_data_baru = [id_peminjam_baru,
                       id_peminjam,
                       id_buku,
                       tanggal_pinjam,
                       tanggal_tenggat,
                       "belum dikembalikan",
                       0]
    
    update_kuantitas_buku(id_buku, "mengurangi")
    input("Tekan Enter untuk kembali menu pilih buku...")
    
        
def update_kuantitas_buku(id_buku, mode="mengurangi"):
    data_buku_db = core.baca_csv(db_buku)
    core.tambah_ke_csv(db_peminjaman, baris_data_baru)
    print("Data Peminjaman Telah Berhasil Ditambahkan")
    buku_d = core.cari_id_list(data_buku_db, id_buku)[0]
    jumlah = int(buku_d[6])
    if mode == "mengurangi":
        jumlah -= 1
    else:
        jumlah += 1
    
    buku_d[6] = jumlah
    
    index_baris = core.cari_index_dengan_id_list(data_buku_db, id_buku)
    
    core.perbarui_baris_csv(db_buku, index_baris, buku_d)
    print("Data Kuantitas Buku telah diupdate")

def tambah_peminjaman(id_peminjam):
    
    search_keyword = ""
    current_page = 1
    total_pages = 1
    
    while True:
        core.clear()
        daftar_buku = tampilkan_daftar_buku(search_keyword, current_page, total_pages)
        with open('ui/peminjaman/pilih_buku.txt', 'r') as f:
            print(f.read())
            
               
        input_user_x = int(input("Pilih operasi (angka) : "))
        
        buku = core.cari_list(daftar_buku[1:], input_user_x, 0, True)
        match input_user_x:
            case 1:

                if (len(buku) == 0):
                    print("no buku yang anda pilih Tidak ada")
                else:    
                    pilihan_user = input(f"apakah anda yakin memilih buku no {input_user_x} (y/t) :" )

                    if pilihan_user.lower() == 't':
                        break
                    elif pilihan_user.lower() == 'y':
                        sekali = True
                        input_peminjaman(buku[0][6], id_peminjam)
                                
                    else:
                        input("input tidak valid!\ntekan enter untuk melanjutkan")
            case 2:
                search_keyword = input("Masukan Nama buku : ")
            case 3:
                if current_page > 1:
                    current_page -= 1
            case 4:
                if current_page < total_pages:
                    current_page += 1
            case 5:
                break
            case 0:
                exit()
            case _ :
                input("input tidak valid!\ntekan enter untuk melanjutkan")
    

def tampilkan_daftar_buku_dipinjam(current_page = 1, total_pages = 1, id_peminjam = None):
    
    data_peminjaman_f = core.baca_csv(db_peminjaman)
    
    data_peminjaman_f = core.cari_list(data_peminjaman_f, id_peminjam, 1)
    
    
    buku_f = core.baca_csv(db_buku)
    
    kategori_f = core.baca_csv(db_kategori)
    
    peminjaman_tampil = [["No", "Judul", "Kategori", "Tgl Dipinjam", "Tenggat", "Status", "Jumlah Telat Hari", "Denda"]]
    peminjaman = peminjaman_tampil
    peminjaman.append("id")
    i = 1
    for peminjaman_perbaris in data_peminjaman_f:
        # cari buku yg dimpinjam
        buku = core.cari_id_list(buku_f, peminjaman_perbaris[2])
        if len(buku) < 1:
            print("Data Buku yang dipinjam tidak ada disistem!, ini bisa di sebabkan dihapusnya buku di database!")
            continue
        #cari kategori buku yng dipinjam
        buku = buku[0]
        kategori = core.cari_id_list(kategori_f, buku[1])
        
        #parse input str ke datetime objek
        tgl_dipinjam = datetime.strptime(peminjaman_perbaris[3], "%d/%m/%Y")
        tgl_tenggat = datetime.strptime(peminjaman_perbaris[4], "%d/%m/%Y")

        status_f = "BELUM DIEMPLEMENTASI"

        jumlah_tenggat_hari = datetime.today() - tgl_tenggat
        jumlah_tenggat_hari = jumlah_tenggat_hari.days
        
        # data 
        d = [i, # no
            buku[2], # judul 
            kategori[1], # kategori
            tgl_dipinjam.strftime("%d %M %Y"),
            tgl_tenggat.strftime("%d %M %Y"),
            status_f,
            jumlah_tenggat_hari,
            jumlah_tenggat_hari * denda_perhari
            ]
        
        peminjaman.append(d)
        f = d
        peminjaman_tampil.append(f.append(peminjaman_perbaris[0]))
        
        i += 1
        
    df = pd.DataFrame(peminjaman_tampil[1:], columns=peminjaman_tampil[0])

    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*10 + i + "\n"
    
    print(hasil)
    
    print( " "*37 + f"page {current_page} of {total_pages}")
    
    return peminjaman, total_pages
    
    
    
def hapus_peminjaman(id_peminjam):
    search_keyword = ""
    current_page = 1
    total_pages = 1
    while True:
        buku_buku_yg_dipindam, total_pages = tampilkan_daftar_buku_dipinjam(current_page, total_pages, id_peminjam)
        with open('ui/peminjaman/aksi_hapus.txt', 'r') as f:
            print(f.read())
            
               
        input_user_x = int(input("Pilih operasi (angka) : "))
        
        buku = core.cari_list(buku_buku_yg_dipindam[1:], input_user_x, 0, True)
        match input_user_x:
            case 1:

                if (len(buku) == 0):
                    print("no peminjaman yang anda pilih Tidak ada")
                else:    
                    pilihan_user = input(f"apakah anda yakin memilih buku no {input_user_x} (y/t) :" )

                    if pilihan_user.lower() == 't':
                        break
                    elif pilihan_user.lower() == 'y':
                        sekali = True
                        input_peminjaman(buku[0][6], id_peminjam)
                                
                    else:
                        input("input tidak valid!\ntekan enter untuk melanjutkan")
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
        

def input_hapus_peminjaman(id_peminjaman):
    while True:
        pilihan = input("Apakah anda yakin ingin Menghapus data Peminjaman ini?, aksi ini tidak dapat dibatalkan! (y/n) \n> ").lower()
        kuantitas = True
        if pilihan == "y":
            while True:
                pilihan = input("Apakah anda juga ingin menambahkan data kuantitas (jumlah) buku yang tersimpan disistem? (y/n) \n> ").lower()
                if pilihan == "y":
                    kuantitas = True
                    break
                elif pilihan == "n":
                    kuantitas = False
                    break
                else:
                    print("Input tidak valid, hanya menerima 'y' atau 'n' saja!")
                        
            data_db_peminjaman = core.baca_csv(db_peminjaman)
            data_peminjaman = core.cari_id_list(data_db_peminjaman, id_peminjaman)[0]
            index_baris = core.cari_index_dengan_id_list(data_db_peminjaman, id_peminjaman)
            core.hapus_baris_csv(db_peminjaman, index_baris)
            if kuantitas:
                update_kuantitas_buku(data_peminjaman[2], "menambahkan")
                input("Data Telah Dihapus Tekan Enter Untuk Kembali...")
                break
            
        elif pilihan == "n":
            break
        else:
            print("Input tidak valid, hanya menerima 'y' atau 'n' saja!")
        


def tampilkan_daftar_buku(search_keyword = "", current_page = 1, total_pages = 1):

    daftar_buku = core.baca_csv(db_buku)
    
    if len(search_keyword) > 0:
        daftar_buku = core.cari_list(daftar_buku, search_keyword, 2)
        current_page = 1

    daftar_buku, total_pages = core.pagination(daftar_buku, limit_per_page, current_page)
    
    daftar_kategori = core.baca_csv(db_kategori)
        
    data_buku = [["No", "Nama", "Kategori", "Penulis", "Penerbit", "ISBN", "Jumlah" , "id"]]
    
    i = 1
    for baris in daftar_buku:
        # me skip baris kolom / header
        if baris[0] == "id":
            continue
        
        nama_kategori = ""
        
        nama = baris[2]
        
        kategori = core.cari_id_list(daftar_kategori, baris[1])
        if (len(kategori) > 0):
            nama_kategori = kategori[0][1]
            
        penulis = baris[3]
        penerbit = baris[4]
        isbn = baris[5]
        jumlah = baris[6]
        
        data_buku.append([i, nama, nama_kategori, penulis, penerbit, jumlah])
        i += 1



    df = pd.DataFrame(data_buku[1:], columns=["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah"])

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

def kelola_peminjam(id_peminjam):
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
    today = date.today()
    status = []

    def isi_status(status_list, status_str):
        if status_str not in status_list:
            status_list.append(status_str)
        return status_list

    # menginisialisasi status peminjam awal
    meminjam = False

    for i in core.baca_csv(db_peminjaman):
        # me-skip baris kolom/header
        if i[0] == "id":
            continue

        p_id, p_id_peminjam, _, tanggal_peminjaman, tanggal_pengembalian, p_status, _ = i[:7]

        # jika ada data
        if id_peminjam == p_id_peminjam:
            meminjam = True  # menunjukan jika peminjam ada data peminjaman

            if p_status == "belum dikembalikan":
                if today <= datetime.strptime(tanggal_pengembalian, "%d/%m/%Y").date():
                    status.append("Belum Dikembalikan")
                else:
                    status.append("Telat")
            elif p_status == "dikembalikan":
                status.append("Dikembalikan")
            else:
                raise Exception(f"Pengecualian Terdeteksi hasil diluar perkiraan!\nSTATUS di DB : {p_status}\nTanggal Dipinjam : {tanggal_peminjaman.strftime("%d %B %Y")}\nTanggal Hari ini : {date.today().strftime("%d %B %Y")}\nTanggal Deadline : {tanggal_pengembalian.strftime("%d %B %Y")}")
    if not meminjam:
        status.append("Tidak Meminjam")

    # core.dd(status)
    status = list(dict.fromkeys(status)) # hapus duplikasi

    
    return ", ".join(status)


def tampilkan_daftar_peminjam_dan_status(search_keyword = "", current_page = 1, total_pages = 1):
    core.clear()
    data_peminjam = core.baca_csv(db_peminjam)[1:]

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
        if (mode == "tambah"):
            print(f"{ " "*3 }[ Silahkan Pilih Peminjam sebelum manambah peminjaman atau pilih buat peminjam baru ]")

        with open('ui/peminjaman/aksi_peminjaman.txt', 'r') as f:
            print(f.read())
        input_user = int(input("Pilih operasi anda (angka) : "))

        if (input_user == 1):
            no_urut = int(input("Silahkan pilih menggunakan no urut : "))
            id_peminjam = core.cari_list(daftar_peminjam, no_urut, 0, True)[0][4]
            
            if (mode == "kelola"):
                kelola_peminjam()
            elif (mode == "tambah"):
                tambah_peminjaman(id_peminjam)
            elif (mode =="hapus"):
                hapus_peminjaman(id_peminjam)
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
        core.clear()
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

# aksi_utama()    

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
