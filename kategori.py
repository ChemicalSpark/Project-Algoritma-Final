import csv
import pandas as pd
import core

nama_file = 'database/kategori.csv'

def tulis_csv(data):
    core.tulis_csv(nama_file, data)

def list_kategori():
    kategori_file = core.baca_csv(nama_file)
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

def tambah_kategori(kat):
    data = core.baca_csv(nama_file)
    if len(data) <= 1:
        new_id = 1
    else:
        new_id = int(data[len(data) - 1][0]) + 1

    new_baris = [new_id, kat]
    data.append(new_baris)
    tulis_csv(data)

def perbarui_baris_kategori(id, kat):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = kat
            break
    tulis_csv(data)
        
def hapus_kategori(delete):
    data = core.baca_csv(nama_file)
    nomor_urut = 0
    nomor = []
    for baris in data:
        if baris[0] != 'ID':
            nomor.append(baris)
            nomor_urut += 1

    if 1 <= delete <= len(nomor):
        print(f'ID: {nomor[delete - 1][0]}')
        print(f'Kategori: {nomor[delete - 1][1]}')     
        user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
        if user == 'y':
            data.remove(nomor[delete - 1])
            with open(nama_file, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
                print('+' + '='*32 + '+')
                print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(32) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(32) + '|')
                print('+' + '='*32 + '+')
                enter  = input()
        else:
            print('+' + '='*32 + '+')
            print('|' + '[ DATA BATAL DIHAPUS ]'.center(32) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(32) + '|')
            print('+' + '='*32 + '+')
            enter  = input()


def aksi_kategori():
    while True:
        core.clear()
        with open('ui/kategori.txt','r') as kat:
            display = kat.read()
            print(display)
        user = input("| Pilihan: ")
        match user:
            case '1':
                print('+' + '='*83 + '+')
                print('|' + '-'*37 + '[ NOTICE ]' + '-'*36 + '|')
                print('|' + 'Masukkan kategori baru!'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input("| Kategori: ")
                if user:
                    tambah_kategori(user)
                    print('+' + '='*83 + '+')
                    print('|' + '-'*37 + '[ NOTICE ]' + '-'*36 + '|')
                    print('|' + 'Kategori berhasil ditambahkan'.center(83) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    enter = input()
                else:
                    print('+' + '='*83 + '+')
                    print('|' + '-'*34 + '[ INPUT ERROR ]' + '-'*34 + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    enter  = input()
            case '2':
                core.clear()
                print('+' + '='*32 + '+')
                print('|' + '-'*4 + '[ DAFTAR KATEGORI BUKU ]' + '-'*4 + '|')
                print('+' + '='*32 + '+')
                list_kategori()
                print('+' + '='*32 + '+')
                print('|' + '-'*11 + '[ NOTICE ]' + '-'*11 + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(32) + '|')
                print('+' + '='*32 + '+')
                enter = input()
            case '3':
                core.clear()
                print('+' + '='*55 + '+')
                print('|' + '-'*15 + '[ DAFTAR KATEGORI BUKU ]' + '-'*16 + '|')
                print('+' + '='*55 + '+')
                list_kategori()
                read_data = core.baca_csv(nama_file)
                nomor_urut = 0
                nomor = []
                for baris in read_data:
                    if baris[0] != 'ID':
                        nomor.append(baris)
                        nomor_urut += 1
                update = input("Masukkan Nomor urut data yang akan diperbarui: ")
                if update.split() and update.isdigit():
                    update = int(update)
                    if 1 <= update <= len(nomor):
                        id = nomor[update -1][0]
                        data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                        if data:
                            print("Kategori lama :", data[0][1])
                            kat_baru = input("Masukkan Kategori yang baru : ")
                            kat = kat_baru if kat_baru else data[0][1]
                            perbarui_baris_kategori(id, kat)
                            print("Data telah diperbarui.")
                            enter  = input("Klik ENTER untuk meneruskan")
                        else:
                            print('+' + '='*55 + '+')
                            print('|' + '-'*18 + '[ DATA NOT FOUND ]' + '-'*19 + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                            print('+' + '='*55 + '+')
                            enter  = input()
                    else:
                        print('+' + '='*55 + '+')
                        print('|' + '-'*18 + '[ DATA NOT FOUND ]' + '-'*19 + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                        print('+' + '='*55 + '+')
                        enter  = input()
                else:
                    print('+' + '='*55 + '+')
                    print('|' + '-'*18 + '[ DATA NOT FOUND ]' + '-'*19 + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                    print('+' + '='*55 + '+')
                    enter  = input()
            case '4':
                core.clear()
                print('+' + '='*55 + '+')
                print('|' + '-'*15 + '[ DAFTAR KATEGORI BUKU ]' + '-'*16 + '|')
                print('+' + '='*55 + '+')
                list_kategori()
                user = input("\n| Pilih data yang akan dihapus: ")
                if user.split() and user.isdigit():
                    hapus_kategori(int(user))
                else:
                    print('+' + '='*55 + '+')
                    print('|' + '-'*18 + '[ DATA NOT FOUND ]' + '-'*19 + '|')
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