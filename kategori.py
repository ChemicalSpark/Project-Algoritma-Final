import csv
import pandas as pd
import core

nama_file = 'database/kategori.csv'

def tulis_csv(data):
    core.tulis_csv(nama_file, data)

def list_kategori():
    df = pd.read_csv(nama_file)
    df.index = df.index + 1
    print(df.to_string(index=True))

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
    with open(nama_file,'r') as file:
        data = list(csv.reader(file))
        index_hapus = 0
        for array in data:
            if array[0] == delete:
                print('+' + '-'*55 + '+')
                print(f'| ID\t   : {array[0]}')
                print(f'| Kategori : {array[1]}')
                print('+' + '-'*55 + '+')
                user = input('| Apakah anda yakin ingin menghapus data diatas?(y/n) ')

                if user == 'y':
                    data.pop(index_hapus)
                    with open(nama_file,'w',newline="") as new_data:
                        write = csv.writer(new_data)
                        write.writerows(data)
                    print('+' + '='*55 + '+')
                    print('|' + '-'*23 + '[ NOTICE ]' + '-'*22 + '|')
                    print('|' + 'Data berhasil dihapus!'.center(55) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan'.center(55) + '|')
                    print('+' + '='*55 + '+')
                    user = input()
                    core.clear()
                elif user == 'n':
                    print('Data batal dihapus')
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    core.clear()
                    print('+' + '='*83 + '+')
                    print('|' + '-'*32 + '[ DATA NOT FOUND ]' + '-'*33 + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    enter = input()
                    core.clear()
                    aksi_kategori()
            index_hapus += 1

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
                    core.clear()
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
                enter = input()
                print('+' + '='*32 + '+')
                print('|' + '-'*11 + '[ NOTICE ]' + '-'*11 + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(32) + '|')
                print('+' + '='*32 + '+')
                enter = input()
            case '3':
                list_kategori()
                id = input("Masukkan ID data yang akan diperbarui: ")
                data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                # if data == False:
                #     list_kategori()
                #     print("Data Tidak ada")
                #     enter  = input("| Klik Enter untuk melanjutkan... ")
                #     core.clear()
                if data:
                    print("Kategori lama :", data[0][1])
                    kat_baru = input("Masukkan Kategori yang baru : ")
                    kat = kat_baru if kat_baru else data[0][1]
                    perbarui_baris_kategori(id, kat)
                    print("Data telah diperbarui.")
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    core.clear()
                    print("Data tidak ada")
                    enter = input("Klik ENTER untuk meneruskan")
            case '4':
                core.clear()
                print('+' + '='*55 + '+')
                print('|' + '-'*15 + '[ DAFTAR KATEGORI BUKU ]' + '-'*16 + '|')
                print('+' + '='*55 + '+')
                list_kategori()
                user = input("\n| Pilih data yang akan dihapus: ")
                if user:
                    hapus_kategori(user)
                else:
                    core.clear()
                    print('+' + '='*83 + '+')
                    print('|' + '-'*32 + '[ DATA NOT FOUND ]' + '-'*33 + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
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