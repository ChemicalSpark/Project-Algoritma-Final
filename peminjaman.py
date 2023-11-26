import core
import pandas as pd
from datetime import datetime,date
import data_peminjam as pnjm

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'
db_kategori   = "database/kategori.csv"

limit_per_page = 10

denda_perhari = 1000


def validasi_tanggal(tanggal_string):
    try:
        tanggal_obj = datetime.strptime(tanggal_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def input_tambah_peminjaman(id_buku, id_peminjam):
    
    tanggal_pinjam = date.today().strftime("%d/%m/%Y")
    tanggal_tenggat = ""
    while True: 
        tanggal_tenggat = input("Silahkan Masukan Waktu Tenggat Peminjaman DD/MM/YYYY contoh : 12/08/2034 \n> ")
        if (len(tanggal_tenggat) < 1):
            input("Input Dibatalkan, Tekan untuk kembali...")
            return
        if validasi_tanggal(tanggal_tenggat) == False:
            print("Format tanggal Tidak Valid! mohon coba lagi!")
        else:
            if datetime.today() >= datetime.strptime(tanggal_tenggat,"%d/%m/%Y"):
                print("Tanggal Tidak Valid!, Tanggal yang anda masukan telah tenggat, mohon masukan tanggal diatas hari ini!")
            else:    
                break
        

    daftar_peminjaman_i = core.baca_csv(db_peminjaman)[::-1]

    id_peminjam_baru = 1
    
    if daftar_peminjaman_i[0][0] != "id":
        id_di_db = int(daftar_peminjaman_i[0][0])
        id_peminjam_baru += id_di_db
    
    baris_peminjaman_baru = [id_peminjam_baru,
                            id_peminjam,
                            id_buku,
                            tanggal_pinjam,
                            tanggal_tenggat,
                            "belum dikembalikan",
                            0,
                            "belum"]
    core.tambah_ke_csv(db_peminjaman, baris_peminjaman_baru)
    print("Data Peminjaman Telah Berhasil Ditambahkan")
    
    update_kuantitas_buku(id_buku, "mengurangi")
    input("Tekan Enter untuk kembali menu pilih buku...")


def input_update_peminjaman(id_peminjaman):
    status = cari_status_peminjaman(id_peminjaman)
    daftar_peminjaman_db = core.baca_csv(db_peminjaman)
    data_peminjaman = core.cari_id_list(daftar_peminjaman_db, id_peminjaman)[0]
    id_buku = data_peminjaman[2]
    harga_buku = 
    index_baris = core.cari_index_dengan_id_list(daftar_peminjaman_db, id_peminjaman)
    tgl_tenggat = datetime.strptime(data_peminjaman[4], "%d/%m/%Y")

    today = datetime.today()

    denda = 0

    jumlah_tenggat_hari = today - tgl_tenggat
    jumlah_tenggat_hari = jumlah_tenggat_hari.days
    jumlah_tenggat_hari = (jumlah_tenggat_hari) if jumlah_tenggat_hari > 0 else 0 # Bruh
    
    match (status):
        case "Belum Dikembalikan":
            pilihan = input("Apakah anda ingin mengubah status pengembalian buku (y/n) ? : ").lower()
            if pilihan == "y":
                hilang = input("Apakah buku hilang? (y/n) : ").lower()
                if hilang == "y":
                    # Tandai buku sebagai hilang
                    data_peminjaman[5] = "hilang"
                    data_peminjaman[7] = today.strftime("%d/%m/%Y")
                    core.perbarui_baris_csv(db_peminjaman, index_baris, data_peminjaman)
                    print("Buku Telah Ditandai sebagai Hilang!")
                    print("===================================")
                    print
                    print("Data Peminjaman Telah Diupdate!")
                    
                elif "y" == input("Apakah buku mengalami kerusakan? (y/n) : ").lower():           
                    persen_kerusakan = float(input("Masukkan persentase kerusakan buku (misal 10 untuk 10%): "))
                    denda += (persen_kerusakan / 100) * denda  # Denda dihitung berdasarkan persentase kerusakan
                    data_peminjaman[5] = "dikembalikan"
                    data_peminjaman[7] = today.strftime("%d/%m/%Y")
                    
                else:
                    core.perbarui_baris_csv(db_peminjaman, index_baris, data_peminjaman)
                    print("Data Peminjaman Telah Diupdate!")
                    update_kuantitas_buku(id_buku, "menambah")
                    print("Kuantitas Buku telah Ditambahkan")
                input("Tekan Enter Untuk Kembali...")

        case "Telat":
            denda_perhari = 1000  # Ganti dengan nilai denda per hari yang sesuai
            denda = jumlah_tenggat_hari * denda_perhari

            print("Buku yang dipinjam Telah Tenggat waktu")
            print("Tanggal Tenggat :", data_peminjaman[4])
            print("Jumlah Telat Hari:", jumlah_tenggat_hari)
            print("Denda : ", denda)

            hilang = input("Apakah buku hilang? (y/n) : ").lower()
            if hilang == "y":
                # Tandai buku sebagai hilang
                data_peminjaman[5] = "hilang"
                data_peminjaman[7] = today.strftime("%d/%m/%Y")
                core.perbarui_baris_csv(db_peminjaman, index_baris, data_peminjaman)
                print("Buku Telah Ditandai sebagai Hilang!")
            else:
                # Pengecekan kerusakan buku
                kerusakan = input("Apakah buku mengalami kerusakan? (y/n) : ").lower()
                if kerusakan == "y":
                    persen_kerusakan = float(input("Masukkan persentase kerusakan buku (misal 10 untuk 10%): "))
                    denda += (persen_kerusakan / 100) * denda  # Denda dihitung berdasarkan persentase kerusakan

                data_peminjaman[5] = "dikembalikan"
                data_peminjaman[7] = today.strftime("%d/%m/%Y")
                core.perbarui_baris_csv(db_peminjaman, index_baris, data_peminjaman)
                print("Data Peminjaman Telah Diupdate!")

                if kerusakan == "y":
                    print("Denda akibat kerusakan buku : ", (persen_kerusakan / 100) * denda)

                update_kuantitas_buku(id_buku, "menambah")
                print("Data Kuantitas telah diupdate")
                input("Tekan Enter Untuk Kembali...")

        case "Dikembalikan":
            input("Buku Telah Dikembalikan!\nTekan Enter Untuk Kembali...")

        
    
        
        
def update_kuantitas_buku(id_buku, mode="mengurangi"):
    data_buku_db = core.baca_csv(db_buku)

    buku_d = core.cari_id_list(data_buku_db, id_buku)
    if len(buku_d) < 1:
        print("GAGAL MENGUBAH kuantitas BUKU, data buku yg dicari tidak ada, pastikan id buku ada")
        core.dd(buku_d)
        exit()
    buku_d = buku_d[0]
    jumlah = int(buku_d[6])
    if mode == "mengurangi":
        jumlah -= 1
    else:
        jumlah += 1
    
    buku_d[6] = jumlah
    
    index_baris = core.cari_index_dengan_id_list(data_buku_db, id_buku)
    
    core.perbarui_baris_csv(db_buku, index_baris, buku_d)
    print("Data Kuantitas Buku telah diupdate")


#membuat peminjaman
def tambah_peminjaman(id_peminjam):
    
    search_keyword = ""
    current_page = 1
    total_pages = 1
    
    while True:
        core.clear()
        daftar_buku, total_pages = tampilkan_daftar_buku(search_keyword, current_page, total_pages)
        
        with open('ui/peminjaman/pilih_buku.txt', 'r') as f:
            print(f.read())
            
               
        input_no_aksi = input("| Pilih operasi : ")
        
        match input_no_aksi:
            case '1':
                no_urut_buku = input("| Silahkan Pilih Buku berdasarkan no urut : ")
                if no_urut_buku.isdigit():
                    no_urut_buku = int(no_urut_buku)
                    buku = core.cari_list(daftar_buku[1:], no_urut_buku, 0, True)
                else:
                    continue

                if (len(buku) == 0):
                    input("no buku yang anda pilih Tidak ada\nTekan Enter untuk kembali...")
                else:    
                    pilihan_user = input(f"apakah anda yakin memilih buku no {no_urut_buku} (y/t) :" )

                    if pilihan_user.lower() == 't':
                        break
                    elif pilihan_user.lower() == 'y':
                        input_tambah_peminjaman(buku[0][6], id_peminjam)
                                
                    else:
                        input("input tidak valid!\ntekan enter untuk melanjutkan")
            case '2':
                search_keyword = input("| Masukan Nama buku : ")
                
            case '3':
                if current_page > 1:
                    current_page -= 1
            case '4':
                if current_page < total_pages:
                    current_page += 1
            case '9':
                break
            case '0':
                exit()
            case _ :
                continue
                # input("input tidak valid!\ntekan enter untuk melanjutkan")
    
#menampilkan peminjaman
def tampilkan_daftar_buku_dipinjam(current_page=1, total_pages=1, id_peminjam=0):
    if id_peminjam == 0:
        print("Argumen ke-3 id_peminjam harus diisi")
        return [], 0

    # penambahan huruf f ini menandakan data yg diload dari database

    data_peminjaman_f = core.baca_csv(db_peminjaman)
    data_peminjaman_f = core.cari_list(data_peminjaman_f, id_peminjam, 1)
    buku_f = core.baca_csv(db_buku)
    kategori_f = core.baca_csv(db_kategori)

    peminjaman_tampil = [["No", "Judul", "Kategori", "Tgl Dipinjam", "Tenggat", "Status", "Jumlah Telat Hari", "Denda", "Tgl Dikembalikan"]]
    peminjaman = [["No", "Judul", "Kategori", "Tgl Dipinjam", "Tenggat", "Status", "Jumlah Telat Hari", "Denda", "Tgl Dikembalikan", "id"]]
    i = 1

    for peminjaman_perbaris in data_peminjaman_f:
        buku = core.cari_id_list(buku_f, peminjaman_perbaris[2])
        if not buku:
            print("Data Buku yang dipinjam tidak ada di sistem! Kemungkinan buku telah dihapus dari database!")
            continue

        buku = buku[0]
        kategori = core.cari_id_list(kategori_f, buku[1])

        #parse input str ke datetime objek
        tgl_dipinjam = datetime.strptime(peminjaman_perbaris[3], "%d/%m/%Y")
        tgl_tenggat = datetime.strptime(peminjaman_perbaris[4], "%d/%m/%Y")
        status = cari_status_peminjaman(peminjaman_perbaris[0])

        jumlah_tenggat_hari = (datetime.today() - tgl_tenggat).days
        jumlah_tenggat_hari = jumlah_tenggat_hari if (jumlah_tenggat_hari) > 0 else 0 # bruh
        tanggal_dikembalikan = datetime.strptime(peminjaman_perbaris[7], "%d/%m/%Y").strftime("%d/%b/%Y") if peminjaman_perbaris[7] != "belum" else "belum"

        jumlah_denda = (jumlah_tenggat_hari * denda_perhari) if status == "Telat" else 0

        data_baris =    [i, 
                        buku[2], 
                        kategori[0][1], 
                        tgl_dipinjam.strftime("%d/%b/%Y"), 
                        tgl_tenggat.strftime("%d/%b/%Y"), 
                        status, 
                        f"{jumlah_tenggat_hari} Hari", 
                        jumlah_denda, 
                        tanggal_dikembalikan]
        
        peminjaman_tampil.append(data_baris)
        peminjaman.append(data_baris + [peminjaman_perbaris[0]])
        i += 1

    if len(peminjaman_tampil) <= 1:
        print("* Data Kosong *")
        return [], 0
    
    df = pd.DataFrame(peminjaman_tampil[1:], columns=peminjaman_tampil[0])
    output = df.to_string(index=False)

    hasil = ""
    for i in output.split("\n"):
        hasil += i + "\n"
    
    print(hasil)
    print(" " * 37 + f"page {current_page} of {total_pages}")

    
    return peminjaman, total_pages

#menampilkan daftar buku
def tampilkan_daftar_buku(search_keyword = "", current_page = 1, total_pages = 1):
    
    daftar_buku = core.baca_csv(db_buku)
    
    if len(search_keyword) > 0:
        daftar_buku = core.cari_list(daftar_buku, search_keyword, 2)
        current_page = 1
    
    
    daftar_kategori = core.baca_csv(db_kategori)
    
    data_buku = [["No", "Nama", "Kategori", "Penulis", "Penerbit", "ISBN", "Jumlah" , "id"]]
    data_buku_tampil = data_buku.copy()
    data_buku_tampil[0].pop(7)
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
        jumlah = baris[6]

        data_buku.append([i, nama, nama_kategori, penulis, penerbit, jumlah, baris[0]])
        data_buku_tampil.append([i, nama, nama_kategori, penulis, penerbit, jumlah])
        i += 1



    data_buku_tampil, total_pages = core.pagination(data_buku_tampil[1:], limit_per_page, current_page)
    
    df = pd.DataFrame(data_buku_tampil, columns=["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah"])

    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    
    # Mengganti Output jika data kosong
    if len(data_buku[1:]) < 1:
        output = "* Data Kosong *"
    
    
    hasil = ""
    for i in output.split("\n"):
        hasil += i + "\n"
    
    print(hasil)
    
    print( " "*37 + f"page {current_page} of {total_pages}")
    
    return data_buku, total_pages



def tampilkan_daftar_peminjam_dan_status(search_keyword = "", current_page = 1, total_pages = 1):
    
    data_peminjam = core.baca_csv(db_peminjam)[1:]

    if len(search_keyword) > 0:
        data_peminjam = core.cari_list(data_peminjam, search_keyword, 1)
        current_page = 1

    
    
    i = 1
    data = []
    
    # var untuk ditampilkan
    data_tampil = [["No", "Nama", "NIM", "Status"]]
    
    for baris in data_peminjam:
        if baris[0] == "ID":
            continue # me skip baris kolom / header
        
        status = ""
        for iterasi_status in cari_status(baris[0]):
            status +=  iterasi_status
            
        data.append([i, baris[1], baris[2] , status, baris[0]])
        data_tampil.append([i, baris[1], baris[2] , status])
        
        i += 1
        
    data_tampil, total_pages = core.pagination(data_tampil[1:], limit_per_page, current_page)
    

    # membmode == uat dataframe dan me-set kolom custom
    df = pd.DataFrame(data_tampil, columns=['No.', 'Nama', 'NIM', 'Status'])


    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)

    # Mengganti Output jika data kosong
    if len(data_tampil[1:]) < 1:
        output = "* Data Kosong *"
    
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*10 + i + "\n"
    
    print(hasil)
    print( " "*37 + f"page {current_page} of {total_pages}")
    return data, current_page, total_pages
    


