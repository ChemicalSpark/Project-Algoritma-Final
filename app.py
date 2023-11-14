def buku():
    print(""" N0 | Buku\t\t| kateogori
    1. | Cinderella \t\t| H18+""")
    print("""1. Pilih buku
    2. Cari buku
    3. Next page""")


print("""
1. Tambah Peminjaman
2. Hapus
3. Update
4. Hapus Data
""")
user = input("> ")
match user:
    case '1':
        print(""" N0 | Nama\t\t| NIM
1. | Ahmad Fauzan\t\t| 232410102046""")
print('='*50)
print("""1. Tambah Peminjam
2. Pilih peminjam""")
user2 = input("> ")
match user2:
    case '1':
        nama = input("Nama: ")
        nim = input("NIM: ")
        buku()
    case '2':
        print(""" N0 | Nama\t\t| NIM
1. | Ahmad Fauzan\t\t| 232410102046""")
        user3 = input("Pilih no. peminjam: ")
        buku()