import csv
import os

filepath = 'Project-Algoritma-Final/database/data_peminjam.csv'
def baca_csv():
    if os.path.exists(filepath):
        with open (filepath, 'r') as file:
            baca = csv.reader(file)
            data = list(baca)
    else:
        data = []
    return data

def tulis_csv(data):
    with open(filepath, 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

def tambah_rec(nama, nim, telp, status):
    data = baca_csv()
    new_id = len(data) + 1
    new_rec = [new_id, nama, nim, telp, status]
    data.append(new_rec)
    tulis_csv(data)

def baca_rec():
    data = baca_csv()
    for rec in data:
        print(rec)

def perbarui_rec(id, nama, nim, telp, status):
    data = baca_csv()
    for rec in data:
        if int(rec[0]) == id:
            rec[1] = nama
            rec[2] = nim
            rec[3] = telp
            rec[4] = status
            break
    tulis_csv(data)

def hapus_rec(id):
    data = baca_csv()
    data = [rec for rec in data if int(rec[0]) != id]
    baca_csv(data)

while True:
    print("Pilih operasi:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
    if pilih == 1:
        nama = input("Masukkan Nama: ")
        no = input("Masukkan NIM: ")
        telp = input("Masukkan Nomor Telepon: ")
        status = input("Masukkan Status: ")
        tambah_rec(nama, no, telp, status)
        print("Data telah ditambahkan.")
    elif pilih == 2:
        print("Data saat ini:")
        baca_rec()
    elif pilih == 3:
        id = int(input("Masukkan ID data yang akan diperbarui: "))
        nama = input("Masukkan Nama yang baru: ")
        no = input("Masukkan NIM yang baru: ")
        telp = input("Masukkan Nomor Telepon yang baru: ")
        status = input("Masukkan Status yang baru: ")
        perbarui_rec(id, nama, no, telp, status)
        print("Data telah diperbarui.")
    elif pilih == 4:
        id = int(input("Masukkan ID data yang akan dihapus: "))
        hapus_rec(id)
        print("Data telah dihapus.")
    elif pilih == 5:
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada.")