def update_peminjaman(id_peminjam):  
    pilih_peminjaman(id_peminjam, "update")

 
def hapus_peminjaman(id_peminjam):
    pilih_peminjaman(id_peminjam, "hapus")



def pilih_peminjaman(id_peminjam, mode = ""):
    search_keyword = ""
    current_page = 1
    total_pages = 1
    while True:
        core.clear()
        buku_buku_yg_dipindam, total_pages = tampilkan_daftar_buku_dipinjam(current_page, total_pages, id_peminjam)
        
        if len(buku_buku_yg_dipindam[1:]) < 1:
            input("Peminjan ini belum meminjam buku apapun!\nTekan Enter Untuk Kembali...")
            return
        
        with open(f'ui/peminjaman/aksi_{mode}.txt', 'r') as f:
            print(f.read())
            
               
        input_user = input("| Pilih operasi: ")
        
        match input_user:
            case '1':
                input_no_buku = input("| Silahkan Pilih Buku berdasarkan no urut : ")
                if input_no_buku:
                    input_no_buku = int(input_no_buku)
                    peminjaman = core.cari_list(buku_buku_yg_dipindam[1:], input_no_buku, 0, True)
                else:
                    continue
                if (len(peminjaman) == 0):
                    input("no peminjaman yang anda pilih Tidak ada\nTekan Enter untuk kembali")
                else:    
                    peminjaman = peminjaman[0]
                    id_peminjaman = peminjaman[9]

                    if mode == "hapus":
                        input_hapus_peminjaman(id_peminjaman)
                    elif mode == "update":
                        input_update_peminjaman(id_peminjaman)  

            case '2':
                if current_page > 1:
                    current_page -= 1
            case '3':
                if current_page < total_pages:
                    current_page += 1
            case '9':
                break
            case '0':
                exit()
            case _ :
                continue

