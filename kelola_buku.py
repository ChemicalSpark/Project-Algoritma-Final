import os
import csv
import core
import pandas  as pd

db_buku = 'database/buku.csv'
db_kategori   = "database/kategori.csv"
ui_bk = "ui/kelola_buku.txt"

def list_buku():
    '''fungsi read data buku'''
    with open(db_buku, mode='r', encoding='cp1252') as list_data:
        baca_buku = list(csv.reader(list_data))
        return baca_buku
    
def dtframe_buku(cari_keyword='',halaman_sekarang=1,halaman_total=1):
    '''fungsi menampilkan data frame buku'''
    
    daftar_buku = core.baca_csv(db_buku)[1:]
    daftar_kategori = core.baca_csv(db_kategori)[1:]
    halaman_limit = 10
        
    if len(cari_keyword) > 1:
        daftar_buku = core.cari_list(daftar_buku,cari_keyword,1)
        halaman_sekarang = 1
    data_buku = [["No", "Judul", "Kategori", "Penulis", "Penerbit", "ISBN", "Jumlah" , "id"]]
    
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
        # isbn = baris[5]
        jumlah = baris[6]
        harga = baris[7]
        
        data_buku.append([i, nama, nama_kategori, penulis, penerbit, jumlah, harga])
        i += 1
    # if len(data_buku) == 11:
    # membuat data frame dengan data buku dimulai dari index (me skip header)
    data_buku,halaman_total = core.pagination(data_buku[1:],halaman_limit,halaman_sekarang)
    df = pd.DataFrame(data_buku, columns=["No", "Nama", "Kategori", "Penulis", "Penerbit", "Jumlah", "Harga"])

    # untuk mengabaikan index bawaan pandas
    if len(data_buku) < 1:
        output = "* Data Kosong *"
        aksi_buku()
    else:
        output = df.to_string(index=False)

    hasil = ""
    if "\n" in output:
        lines = output.split("\n")
        for i in lines:
            hasil += i + "\n"
    else:
        hasil += output + "\n"
    print(hasil)
    print(" "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_buku,halaman_sekarang,halaman_total
    

def kategori_buku():
    '''fungsi menampilakn kategori buku'''
    with open(db_kategori, mode='r', encoding='cp1252') as kategori:
        list_kategori = list(csv.reader(kategori))
        nomor = 0
        tampil_kategori = ''
        for i in list_kategori:
            if i[0] == 'ID':
                continue
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
        print('| Pilihan kategori :')
        print(display_kategori)
        input_kategori = input('\n| Pilih kategori buku\t: ')
        input_judul = input('| Masukkan judul\t: ')
        input_penulis = input('| Masukkan penulis\t: ')
        input_penerbit = input('| Masukkan penerbit\t: ')
        input_isbn = input('| Masukkan ISBN\t\t: ')
        input_jumlah = input('| Masukkan jumlah buku\t: ')
        input_harga = input('| Masukkan harga buku\t: ')
        
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
                print('+' + '='*60 + '+')
                print('|' + '[ DATA ALREADY EXIST ]'.center(60) + '|')
                print('|' + 'Silahkan masukkan data lain!'.center(60) + '|')
                print('+' + '='*60 + '+')
            else:
                nomor += 1
        if nomor == len(data_buku):
            nama_file = db_buku
            new_baris = [id_bk,list_kategori[input_kategori][0],input_judul,input_penulis,input_penerbit,input_isbn,input_jumlah, input_harga]
            core.tambah_ke_csv(nama_file, new_baris)
            ulangi = input('| Ingin menambahkan buku lagi(y/n) ? : ')
    print('+' + '='*60 + '+')
    print('|' + '[ DATA BERHASIL DITAMBAHKAN ]'.center(60) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    print('+' + '='*60 + '+')
    enter  = input()

def update_buku(data_buku):
    '''fungsi update data buku'''
    display_kategori, list_kategori = kategori_buku()
    baca_buku = list_buku()
    cek = ''
    nilai = 0
    # data_buku,halaman_sekarang,halaman_total = dtframe_buku()
    input_no = input('| Masukkan nomor urut : ').strip()
    # core.dd(data_buku)
    
    # cek jika input berupa digit
    if not input_no.isdigit():
        input("input harus berupa angka!\ntekan enter untuk kembali...")
        return

    buku = core.cari_list(data_buku, int(input_no), 0, True)
    
    # jika hasil pencarian buku 0
    if len(buku) < 1:
        input(f"buku dengan no urut {input_no} tidak ada\ntekan enter untuk kembali...")
        return

    buku = buku[0]

    index_urut = core.cari_index_dengan_id_list(baca_buku, buku[0])
    
    print('rincian :')
    print('judul :',buku[2])
    print('id buku :',buku[0])
    confirm = input('yakin ingin update data ? y/n :')
    if confirm == 'y':
        print('pilih data yang akan diubah :')
        print('[1] kategori [2] judul [3] penulis [4] penerbit [5] ISBN [6] jumlah [7] harga [99] semua')
        pilihan = input('masukkan pilihan : ')
        # if pilihan
        match pilihan :
            case '1':
                print('pilihan kategori :')
                print(display_kategori)
                input_kategori = int(input('| Masukkan kategori baru : '))
                buku[1] = list_kategori[input_kategori - 1][0]
            case '2':
                buku[2] = input('masukkan judul baru : ')
            case '3':
                buku[3] = input('masukkan penulis baru : ')
            case '4':
                buku[4] = input('masukkan penerbit baru :')       
            case '5':
                buku[5] = input('masukkan ISBN baru : ')      
            case '6':
                buku[6] = input('masukkan jumlah baru : ')   
            case '7':
                buku[7] = input('masukkan harga baru : ')    
            case '99':
                print('| Pilihan kategori :')
                print(display_kategori)
                input_kategori = int(input('\n| Masukkan kategori baru : '))
                buku[1] = list_kategori[input_kategori - 1][0]
                buku[2] = input('masukkan judul baru : ')
                buku[3] = input('masukkan penulis baru : ')
                buku[4] = input('masukkan penerbit baru :')
                buku[5] = input('masukkan ISBN baru : ')
                buku[6] = input('masukkan jumlah baru : ')
                buku[7] = input('masukkan harga baru : ') 
            # if i[1]=='' or i[2]=='' or i[3]=='' or i[4]=='' or i[5]=='' or i[6]=='' or i[7]=='' :
    
        with open(db_buku, mode='w', newline='', encoding='cp1252') as data_kembali:
            masukkan_data = csv.writer(data_kembali)
            masukkan_data.writerows(baca_buku)
            print('+' + '='*60 + '+')
            print('|' + '[ DATA BERHASIL DIPERBARUI ]'.center(60) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
            print('+' + '='*60 + '+')
            kondisi = False
            # return False
            enter  = input()


def hapus_buku(delete):
    data = list_buku()
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
            data.remove(array[delete - 1])
            with open(db_buku, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
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
    # '''fungsi hapus buku'''
    # data_buku = list_buku()
    # kondisi = True

    # while kondisi == True :
    #     nilai = 0
    #     index_hapus = 0
    #     input_judul = input('| Masukkan judul : ').strip().title()
    #     for i in data_buku:
    #         if i[2] == input_judul:
    #             print('rincian :')
    #             print('judul : ',i[2])
    #             print('ID : ',i[0])
    #             confirm = input('| Yakin ingin menghapus(y/n)? : ')
    #             if confirm == 'y':
    #                 data_buku.pop(index_hapus)
    #                 with open(db_buku, mode='w', newline='', encoding='cp1252') as return_data:
    #                     masukkan_data = csv.writer(return_data)
    #                     masukkan_data.writerows(data_buku)
    #                     print('+' + '='*60 + '+')
    #                     print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(60) + '|')
    #                     print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    #                     print('+' + '='*60 + '+')
    #                     kondisi = False
    #                     enter  = input()
    #             else:
    #                 print('+' + '='*60 + '+')
    #                 print('|' + '[ DATA BATAL DIHAPUS ]'.center(60) + '|')
    #                 print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    #                 print('+' + '='*60 + '+')
    #                 enter  = input()
    #                 kondisi = False
    #         else:
    #             nilai += 1   
    #         if nilai == len(data_buku):
    #             print('+' + '='*60 + '+')
    #             print('|' + '[ DATA BATAL DIHAPUS ]'.center(60) + '|')
    #             print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
    #             print('+' + '='*60 + '+')
    #             enter  = input()
    #             kondisi = False
    #         index_hapus += 1
            
def aksi_buku():
        cari_keyword=''
        halaman_sekarang=1
        halaman_total=1
        while True:
            core.clear()
            with open(ui_bk,'r') as buku:
                display = buku.read() 
                print(display)
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
                                    update_buku(data_buku)
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