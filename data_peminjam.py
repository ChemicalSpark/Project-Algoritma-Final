import csv
import core

nama_file = 'database/data_peminjam.csv'

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
    
    return new_id

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
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)

        pilih = int(input("Pilihan: "))
        if pilih == 1:
            nama = input("Masukkan Nama: ")
            no = input("Masukkan NIM: ")
            telp = input("Masukkan Nomor Telepon: ")
            tambah_baris_peminjam(nama, no, telp)
            print("Data telah ditambahkan."+'\n')
            core.clear()
        elif pilih == 2:
            core.clear()
            print("Data saat ini:")
            baca_baris_peminjam()
            print("\n")
        elif pilih == 3:
            id = input("Masukkan ID data yang akan diperbarui: ")
            data = core.cari_id_list(core.baca_csv(nama_file), id)
            if data == False:
                print("Data Tidak ada"+'\n')
                core.clear()
            else:
                print("Nama lama :", data[1])
                nama = input("Masukkan Nama yang baru : ")
                print("NIM lama :", data[2])
                no = input("Masukkan NIM yang baru : ")
                print("Nomor Telepon lama :", data[3])
                telp = input("Masukkan Nomor Telepon yang baru : ")
                perbarui_baris_peminjam(id, nama, no, telp)
                print("Data telah diperbarui."+'\n')
                core.clear()
        elif pilih == 4:
            id = input("Masukkan ID data yang akan dihapus: ")
            confirm = input('yakin ingin menghapus(y/n)? : ')
            if confirm == 'y':
                hapus_baris_peminjam(id)
                print("Data telah dihapus."+'\n')
                core.clear()
            elif confirm == 'n':
                print('Data batal dihapus'+'\n')
                core.clear()
        elif pilih == 9:
            print("Kembali")
        elif pilih == 0:
            print("Keluar dari program.")
            core.clear()
            break
        else:
            print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')
            core.clear()

if __name__ == "__main__":
    tulis_csv()
    tambah_baris_peminjam()
    baca_baris_peminjam()
    perbarui_baris_peminjam()
    hapus_baris_peminjam()
    aksi_peminjam()