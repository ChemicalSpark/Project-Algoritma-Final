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
            tampil_kategori += f'[{nomor}] {i[1]} '
        return tampil_kategori, list_kategori

def tambah_buku():
    '''fungsi tambah buku'''
    baca_buku = list_buku()
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
        if len(baca_buku) <= 1:
            id_bk = 1
        else :
            id_bk = int(baca_buku[len(baca_buku) - 1][0]) + 1
        with open('database/buku.csv', mode='a', encoding='cp1252', newline='') as tambah_data:
            write = csv.writer(tambah_data)
            write.writerow([id_bk,list_kategori[input_kategori-1][0],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah])
        ulangi = input('ada tambahan(y/n) ? : ')
    print('data telah ditambahkan')

# def update_buku(baca_buku):
#     input_judul = input('masukkan judul buku : ')
#     for 


def hapus_buku():
    '''fungsi hapus buku'''
    input_judul = input('masukkan judul : ')
    with open('database/buku.csv', mode='r', encoding='cp1252') as hapus_data :
        list_data = list(csv.reader(hapus_data))
        index_hapus = 0

        for i in list_data:
            if i[2] == input_judul:
                print('rincian :')
                print('judul : ',i[2])
                print('ID : ',i[0])
                confirm = input('yakin ingin menghapus(y/n)? : ')
                if confirm == 'y':
                    list_data.pop(index_hapus)
                    with open('database/buku.csv', mode='w', newline='', encoding='cp1252') as data_kembali:
                        masukkan_data = csv.writer(data_kembali)
                        masukkan_data.writerows(list_data)
                        print('data telah dihapus')
                else:
                    print('data batal dihapus')
                
            index_hapus += 1

def aksi_buku():
        while True:
            with open('ui/kelola_buku.txt','r') as buku:
                display = buku.read()
                print(display)
                pilihan = input("Pilihan : ")
                match pilihan:
                    case '2':
                        core.clear()
                        daftar_buku()
                    case '1':
                        tambah_buku()
                        core.clear()
                    case '3':
                        pass
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
    