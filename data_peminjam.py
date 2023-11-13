import csv
import core

nama_file = 'database/data_peminjam.csv'

# data = core.baca_csv(nama_file)
# data = core.convert_ke_associative_dict(data)
# print(data)
# exit()


def tulis_csv(data):
    with open(nama_file, 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

def tambah_baris_peminjam(nama, nim, telp):
    data = core.baca_csv(nama_file)
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)

def baca_baris_peminjam():
    data = core.baca_csv(nama_file)
    for baris in data:
        print(baris)

def perbarui_baris_peminjam(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)

def hapus_baris_peminjam(id):
    data = core.baca_csv(nama_file)
    index_baris = core.cari_index_dengan_id_list(data, id)
    if index_baris == 0:
        # baris 0 merupakan baris kolom
        print("data tidak ditemukan")
    else:
        core.hapus_baris_csv(nama_file,index_baris)

def aksi_peminjam():
    while True:
        # print("Data Peminjam:")
        # print("1. Tambah Data")
        # print("2. Daftar Peminjam")
        # print("3. Perbarui Data")
        # print("4. Hapus Data")
        # print("0. Kembali")

        pilih = int(input("Pilihan: "))
        if pilih == 1:
            nama = input("Masukkan Nama: ")
            no = input("Masukkan NIM: ")
            telp = input("Masukkan Nomor Telepon: ")
            tambah_baris_peminjam(nama, no, telp)
            print("Data telah ditambahkan."+'\n')
        elif pilih == 2:
            print("Data saat ini:")
            baca_baris_peminjam()
            print("\n")
        elif pilih == 3:
            id = input("Masukkan ID data yang akan diperbarui: ")
            data = core.cari_id_list(core.baca_csv(nama_file), id)
            if data == False:
                print("Data Tidak ada"+'\n')
            else:
                print("Nama lama :", data[1])
                nama = input("Masukkan Nama yang baru : ")
                print("NIM lama :", data[2])
                no = input("Masukkan NIM yang baru : ")
                print("Nomor Telepon lama :", data[3])
                telp = input("Masukkan Nomor Telepon yang baru : ")
                perbarui_baris_peminjam(id, nama, no, telp)
                print("Data telah diperbarui."+'\n')

        elif pilih == 4:
            id = input("Masukkan ID data yang akan dihapus: ")
            confirm = input('yakin ingin menghapus(y/n)? : ')
            if confirm == 'y':
                hapus_baris_peminjam(id)
                print("Data telah dihapus."+'\n')
            elif confirm == 'n':
                print('Data batal dihapus'+'\n')
        elif pilih == 9:
            print("Kembali")
        elif pilih == 0:
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')

if __name__ == "__main__":
    tulis_csv()
    tambah_baris_peminjam()
    baca_baris_peminjam()
    perbarui_baris_peminjam()
    hapus_baris_peminjam()
    aksi_peminjam()