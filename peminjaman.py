import core

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'

def baca_baris(nama_file_csv):
    data = core.baca_csv(nama_file_csv)
    for baris in data:
        print(baris)

def hapus_baris(nama_file_csv,id):
    data = core.baca_csv(nama_file_csv)
    index_baris = core.cari_index_dengan_id_list(data, id)
    core.hapus_baris_csv(nama_file_csv, index_baris)


def perbarui_baris():
    exit()


# Fungsi Fungsi setelah Memilih Fitur

def tambah_peminjaman():
    nama = input("Masukkan NIM Peminjam: ")
    isbn = input("Masukkan ID Buku: ")
    tglpinjam = input("Masukkan Tanggal Peminjaman: ")
    tglkembali = input("Masukkan Tanggal Kembali: ")
    status = input("Masukkan Status: ")
    print("Data telah ditambahkan."+'\n')

def tampilkan_peminjaman():
    print("Data saat ini:")
    baca_baris(db_peminjaman)
    print("\n")

def perbarui_peminjaman():
    id = input("Masukkan ID Peminjaman yang akan diperbarui: ")
    data = core.cari_id_list(core.baca_csv(db_peminjam), id)
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
        perbarui_baris(id, nama, no, telp)
        print("Data telah diperbarui."+'\n')

def hapus_peminjaman():
    id = input("Masukkan ID data yang akan dihapus: ")
    hapus_baris(db_peminjaman,id)
    print("Data telah dihapus."+'\n')
    

while True:
    print("Pilih operasi:")
    print("1. Tambah Peminjaman")
    print("2. Tampilkan Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("9. Kembali")
    print("0. Keluar")

    pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
    
    if pilih == 1:
        tambah_peminjaman()
    elif pilih == 2:
        tampilkan_peminjaman()
    elif pilih == 3:
        perbarui_peminjaman()
    elif pilih == 4:
        hapus_peminjaman()
    elif pilih == 9:
         print("kembali")
    elif pilih == 0:
        print("Terima kasih! Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')

if __name__ == "__main__":
    baca_baris()
    hapus_baris()
    perbarui_baris()
    tambah_peminjaman()
    tampilkan_peminjaman()
    perbarui_peminjaman()
    hapus_peminjaman()
    