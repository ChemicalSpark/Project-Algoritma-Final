import csv
import core
import pandas as pd

nama_file = 'database/data_peminjam.csv'

def tulis_csv(data):
    core.tulis_csv(nama_file, data)

def tambah_baris_peminjam(nama, nim, telp):
    data = core.baca_csv(nama_file)
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)

def baca_baris_peminjam():
    df = pd.read_csv(nama_file)
    print(df.to_string(index=False))

def perbarui_baris_peminjam(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)

def hapus_baris_peminjam(delete):
    with open(nama_file,'r') as file:
        data = list(csv.reader(file))
        index_hapus = 0
        for arr in data:
            if arr[0] == delete:
                print(f'ID: {arr[0]}')
                print(f'Nama: {arr[1]}')
                print(f'NIM: {arr[2]}')
                user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
                if user == 'y':
                    data.pop(index_hapus)
                    with open('database/data_peminjam.csv','w',newline="") as new_data:
                        write = csv.writer(new_data)
                        write.writerows(data)
                        print('Data telah dihapus')
                        enter  = input("Klik ENTER untuk meneruskan")
                        core.clear()
                elif user == 'n':
                    print('Data batal dihapus')
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    core.clear()
                    print('Aksi tidak ada / tidak sesuai!')
                    enter  = input("Klik ENTER untuk meneruskan")
                    aksi_peminjam()
            index_hapus += 1
        

def aksi_peminjam():
    while True:
        core.clear()
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)
        pilih = input("| Pilihan: ")
        match pilih:
            case '1':
                nama = input("Masukkan Nama: ")
                no = input("Masukkan NIM: ")
                telp = input("Masukkan Nomor Telepon: ")
                if no:
                    tambah_baris_peminjam(nama, no, telp)   
                    print("Data telah ditambahkan")
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    core.clear()
                    print("Data Tidak ada")
                    enter  = input("Klik ENTER untuk meneruskan")
            case '2':
                core.clear()
                print("Data saat ini:")
                baca_baris_peminjam()
                enter  = input("Klik ENTER untuk meneruskan")
            case '3':
                print("Data saat ini:")
                baca_baris_peminjam()
                id = input("Masukkan ID data yang akan diperbarui: ")
                data = core.cari_id_list(core.baca_csv(nama_file), id)
                # if data == False:
                #     baca_baris_peminjam()
                #     print("Data Tidak ada")
                #     enter  = input("Klik ENTER untuk meneruskan")
                #     core.clear()
                if data:
                    print("Nama lama :", data[0][1])
                    nama_baru = input("Masukkan Nama yang baru : ")
                    nama = nama_baru if nama_baru else data[0][1]
                    
                    print("NIM lama :", data[0][2])
                    no_baru = input("Masukkan NIM yang baru : ")
                    no = no_baru if no_baru else data[0][2]
                    
                    print("Nomor Telepon lama :", data[0][3])
                    telp_baru = input("Masukkan Nomor Telepon yang baru : ")
                    telp = telp_baru if telp_baru else data[0][3]
                    perbarui_baris_peminjam(id, nama, no, telp)
                    print("Data telah diperbarui.")
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    core.clear()
                    print("Data Tidak ada")
                    enter  = input("Klik ENTER untuk meneruskan")
            case '4':
                print("Data saat ini:")
                baca_baris_peminjam()
                user = input("Masukkan ID data yang akan dihapus: ")
                if user:
                    hapus_baris_peminjam(user)
                else:
                    core.clear()
                    print('Data tidak ada')
                    enter  = input("Klik ENTER untuk meneruskan")
            case '9':
                break
            case '0':
                core.clear()
                exit()
            case _:
                core.clear()

if __name__ == "__main__":
    aksi_peminjam()
    tulis_csv()
    tambah_baris_peminjam()
    baca_baris_peminjam()
    perbarui_baris_peminjam()
    hapus_baris_peminjam()