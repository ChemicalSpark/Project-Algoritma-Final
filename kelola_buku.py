import os
import csv
import core
import pandas  as pd

def list_buku():
    '''fungsi menampilkan buku'''
    with open('database/buku.csv', mode='r', encoding='cp1252') as list_data:
        baca_buku = list(csv.reader(list_data))
        return baca_buku
    
def daftar_buku():
    '''fungsi menampilkan buku'''
    df = pd.read_csv('database/buku.csv')
    print(df)

def kategori_buku():
    '''fungsi menampilakn kategori buku'''
    with open('database/kategori.csv', mode='r', encoding='cp1252') as kategori:
        list_kategori = list(csv.reader(kategori))
        nomor = 0
        tampil_kategori = ''
        for i in list_kategori:
            nomor += 1
            tampil_kategori += f'[{nomor}] {i[1]}'
        return tampil_kategori, list_kategori

def tambah_buku():
    '''fungsi tambah buku'''
    data_buku = list_buku()
    tampil_kategori, list_kategori = kategori_buku()
    ulangi = 'y'
    while ulangi == 'y':
        print(tampil_kategori)
        input_kategori = int(input('pilih kategori buku : '))
        input_judul = input('masukkan judul : ')
        input_penulis = input('masukka penulis : ')
        input_penerbit = input('masukkan penerbit : ')
        input_isbn = input('masukkan ISBN : ')
        input_jumlah = int(input('masukkan jumlah buku : '))
        if len(data_buku) <= 1:
            id_bk = 1
        else :
            id_bk = int(data_buku[len(data_buku) - 1][0]) + 1
        with open('database/buku.csv', mode='a', encoding='cp1252', newline='') as tambah_data:
            write = csv.writer(tambah_data)
            write.writerow([id_bk,list_kategori[input_kategori-1][0],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah])
        ulangi = input('ada tambahan(y/n) ? : ')
    print('data telah ditambahkan')

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
                            list_kategori()
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
                            print(display_kategori)
                            input_kategori = int(input('masukkan kategori baru : '))
                            i[1] = display_kategori[input_kategori - 1][0]
                            i[2] = input('masukkan judul baru : ')
                            i[3] = input('masukkan penulis baru : ')
                            i[4] = input('masukkan penerbit baru :')
                            i[5] = input('masukkan ISBN baru : ')
                            i[6] = input('masukkan jumlah baru : ')
                    with open('database/buku.csv', mode='w', newline='', encoding='cp1252') as data_kembali:
                        masukkan_data = csv.writer(data_kembali)
                        masukkan_data.writerows(baca_buku)
                        print('data telah diperbarui')
                        kondisi = False
                else :
                    print('update dibatalkan')
                    kondisi = False
            else:
                nilai += 1

            if nilai == len(baca_buku):
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
                    with open('database/buku.csv', mode='w', newline='', encoding='cp1252') as return_data:
                        masukkan_data = csv.writer(return_data)
                        masukkan_data.writerows(data_buku)
                        print('data telah dihapus')
                        kondisi = False
                else:
                    print('data batal dihapus')
                    kondisi = False
            else:
                nilai += 1
            if nilai == len(data_buku):
                print('!! judul tidak ditemukan, silahkan masukkan judul yang benar !!')
            index_hapus += 1
            
def aksi_buku():
        while True:
            with open('ui/kelola_buku.txt','r') as buku:
                display = buku.read()
                print(display)
                pilihan = input("Pilihan : ")
                match pilihan:
                    case '1':
                        tambah_buku()
                        core.clear()
                    case '2':
                        daftar_buku()
                        # core.clear()
                    case '3':
                        update_buku()
                        core.clear()
                    case '4':
                        hapus_buku()
                        core.clear()
                    case '9':
                        core.clear()
                        pass
                    case '0':
                        print("Keluar dari program."+'\n')
                        core.clear()
                        break

if __name__ == "__main__":
    aksi_buku()
    daftar_buku()
    tambah_buku()
    hapus_buku()
    