import os

filepath = 'Project-Algoritma-Final/database/data_peminjam.csv'
if os.path.exists(filepath):
    with open (filepath, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
else:
    data = []

def tambah_csv(nama, no, telp, status):
    new_id = len(data) + 1
    new_rec = f"{new_id},{nama},{no},{telp},{status}"
    data.append(new_rec)

    with open(filepath, 'a') as file:
        file.write(new_rec+'\n')

def baca_csv():
    for rec in data:
        print(rec)

def perbarui_csv(id, nama, no, telp, status):
    for i,rec in enumerate(data):
        rec_id, _, _ = rec.split(',')
        if int(rec_id) == id:
            up_rec = f"{id},{nama}, {no}, {telp}, {status}"
            data[i] = up_rec

    with open(filepath, 'w') as file:
        file.write('\n'.join(data))

def hapus_csv(id):
    data[:] = [record for record in data if int(record.split(',')[0]) != id]

    with open(filepath, 'w') as file:
        file.write('\n'.join(data))

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
        tambah_csv(nama, no, telp, status)
        print("Data telah ditambahkan.")
    elif pilih == 2:
        print("Data saat ini:")
        baca_csv()
    elif pilih == 3:
        id = int(input("Masukkan ID data yang akan diperbarui: "))
        nama = input("Masukkan Nama yang baru: ")
        no = input("Masukkan NIM yang baru: ")
        telp = input("Masukkan Nomor Telepon yang baru: ")
        status = input("Masukkan Status yang baru: ")
        perbarui_csv(id, nama, no, telp, status)
        print("Data telah diperbarui.")
    elif pilih == 4:
        id = int(input("Masukkan ID data yang akan dihapus: "))
        hapus_csv(id)
        print("Data telah dihapus.")
    elif pilih == 5:
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada.")