def input_hapus_peminjaman(id_peminjaman):
    while True:
        pilihan = input("| Apakah anda yakin ingin Menghapus data Peminjaman ini (y/n)? \n> ").lower()
        if pilihan.lower() == "y":
            data_db_peminjaman = core.baca_csv(db_peminjaman)
            data_peminjaman = core.cari_id_list(data_db_peminjaman, id_peminjaman)[0]
            index_baris = core.cari_index_dengan_id_list(data_db_peminjaman, id_peminjaman)
            core.hapus_baris_csv(db_peminjaman, index_baris)
            
            update_kuantitas_buku(data_peminjaman[2], "menambahkan")
            input("Data Peminjaman Telah Dihapus!\nTekan Enter Untuk Kembali...")
            break
            
        elif pilihan.lower() == "n":
            break
        else:
            continue
            # print("Input tidak valid, hanya menerima 'y' atau 'n' saja!")
        

def cari_status(id_peminjam):
    today = date.today()
    status = []
    
    # menginisialisasi status peminjam awal
    meminjam = False

    for i in core.baca_csv(db_peminjaman):
        # me-skip baris kolom/header
        if i[0] == "id":
            continue

        id_peminjaman = i[0]
        p_id_peminjam = i[1]
        
        # jika ada data
        if id_peminjam == p_id_peminjam:
            meminjam = True  # menunjukan jika peminjam ada data peminjaman

            status.append(cari_status_peminjaman(id_peminjaman))

    if not meminjam:
        status.append("Tidak Meminjam")

    # core.dd(status)
    status = list(dict.fromkeys(status)) # hapus duplikasi

    
    return ", ".join(status)


