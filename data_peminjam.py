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
    
    return new_id

def baca_baris_peminjam():
    # data = core.baca_csv(nama_file)
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
    with open('database/data_peminjam.csv','r') as file:
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
                        enter  = input("Klik enter untuk meneruskan")
                        core.clear()
                elif user == 'n':
                    print('Data batal dihapus')
                    enter  = input("Klik enter untuk meneruskan")
                    core.clear()
            index_hapus += 1
    # data = core.baca_csv(nama_file)
    # index_baris = core.cari_index_dengan_id_list(data, id)
            if data == 0:
                print("data tidak ditemukan")
    # else:
    #     core.hapus_baris_csv(nama_file,index_baris)

def aksi_peminjam():
    while True:
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)

        pilih = int(input("Pilihan: "))
        match pilih:
            case 1:
                nama = input("Masukkan Nama: ")
                no = input("Masukkan NIM: ")
                telp = input("Masukkan Nomor Telepon: ")
                tambah_baris_peminjam(nama, no, telp)
                print("Data telah ditambahkan")
                enter  = input("Klik enter untuk meneruskan")
                core.clear()
            case 2:
                core.clear()
                print("Data saat ini:")
                baca_baris_peminjam()
                
            case 3:
                print("Data saat ini:")
                baca_baris_peminjam()
                id = input("Masukkan ID data yang akan diperbarui: ")
                data = core.cari_id_list(core.baca_csv(nama_file), id)
                if data == False:
                    baca_baris_peminjam()
                    print("Data Tidak ada")
                    enter  = input("Klik enter untuk meneruskan")
                    core.clear()
                else:
                    print("Nama lama :", data[1])
                    nama_baru = input("Masukkan Nama yang baru : ")
                    nama = nama_baru if nama_baru else data[1]
                    print("NIM lama :", data[2])
                    no_baru = input("Masukkan NIM yang baru : ")
                    no = no_baru if no_baru else data[2]
                    print("Nomor Telepon lama :", data[3])
                    telp_baru = input("Masukkan Nomor Telepon yang baru : ")
                    telp = telp_baru if telp_baru else data[3]
                    perbarui_baris_peminjam(id, nama, no, telp)
                    print("Data telah diperbarui.")
                    enter  = input("Klik enter untuk meneruskan")
                    core.clear()
            case 4:
                user = input("Masukkan ID data yang akan dihapus: ")
                hapus_baris_peminjam(user)
                match user:
                    case _:
                        aksi_peminjam()
                        core.clear()
            # confirm = input('yakin ingin menghapus(y/n)? : ')
            # if confirm == 'y':
            #     hapus_baris_peminjam(idhapus)
            #     print("Data telah dihapus."+'\n')
            #     enter  = print("Klik enter untuk meneruskan")
            #     core.clear()
            # elif confirm == 'n':
            #     print('Data batal dihapus'+'\n')
            #     enter  = print("Klik enter untuk meneruskan")
            # core.clear()
            case 9:
                print("Kembali")
            case 0:
                print("Keluar dari program.")
                core.clear()
                break
            case _:
                print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')
                core.clear()

if __name__ == "__main__":
    aksi_peminjam()
    tulis_csv()
    tambah_baris_peminjam()
    baca_baris_peminjam()
    perbarui_baris_peminjam()
    hapus_baris_peminjam()