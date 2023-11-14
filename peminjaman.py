import core

db_peminjam   = 'database/data_peminjam.csv'
db_peminjaman = 'database/peminjaman.csv'
db_buku       = 'database/buku.csv'

def baca_baris(nama_file_csv):
    data = core.baca_csv(nama_file_csv)
    for baris in data:
        print(baris)



while True:
    core.clear()
    tampilkan_peminjaman()
    print("Pilih operasi:")
    print("1. Tambah Peminjaman")
    print("3. Perbarui Peminjaman")
    print("4. Hapus Peminjaman")
    print("5. Keluar")

    pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
    
    if pilih == 1:
        tambah_peminjaman()
    elif pilih == 3:
        perbarui_peminjaman()
    elif pilih == 4:
        hapus_peminjaman()
    elif pilih == 5:
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
    