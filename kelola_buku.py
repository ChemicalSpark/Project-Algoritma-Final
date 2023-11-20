import os
import csv
import core
import pandas  as pd

db_buku = 'database/buku.csv'
db_kategori   = "database/kategori.csv"

def list_buku():
    '''fungsi read data buku'''
    with open(db_buku, mode='r', encoding='cp1252') as list_data:
        baca_buku = list(csv.reader(list_data))
        return baca_buku
    
def dtframe_buku():
    '''fungsi menampilkan data frame buku'''
    
    daftar_buku = core.baca_csv(db_buku)
    
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



    # membuat data frame dengan data buku dimulai dari index (me skip header)
    df = pd.DataFrame(data_buku[1:], columns=["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah"])

    # untuk mengabaikan index bawaan pandas
    output = df.to_string(index=False)
    print(output)
    
    

def kategori_buku():
    '''fungsi menampilakn kategori buku'''
    with open(db_kategori, mode='r', encoding='cp1252') as kategori:
        list_kategori = list(csv.reader(kategori))
        nomor = 0
        tampil_kategori = ''
        for i in list_kategori:
            nomor += 1
            tampil_kategori += f'[{nomor}] {i[1]} '
        return tampil_kategori, list_kategori

def tambah_buku():
    '''fungsi tambah buku'''
    data_buku = list_buku()
    display_kategori, list_kategori = kategori_buku()
    ulangi = 'y'
    while ulangi == 'y':
        nomor = 0
        print('pilihan kategori :')
        print(display_kategori)
        input_kategori = input('pilih kategori buku : ')
        input_judul = input('masukkan judul : ')
        input_penulis = input('masukka penulis : ')
        input_penerbit = input('masukkan penerbit : ')
        input_isbn = input('masukkan ISBN : ')
        input_jumlah = input('masukkan jumlah buku : ')
        if input_kategori and input_judul and input_penulis and input_penerbit and input_isbn and input_jumlah:
            input_kategori = int(input_kategori)
            input_jumlah = int(input_jumlah)
            print('+' + '='*60 + '+')
            print('|' + '[ PROSES ]'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter  = input()
        else:
            print('+' + '='*60 + '+')
            print('|' + '[ DATA TIDAK LENGKAP ]'.center(60) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
            print('+' + '='*60 + '+')
            enter  = input()
            return False

        if len(data_buku) <= 1:
            id_bk = 1
        else :
            id_bk = int(data_buku[len(data_buku) - 1][0]) + 1
        for i in data_buku:
            if i[2] == input_judul:
                print('!'*27,'PERINGATAN','!'*27)
                print('<< data yang ditambahkan sudah ada, silahkan masukkan data lain >>')
            else:
                nomor += 1
        if nomor == len(data_buku):
            with open(db_buku, mode='a', encoding='cp1252', newline='') as tambah_data:
                write = csv.writer(tambah_data)
                write.writerow([id_bk,list_kategori[input_kategori-1][0],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah])
            ulangi = input('ada tambahan(y/n) ? : ')
    print('+' + '='*60 + '+')
    print('|' + '[ DATA BERHASIL DITAMBAHKAN ]'.center(60) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    print('+' + '='*60 + '+')
    enter  = input()

def update_buku():
    '''fungsi update data buku'''
    display_kategori, list_kategori = kategori_buku()
    baca_buku = list_buku()
    kondisi = True
    while kondisi == True:
        nilai = 0
        input_judul = input('masukkan judul buku : ')
        for i in baca_buku:
            if i[2]==input_judul:
                print('rincian :')
                print('judul :',i[2])
                print('id buku :',i[0])
                confirm = input('yakin ingin update data ? y/n :')
                if confirm == 'y':
                    print('pilih data yang akan diubah :')
                    print('[1] kategori [2] judul [3] penulis [4] penerbit [5] ISBN [6] jumlah [99] semua')
                    pilihan = input('masukkan pilihan : ')
                    match pilihan :
                        case '1':
                            print('pilihan kategori :')
                            print(display_kategori)
                            input_kategori = int(input('masukkan kategori baru : '))
                            i[1] = list_kategori[input_kategori - 1][0]
                        case '2':
                            i[2] = input('masukkan judul baru : ')
                        case '3':
                            i[3] = input('masukkan penulis baru : ')
                        case '4':
                            i[4] = input('masukkan penerbit baru :')       
                        case '5':
                            i[5] = input('masukkan ISBN baru : ')      
                        case '6':
                            i[6] = input('masukkan jumlah baru : ')     
                        case '99':
                            print('pilihan kategori :')
                            print(display_kategori)
                            input_kategori = int(input('masukkan kategori baru : '))
                            i[1] = list_kategori[input_kategori - 1][0]
                            i[2] = input('masukkan judul baru : ')
                            i[3] = input('masukkan penulis baru : ')
                            i[4] = input('masukkan penerbit baru :')
                            i[5] = input('masukkan ISBN baru : ')
                            i[6] = input('masukkan jumlah baru : ')
                    with open(db_buku, mode='w', newline='', encoding='cp1252') as data_kembali:
                        masukkan_data = csv.writer(data_kembali)
                        masukkan_data.writerows(baca_buku)
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA BERHASIL DIPERBARUI ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        kondisi = False
                        enter  = input()
                else :
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA BATAL DIPERBARUI ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    kondisi = False
                    enter = input()
            else:
                nilai += 1

            if nilai == len(baca_buku):
                core.clear()
                print('!! judul tidak ditemukan, silahkan masukkan judul yang benar !!')


def hapus_buku():
    '''fungsi hapus buku'''
    data_buku = list_buku()
    kondisi = True

    while kondisi == True :
        nilai = 0
        index_hapus = 0
        input_judul = input('masukkan judul : ')
        for i in data_buku:
            if i[2] == input_judul:
                print('rincian :')
                print('judul : ',i[2])
                print('ID : ',i[0])
                confirm = input('yakin ingin menghapus(y/n)? : ')
                if confirm == 'y':
                    data_buku.pop(index_hapus)
                    with open(db_buku, mode='w', newline='', encoding='cp1252') as return_data:
                        masukkan_data = csv.writer(return_data)
                        masukkan_data.writerows(data_buku)
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        kondisi = False
                        enter  = input()
                else:
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA BATAL DIHAPUS ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    enter  = input()
                    kondisi = False
            else:
                nilai += 1   
            if nilai == len(data_buku):
                print('!! judul tidak ditemukan, silahkan masukkan judul yang benar !!')
            index_hapus += 1
            
def aksi_buku():
        while True:
            core.clear()
            with open('ui/kelola_buku.txt','r') as buku:
                display = buku.read()
                print(display)
                pilihan = input("Pilihan : ")
                match pilihan:
                    case '1':
                        core.clear()
                        tambah_buku()
                    case '2':
                        core.clear()
                        print('+' + '='*120 + '+')
                        print('|' + '[ DAFTAR BUKU ]'.center(120) + '|')
                        print('+' + '='*120 + '+')
                        dtframe_buku()
                        print('+' + '='*120 + '+')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(120) + '|')
                        print('+' + '='*120 + '+')
                        enter  = input()
                    case '3':
                        core.clear()
                        dtframe_buku()
                        update_buku()
                    case '4':
                        core.clear()
                        dtframe_buku()
                        hapus_buku()
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