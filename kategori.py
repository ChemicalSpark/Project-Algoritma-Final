# import session
import csv
import pandas as pd
import core
# path file database kategori
nama_file = 'database/kategori.csv'
# function untuk menulis data ke database
def tulis_csv(data):
    core.tulis_csv(nama_file, data)

# function untuk menampilkan daftar kategori
def list_kategori(cari_keyword='',halaman_sekarang=1,halaman_total=1):
    kategori_file = core.baca_csv(nama_file)[1:]
    halaman_limit = 20
    
    if len(cari_keyword) > 1:
        kategori_file = core.cari_list(kategori_file,cari_keyword,1)
        halaman_sekarang = 1
    kategori_file, halaman_total = core.pagination(kategori_file,halaman_limit,halaman_sekarang)
    data_kategori = [['ID','Kategori']]
    i = 1
    for baris in kategori_file:
        if baris[0] == 'ID':
            continue
        kategori = baris[1]
        data_kategori.append([i,kategori])
        i += 1
    df = pd.DataFrame(data_kategori[1:],columns=['No','Kategori'])
    print(df.to_string(index=False))

    print('\n' , " "*10 + f'page {halaman_sekarang} to {halaman_total}')
    return data_kategori,halaman_sekarang,halaman_total
    
# function untuk menambahkan kategori baru
def tambah_kategori(kat):
    data = core.baca_csv(nama_file)
    data_ada = []
    for cek in data[1:]:
        data_ada.append(cek[1])
        if kat in data_ada:
            print('+' + '='*83 + '+')
            print('|' + '[ DATA ALREADY EXIST ]'.center(83) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
            print('+' + '='*83 + '+')
            return False

    if len(data) <= 1:
        new_id = 1
    else:
        new_id = int(data[len(data) - 1][0]) + 1

    new_baris = [new_id, kat]
    data.append(new_baris)
    tulis_csv(data)
    print('+' + '='*83 + '+')
    print('|' + '[ NOTICE ]'.center(83) + '|')
    print('|' + 'Kategori berhasil ditambahkan'.center(83) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
    print('+' + '='*83 + '+')

# function untuk memperbaharui kategori
def perbarui_baris_kategori(id, kat):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = kat
            break
    tulis_csv(data)
        
# funciton untuk menghapus kategori 
def hapus_kategori(delete):
    data = core.baca_csv(nama_file)
    nomor_urut = 0
    nomor = []
    for baris in data:
        if baris[0] != 'ID':
            nomor.append(baris)
            nomor_urut += 1

    if 1 <= delete <= len(nomor):
        print('-'*57)
        print(f'| ID\t  : {nomor[delete - 1][0]}')
        print(f'| Kategori: {nomor[delete - 1][1]}')     
        print('-'*57)
        user = input('| Apakah anda ingin menghapus data diatas?(y/n) ')
        if user == 'y' or user == 'Y':
            data.remove(nomor[delete - 1])
            with open(nama_file, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
                print('+' + '='*55 + '+')
                print('|' + '[ NOTICE ]'.center(55) + '|')
                print('|' + 'Data berhasil dihapus'.center(55) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                print('+' + '='*55 + '+')
                enter  = input()
        else:
            print('+' + '='*55 + '+')
            print('|' + '[ DATA GAGAL DIHAPUS ]'.center(55) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
            print('+' + '='*55 + '+')
            enter  = input()

# main kategori
def aksi_kategori():
    while True:
        core.clear()
        with open('ui/kategori.txt','r') as kat:
            display = kat.read()
            print(display)
        user = input("| Pilihan: ")
        match user:
            case '1':
                core.clear()
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Masukkan kategori baru!'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input("| Kategori: ")
                if user:
                    tambah_kategori(user.strip().title())
                    enter = input()
                else:
                    print('+' + '='*83 + '+')
                    print('|' + '[ INPUT ERROR ]'.center(83) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    enter  = input()
            case '2':
                cari_keyword = ''
                halaman_sekarang = 1
                halaman_total = 1
                while True:
                    core.clear()
                    print('+' + '='*32 + '+')
                    print('|' + '[DAFTAR KATEGORI BUKU]'.center(32) + '|')
                    print('+' + '='*32 + '+')
                    data_kategori,halaman_sekarang,halaman_total = list_kategori(cari_keyword,halaman_sekarang,halaman_total)
                    if len(data_kategori) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page.txt','r') as page :
                            display = page.read()
                            print(display)
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == '1' and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == '2' and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == '9':
                            break
                        else:
                            continue 
                    # print('\n+' + '='*32 + '+')
                    # print('|' + '[NOTICE]'.center(32) + '|')
                    # print('|' + 'Klik ENTER untuk melanjutkan!'.center(32) + '|')
                    # print('+' + '='*32 + '+')
                    # enter = input()
            case '3':
                core.clear()
                print('+' + '='*55 + '+')
                print('|' + '[DAFTAR KATEGORI BUKU]'.center(55) + '|')
                print('+' + '='*55 + '+')
                list_kategori()
                read_data = core.baca_csv(nama_file)
                nomor_urut = 0
                nomor = []
                for baris in read_data:
                    if baris[0] != 'ID':
                        nomor.append(baris)
                        nomor_urut += 1
                update = input("\n| Masukkan Nomor urut data yang akan diperbarui: ")
                if update.isdigit():
                    update = int(update)
                    if 1 <= update <= len(nomor):
                        id = nomor[update - 1][0]
                        data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                        if data:
                            print('-'*57)
                            print("| Kategori lama\t\t      :", data[0][1])
                            kat_baru = input("| Masukkan Kategori yang baru : ")
                            print('-'*57)
                            if kat_baru:
                                kat = kat_baru 

                            else:
                                kat = data[0][1]
                                print('+' + '='*55 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                                print('+' + '='*55 + '+')
                                enter  = input()
                                aksi_kategori()

                            perbarui_baris_kategori(id, kat)
                            print('+' + '='*55 + '+') 
                            print('|' + '[ NOTICE ]'.center(55) + '|')
                            print('|' + 'Data Berhasil diperbaharui'.center(55) + '|')
                            print('|' + 'Klik ENTER untuk meneruskan'.center(55) + '|')
                            print('+' + '='*55 + '+')
                            enter  = input()
                                
                        else:
                            print('+' + '='*55 + '+')
                            print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                            print('+' + '='*55 + '+')
                            enter  = input()
                    else:
                        print('+' + '='*55 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                        print('+' + '='*55 + '+')
                        enter  = input()
                else:
                    print('+' + '='*55 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                    print('+' + '='*55 + '+')
                    enter  = input()
            case '4':
                core.clear()
                print('+' + '='*55 + '+')
                print('|' + '[ DAFTAR KATEGORI BUKU ]'.center(55) + '|')
                print('+' + '='*55 + '+')
                list_kategori()
                user = input("\n| Pilih data yang akan dihapus: ")
                if user.split() and user.isdigit():
                    hapus_kategori(int(user))
                else:
                    print('+' + '='*55 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                    print('+' + '='*55 + '+')
                    enter  = input()
            case '9':
                core.clear()
                break
            case '0':
                core.clear()
                exit()
            case _:
                core.clear()

if __name__ == "__main__":
    aksi_kategori()