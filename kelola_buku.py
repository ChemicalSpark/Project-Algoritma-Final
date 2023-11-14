import os
import csv
import core
#import pandas  as pd
os.system('cls')

def tulis_csv(data):
    with open('database/kategori.csv', 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

def list_buku():
    '''fungsi menampilkan buku'''
    with open('database/buku.csv', mode='r', encoding='cp1252') as list_data:
        baca_buku = list(csv.reader(list_data))
        # for_id = len(baca_buku)
        # nomor = 0
        # for i in baca_buku:
        #     nomor += 1
        #     print(nomor, i)
        return baca_buku

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
# def id_buku():
    # tampil_kategori, list_kategori = kategori_buku()
    #id_number = f"{list_kategori[input_kategori-1][0]}0"

def tambah_buku():
    '''fungsi tambah buku'''
    baca_buku = list_buku()
    tampil_kategori, list_kategori = kategori_buku()
    ulangi = 'y'
    while ulangi == 'y':
        print(tampil_kategori)
        input_kategori = int(input('pilih kategori buku : '))
        input_judul = input('masukkan judul : ')
        #input_id = input('masukkan ID buku : ')
        input_penulis = input('masukka penulis : ')
        input_penerbit = input('masukkan penerbit : ')
        input_isbn = input('masukkan ISBN : ')
        input_jumlah = int(input('masukkan jumlah buku : '))
        if len(baca_buku) < 1:
            id_bk = 1
        else :
            id_bk = len(baca_buku) + 1
        id_number = f"{list_kategori[input_kategori-1][0]}0{id_bk}"
        with open('database/buku.csv', mode='a', encoding='cp1252', newline='') as tambah_data:
            write = csv.writer(tambah_data)
            write.writerow([id_number,list_kategori[input_kategori-1][1],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah])
        ulangi = input('ada tambahan(y/n) ? : ')
    print('data telah ditambahkan')

def perbarui_baris_kategori(id_bk, input_kategori, input_judul, input_penulis, input_penerbit, input_isbn, input_jumlah):
    data = core.baca_csv('database/buku.csv')
    for baris in data:
        if  baris[0] == id_bk:
            baris[1] = input_kategori
            baris[2] = input_judul
            baris[3] = input_penulis
            baris[4] = input_penerbit
            baris[5] = input_isbn
            baris[6] = input_jumlah
            break
    tulis_csv(data)

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
                pilihan = input("Pilihan : ")
                baca_buku = list_buku()
                nomor = 0
                match pilihan:
                    case '2':
                        for i in baca_buku:
                            nomor += 1
                            print(f'{nomor} {i}')
                    case '1':
                        tambah_buku()
                    case '3':
                        id = input("Masukkan ID data yang akan diperbarui: ")
                        data = core.cari_id_list(core.baca_csv('database/buku.csv'), id)
                        if data == False:
                            print("Data Tidak ada"+'\n')
                        else:
                            print("Kategori lama :", data[1])
                            input_kategori = input("Masukkan Kategori yang baru : ")
                            print("Judul lama :", data[2])
                            input_judul = input("Masukkan Judul yang baru : ")
                            print("Penulis lama :", data[3])
                            input_penulis = input("Masukkan Penulis yang baru : ")
                            print("Penerbit lama :", data[4])
                            input_penerbit = input("Masukkan Penerbit yang baru : ")
                            print("jumlah lama :", data[5])
                            input_jumlah = input("Masukkan  yang baru : ")
                            perbarui_baris_kategori(id, input_kategori, input_judul, input_penulis, input_penerbit, input_jumlah)
                            print("Data telah diperbarui."+'\n')
                    case '4':
                        hapus_buku()
                    case '9':
                        pass
                    case '0':
                        print("Keluar dari program."+'\n')
                        break

if __name__ == "__main__":
    list_buku()
    kategori_buku()
    tambah_buku()
    hapus_buku()
    aksi_buku()




