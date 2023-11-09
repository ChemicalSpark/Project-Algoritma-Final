import core
import csv

file1 = 'database/data_peminjam.csv'
file2 = 'database/peminjaman.csv'
file3 = 'database/buku.csv'
#function here


def baca_rec():
    data = core.baca_csv(file1)
    for rec in data:
        print(rec)
        

while True:
    print("Pilih operasi:")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
    if pilih == 1:
        nama = input("Masukkan NIM Peminjam: ")
        isbn = input("Masukkan ID Buku: ")
        tglpinjam = input("Masukkan Tanggal Peminjaman: ")
        tglkembali = input("Masukkan Tanggal Kembali: ")
        status = input("Masukkan Status: ")
        
        print("Data telah ditambahkan."+'\n')
    elif pilih == 2:
        print("Data saat ini:")
        baca_rec()
        print("\n")
    elif pilih == 3:
        id = input("Masukkan ID Peminjaman yang akan diperbarui: ")
        data = core.cari_id_list(core.baca_csv(nama_file), id)
        if data == False:
            print("Data Tidak ada"+'\n')
        else:
            print("NIM Peminjam lama :", data[1])
            nama = input("Masukkan NIM Peminjam yang baru : ")
            print("ID Buku lama :", data[2])
            no = input("Masukkan ID Buku yang baru : ")
            print("Tanggal Peminjaman lama :", data[3])
            telp = input("Masukkan Tanggal Peminjaman yang baru : ")
            print("Tanggal Kembali lama :", data[4])
            telp = input("Masukkan Tanggal Kembali yang baru : ")
            print("Status lama :", data[5])
            telp = input("Masukkan Status yang baru : ")
            perbarui_rec(id, nama, no, telp)
            print("Data telah diperbarui."+'\n')

    elif pilih == 4:
        id = input("Masukkan ID data yang akan dihapus: ")
        hapus_rec(id)
        print("Data telah dihapus."+'\n')
    elif pilih == 5:
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')