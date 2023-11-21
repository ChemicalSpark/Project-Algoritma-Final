import csv
import core
import pandas as pd

nama_file = 'database/data_peminjam.csv'

def tulis_csv(data):
    core.tulis_csv(nama_file, data)


def tambah_baris_peminjam(nama, nim, telp):
    data = core.baca_csv(nama_file)
    data_ada = []
    for cek in data:
        data_ada.append(cek[2])
        if nim in data_ada:
            print('+' + '='*40 + '+')
            print('|' + '[ NIM INI SUDAH ADA ]'.center(40) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
            print('+' + '='*40 + '+')
            return False
        
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)
    print('+' + '='*40 + '+')
    print('|' + '[ DATA TELAH DITAMBAHKAN ]'.center(40) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
    print('+' + '='*40 + '+')



def baca_baris_peminjam():
    peminjam = core.baca_csv(nama_file)
    data_peminjam = [['No','Nama','NIM','Nomor Telepon']]
    i = 1
    for baris in peminjam:
        if baris[0] == 'ID':
            continue
        nama = baris[1]
        nim = baris[2]
        telp = baris[3]
        data_peminjam.append([i,nama,nim,telp])
        i += 1 
    df = pd.DataFrame(data_peminjam[1:], columns=['No','Nama','NIM','Nomor Telepon'])
    print(df.to_string(index=False))


def perbarui_baris_peminjam(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)


def hapus_baris_peminjam(delete):
    data = core.baca_csv(nama_file)
    nomor_urut = 0
    nomor = []
    for baris in data:
        if baris[0] != 'ID':
            nomor.append(baris)
            nomor_urut += 1

    if 1 <= delete <= len(nomor):
        print(f'ID: {nomor[delete - 1][0]}')
        print(f'Nama: {nomor[delete - 1][1]}')
        print(f'NIM: {nomor[delete - 1][2]}')
        print(f'Nomor Telepon: {nomor[delete - 1][3]}')     
        user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
        if user == 'y' or 'Y':
            data.remove(nomor[delete - 1])
            with open(nama_file, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
                print('+' + '='*40 + '+')
                print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(40) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                print('+' + '='*40 + '+')
                enter  = input()
        else:
            print('+' + '='*40 + '+')
            print('|' + '[ DATA BATAL DIHAPUS ]'.center(40) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
            print('+' + '='*40 + '+')
            enter  = input()
        

def aksi_peminjam():
    while True:
        core.clear()
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)
        pilih = input("| Pilihan: ")
        match pilih:
            case '1':
                core.clear()
                nama = input("Masukkan Nama: ")
                nim = input("Masukkan NIM: ")
                telp = input("Masukkan Nomor Telepon: ")
                if nama and nim and telp:
                    tambah_baris_peminjam(nama, nim, telp)  
                    enter  = input() 
                else:
                    print('+' + '='*40 + '+')
                    print('|' + '[ INPUT TIDAK LENGKAP ]'.center(40) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                    print('+' + '='*40 + '+')
                    enter  = input()
            case '2':
                core.clear()
                print('+' + '='*60 + '+')
                print('|' + '[ DAFTAR DATA PEMINJAM ]'.center(60) + '|')
                print('+' + '='*60 + '+')
                baca_baris_peminjam()
                print('+' + '='*60 + '+')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                print('+' + '='*60 + '+')
                enter  = input()
            case '3':
                core.clear()
                print("Data saat ini:")
                baca_baris_peminjam()
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
                        id = nomor[update - 1][0]
                        data = core.cari_id_list(core.baca_csv(nama_file),id)
                        if data:
                            print("Nama lama :", data[0][1])
                            nama_baru = input("Masukkan Nama yang baru : ")
                            nama = nama_baru if nama_baru else data[0][1]
                            
                            print("NIM lama :", data[0][2])
                            nim_baru = input("Masukkan NIM yang baru : ")
                            nim = nim_baru if nim_baru else data[0][2]
                            
                            print("Nomor Telepon lama :", data[0][3])
                            telp_baru = input("Masukkan Nomor Telepon yang baru : ")
                            telp = telp_baru if telp_baru else data[0][3]
                            perbarui_baris_peminjam(id, nama, nim, telp)
                            print("Data telah diperbarui.")
                            enter  = input("Klik ENTER untuk meneruskan")
                        else:
                            print('+' + '='*60 + '+')
                            print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                            print('+' + '='*60 + '+')
                            enter  = input()
                    else:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                else:
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    enter  = input()
            case '4':
                core.clear()
                print("Data saat ini:")
                baca_baris_peminjam()
                user = input("Masukkan Nomor urut data yang akan dihapus: ")
                if user.split() and user.isdigit():
                    hapus_baris_peminjam(int(user))
                else:
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    enter  = input()
            case '9':
                break
            case '0':
                core.clear()
                exit()
            case _:
                core.clear()

if __name__ == "__main__":
    aksi_peminjam()