def cari_status_peminjaman(id_peminjaman):
    today = date.today()
    
    data_db_peminjaman = core.baca_csv(db_peminjaman)
    
    data_peminjaman = core.cari_id_list(data_db_peminjaman, id_peminjaman)[0]
    
    tanggal_peminjaman = data_peminjaman[3]
    tanggal_tenggat = data_peminjaman[4]
    status = data_peminjaman[5]
    
    if status == "belum dikembalikan":
        if today > datetime.strptime(tanggal_tenggat, "%d/%m/%Y").date():
            return "Telat"
        else:
            return "Belum Dikembalikan"
    elif status == "dikembalikan":
        return "Dikembalikan"
    elif status == "rusak":
        return "Rusak"
    elif status == "hilang":
        return "Hilang"
    else:
        print("Pengecualian Terdeteksi hasil diluar perkiraan!\nSTATUS di DB : " , status , "\nTanggal Dipinjam : " , tanggal_peminjaman.strftime("%d %B %Y") , "\nTanggal Hari ini : " , date.today().strftime("%d %B %Y") ,"\nTanggal Deadline : " , tanggal_tenggat.strftime("%d %B %Y"))
        exit()



          
def aksi_peminjaman(mode = "tambah"):  

    search_keyword = ""
    current_page = 1
    total_pages = 1

    while True:
        core.clear()
        daftar_peminjam, current_page, total_pages = tampilkan_daftar_peminjam_dan_status(search_keyword, current_page, total_pages)
        
        # mengganti huruf pertama denga kapital
        print("Mode :", mode.capitalize() , "Peminjaman ")
        if (mode == "tambah"):
            print( " "*3 , "[ Silahkan Pilih Peminjam sebelum manambah peminjaman atau pilih buat peminjam baru ]")

        with open('ui/peminjaman/aksi_peminjaman.txt', 'r') as f:
            print(f.read())
        input_user = input("Pilih operasi anda: ")

        if (input_user == '1'):
            
            no_urut = input("Silahkan pilih menggunakan no urut : ")
            if no_urut:
                no_urut = int(no_urut)
                peminjam = core.cari_list(daftar_peminjam, no_urut, 0, True)[0]
            else:
                aksi_peminjaman(mode = "tambah")

            if len(peminjam) < 1:
                input("Data peminjam yang anda pilih tidak ada\nTekan Enter untuk melanjutkan")
            else: 
                id_peminjam = peminjam[4]

            if (mode == "tambah"):
                tambah_peminjaman(id_peminjam)
            elif (mode =="hapus"):
                hapus_peminjaman(id_peminjam)
            elif (mode == "update"):
                update_peminjaman(id_peminjam)
            else:
                "Input tidak valid"  
        elif (input_user ==  '2'):
            search_keyword = input("Masukan Nama : ")
            if search_keyword:
                continue
            else:
                aksi_peminjaman(mode = "tambah")
        elif (input_user ==  '3'):
            pnjm.aksi_peminjam()
        elif (input_user ==  '4') and current_page > 1:
            current_page -= 1
        elif (input_user ==  '5') and current_page < total_pages:
            current_page += 1
        elif (input_user ==  '9'):
            break
        elif (input_user ==  '0'):
            exit()
        else:
            continue

# merupakan fungsi yang akan dijalankan pertama kali
def aksi_utama():

    while True:
        core.clear()
        # with open('ui/catalibra.txt', 'r') as f:
        #     print(f.read())
        with open('ui/peminjaman/aksi_utama.txt', 'r') as f:
            print(f.read())
        
        input_user = input("| > Pilih: ")
        
        match input_user:
            case '1':
                aksi_peminjaman("tambah")
            case '2':
                aksi_peminjaman("update")
            case '3':
                aksi_peminjaman("hapus")
            case '9':
                break
            case '0':
                exit()
            case _: 
                continue

    
####################
# Area Setelah memlihi peminjam


if __name__ == "__main__":
    aksi_utama()

