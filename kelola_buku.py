import csv
import core
import pandas  as pd

db_buku = 'database/buku.csv'
db_kategori   = "database/kategori.csv"
ui_bk = "ui/kelola_buku.txt"

def list_buku():
    '''fungsi read data buku'''
    with open(db_buku, mode='r') as list_data:
        baca_buku = list(csv.reader(list_data))
        return baca_buku
    
def dtframe_buku(cari_keyword='',halaman_sekarang=1,halaman_total=1):
    '''fungsi menampilkan data frame buku'''
    
    daftar_buku = core.baca_csv(db_buku)[1:]
    daftar_kategori = core.baca_csv(db_kategori)[1:]

    halaman_limit = 10
    data_buku = [["No", "Judul", "Kategori", "Penulis", "Penerbit", "ISBN", "Jumlah" , "id"]]

    if len(cari_keyword) > 1:
        daftar_buku = core.cari_list(daftar_buku,cari_keyword,1)
        halaman_sekarang = 1

    i = 1
    for baris in daftar_buku:
        nama_kategori = ""
        judul = baris[2]
        kategori = core.cari_id_list(daftar_kategori, baris[1])
        if (len(kategori) > 0):
            nama_kategori = kategori[0][1]
            
        penulis = baris[3]
        penerbit = baris[4]
        jumlah = baris[6]
        harga = baris[7]
        
        data_buku.append([i, judul.title(), nama_kategori.title(), penulis.title(), penerbit.title(), jumlah, harga])
        i += 1
    # membuat data frame dengan data buku dimulai dari index (me skip header)
    data_buku,halaman_total = core.pagination(data_buku[1:],halaman_limit,halaman_sekarang)

    # untuk mengabaikan index bawaan pandas
    if len(data_buku[1:]) <= 1:
        output = "* Data Kosong *"
    elif "" in daftar_buku[len(daftar_buku) - 1]:
        df = pd.DataFrame(data_buku[:len(data_buku) - 1], columns=["No", "Judul", "Kategori", "Penulis", "Penerbit", "Jumlah", "Harga"])
        output = df.to_string(index=False)
    else:
        df = pd.DataFrame(data_buku, columns=["No", "Judul", "Kategori", "Penulis", "Penerbit", "Jumlah", "Harga"])
        output = df.to_string(index=False)

    hasil = ""
    for i in output.split("\n"):
        hasil += i + "\n" 
    print(hasil)

    print(" "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_buku,halaman_sekarang,halaman_total
    

def kategori_buku():
    '''fungsi menampilakn kategori buku'''
    with open(db_kategori, mode='r') as kategori:
        list_kategori = list(csv.reader(kategori))
        tampil_kategori = ''
        for i in list_kategori:
            if i[0] == 'ID':
                continue
            tampil_kategori += f'[{i[0]}] {i[1]} '
        return tampil_kategori, list_kategori

def tambah_buku():
    '''fungsi tambah buku'''
    data_buku = core.baca_csv(db_buku)
    display_kategori, list_kategori = kategori_buku()
    print('| Pilihan kategori :')
    print(display_kategori)
    input_kategori = input('\n| Pilih kategori buku\t: ')
    input_judul = input('| Masukkan judul\t: ').lower()
    input_penulis = input('| Masukkan penulis\t: ').lower()
    input_penerbit = input('| Masukkan penerbit\t: ').lower()
    input_isbn = input('| Masukkan ISBN\t\t: ')
    input_jumlah = input('| Masukkan jumlah buku\t: ')
    input_harga = input('| Masukkan harga buku\t: ')
    
    if input_kategori and input_judul and input_penulis and input_penerbit and input_isbn and input_jumlah:
        input_kategori = int(input_kategori)
        input_jumlah = int(input_jumlah)
      
    else:
        print('+' + '='*60 + '+')
        print('|' + '[ DATA TIDAK LENGKAP ]'.center(60) + '|')
        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
        print('+' + '='*60 + '+')
        enter  = input()
        return False

    for i in data_buku[1:]:
        if i[2] == input_judul:
            print('+' + '='*60 + '+')
            print('|' + '[ JUDUL INI SUDAH ADA ]'.center(60) + '|')
            print('|' + 'Silahkan masukkan data lain!'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter = input()
            return False
      
    if len(data_buku) <= 1:
        id_bk = 1
    elif "" in data_buku[len(data_buku) - 1]:
        id_bk = int(data_buku[len(data_buku) - 1][0]) + 1
        data_buku.remove(data_buku[len(data_buku) - 1])
    else : 
        id_bk = int(data_buku[len(data_buku) - 1][0]) + 1
    new_baris = [id_bk,list_kategori[input_kategori][0],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah, input_harga]
    data_buku.append(new_baris)
    core.tulis_csv(db_buku,data_buku)
    print('+' + '='*60 + '+')
    print('|' + '[ DATA BERHASIL DITAMBAHKAN ]'.center(60) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    print('+' + '='*60 + '+')
    enter  = input()

def perbarui_baris_buku():
    '''fungsi memperbarui data buku'''
    baca_data = core.baca_csv(db_buku)
    display_kategori, list_kategori = kategori_buku()
    nomor_urut = 0
    array = []
    for baris in baca_data:
        if baris[0] != 'id':
            array.append(baris)
            nomor_urut += 1
    
    update = input("| Masukkan Nomor urut data yang akan diperbarui: ")
    core.clear()
    if update.isdigit():
        update = int(update)
        if len(array) >= update >= 1:
            id = array[update - 1][0]
            data = core.cari_id_list(core.baca_csv(db_buku),id)

            if data:
                print("Kategori lama :", data[0][1])
                print(display_kategori)
                kategori_baru = input('| Masukkan kategori baru : ')
                if kategori_baru.isdigit():
                    kategori_baru = int(kategori_baru)
                    data[0][1] = list_kategori[kategori_baru - 1][0]
                id_kategori = kategori_baru if kategori_baru else data[0][1]

                print("|Judul lama :", data[0][2])
                judul_baru = input("| Masukkan Judul yang baru : ").lower()
                judul = judul_baru if judul_baru else data[0][2]
                
                print("| Penulis lama :", data[0][3])
                penulis_baru = input("|Masukkan Penulis yang baru : ").lower()
                penulis = penulis_baru if penulis_baru else data[0][3]
                
                print("| Penerbit lama :", data[0][4])
                penerbit_baru = input("| Masukkan Penerbit yang baru : ").lower()
                penerbit = penerbit_baru if penerbit_baru else data[0][4]

                print("| ISBN lama :", data[0][5])
                isbn_baru = input("| Masukkan ISBN yang baru : ")
                isbn = isbn_baru if isbn_baru else data[0][5]

                print("| Jumlah lama :", data[0][6])
                jumlah_baru = input("| Masukkan Jumlah yang baru : ")
                jumlah = jumlah_baru if jumlah_baru else data[0][6]

                print("| Harga lama :", data[0][7])
                harga_baru = input("| Masukkan Harga yang baru : ")
                harga = harga_baru if harga_baru else data[0][7]
        else:
            print('+' + '='*60 + '+')
            print('|' + '[ DATA TIDAK ADA ]'.center(60) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter  = input()
            return False
    else:
        print('+' + '='*60 + '+')
        print('|' + '[ DATA TIDAK ADA ]'.center(60) + '|')
        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
        print('+' + '='*60 + '+')
        enter  = input()
        return False
            
    for baris in baca_data:
        if baris[0] == id:
            baris[1] = id_kategori
            baris[2] = judul
            baris[3] = penulis
            baris[4] = penerbit
            baris[5] = isbn
            baris[6] = jumlah
            baris[7] = harga
            break
    core.tulis_csv(db_buku,baca_data)
    print('+' + '='*60 + '+')
    print('|' + '[ DATA BERHASIL DIPERBARUI ]'.center(60) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    print('+' + '='*60 + '+')
    enter  = input()

def hapus_buku(delete):
    '''fungsi hapus buku'''
    data = core.baca_csv(db_buku)
    nomor_urut = 0
    array = []
    for baris in data:
        if baris[0] != 'id':
            array.append(baris)
            nomor_urut += 1

    if len(array) >= delete >= 1:
        print(f'| ID: {array[delete - 1][0]}')
        print(f'| Judul: {array[delete - 1][2]}') 
        user = input('| Apakah anda ingin menghapus data diatas?(y/n) ')
        if user.lower() == 'y':
            if delete == len(array):
                index_id = [array[len(array) - 1][0],"","","","","","",""]
                data.remove(array[delete - 1])
                data.append(index_id)
                core.tulis_csv(db_buku, data)
            else:
                data.remove(array[delete - 1])
                core.tulis_csv(db_buku, data)
            print('+' + '='*60 + '+')
            print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(60) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter  = input()
        else:
            print('+' + '='*60 + '+')
            print('|' + '[ DATA BATAL DIHAPUS ]'.center(60) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter  = input()

            
def aksi_buku():
        cari_keyword=''
        halaman_sekarang=1
        halaman_total=1
        while True:
            core.clear()
            with open(ui_bk,'r') as buku:
                print(buku.read())
                pilihan = input("| Pilihan : ")
                match pilihan:
                    case '1':
                        core.clear()
                        tambah_buku()
                    case '2':
                        while True:
                            core.clear()
                            print('+' + '='*120 + '+')
                            print('|' + '[ DAFTAR BUKU ]'.center(120) + '|')
                            print('+' + '='*120 + '+')
                            data_buku,halaman_sekarang,halaman_total = dtframe_buku(cari_keyword,halaman_sekarang,halaman_total)
                            if len(data_buku) < 1:
                                print('+' + '='*120 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(120) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(120) + '|')
                                print('+' + '='*120 + '+')
                                enter  = input()
                            else:
                                with open('ui/page_daftar.txt','r') as page :
                                    print(page.read())
                                pilihan = input('| Pilihlah sesuai nomor diatas: ')
                                if pilihan == '1' and halaman_sekarang > 1:
                                    halaman_sekarang -= 1
                                elif pilihan == '2' and halaman_sekarang < halaman_total:
                                    halaman_sekarang += 1
                                elif pilihan == '9':
                                    break
                                elif pilihan == '0':
                                    exit()
                                else:
                                    continue 
                    case '3':
                        while True:
                            core.clear()
                            print('+' + '='*120 + '+')
                            print('|' + '[ DAFTAR BUKU ]'.center(120) + '|')
                            print('+' + '='*120 + '+')
                            data_buku,halaman_sekarang,halaman_total = dtframe_buku(cari_keyword,halaman_sekarang,halaman_total)
                            if len(data_buku) < 1:
                                print('+' + '='*120 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(120) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(120) + '|')
                                print('+' + '='*120 + '+')
                                enter  = input()
                            else:
                                with open('ui/page.txt','r') as page :
                                    print(page.read())
                                pilihan = input('| Pilihlah sesuai nomor diatas: ')
                                if pilihan == '1' and halaman_sekarang > 1:
                                    halaman_sekarang -= 1
                                elif pilihan == '2' and halaman_sekarang < halaman_total:
                                    halaman_sekarang += 1
                                elif pilihan == '3':
                                    perbarui_baris_buku()
                                elif pilihan == '9':
                                    break
                                elif pilihan == '0':
                                    exit()
                                else:
                                    continue 
                    case '4':
                        while True:
                            core.clear()
                            print('+' + '='*120 + '+')
                            print('|' + '[ DAFTAR BUKU ]'.center(120) + '|')
                            print('+' + '='*120 + '+')
                            data_buku,halaman_sekarang,halaman_total = dtframe_buku(cari_keyword,halaman_sekarang,halaman_total)
                            if len(data_buku) < 1:
                                print('+' + '='*120 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(120) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(120) + '|')
                                print('+' + '='*120 + '+')
                                enter  = input()
                            else:
                                with open('ui/page.txt','r') as page :
                                    print(page.read())
                                pilihan = input('| Pilihlah sesuai nomor diatas: ')
                                if pilihan == '1' and halaman_sekarang > 1:
                                    halaman_sekarang -= 1
                                elif pilihan == '2' and halaman_sekarang < halaman_total:
                                    halaman_sekarang += 1
                                elif pilihan == '3':
                                    user = input("| Masukkan Nomor urut data yang akan dihapus: ")
                                    if user.isdigit():
                                            hapus_buku(int(user))
                                            continue
                                    else:
                                        print('+' + '='*120 + '+')
                                        print('|' + '[ DATA NOT FOUND ]'.center(120) + '|')
                                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(120) + '|')
                                        print('+' + '='*120 + '+')
                                        enter  = input()
                                        continue
                                elif pilihan == '9':
                                    break
                                elif pilihan == '0':
                                    exit()
                                else:
                                    continue 
                    case '9':
                        core.clear()
                        break
                    case '0':
                        core.clear()
                        exit()
                    case _:
                        core.clear()

if __name__ == "__main__":
    aksi_buku()