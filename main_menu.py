print('''
Main Menu
1. Kelola Jenis Buku
2. Kelola Buku
3. Data Peminjam
4. Daftar Peminjaman
5. Kelola Akun Admin
6. Keluar
''')
mainmenu = int(input('Masukkan angka sesuai daftar menu diatas : '))

if mainmenu == 1:
    print('Kelola Jenis Buku')
    print('''
1. Tambah Jenis
2. Update Jenis
3. Hapus Jenis
''')
elif mainmenu == 2:
    print('Kelola Buku')
    print('''
1. Tambah Buku
2. Update Buku
3. Hapus Buku
''')
elif mainmenu == 3:
    print('Data Peminjam')
    print('''
1. Tambah Data Peminjam
2. Update Data Peminjam
3. Hapus Data Peminjam
''')
elif mainmenu == 4:
    print('Daftar Peminjaman')
    print('''
1. Tambah Data Peminjaman
2. Update Data Peminjaman
3. Hapus Data PEminjaman
''')
elif mainmenu == 5:
    print('Kelola Akun Admin')
    print('''
1. Ganti Password
2. Tambah Akun Admin
3. Hapus Akun Admin
''')
elif mainmenu == 6:
    print('harusnya sih logout')
else:
    print('Masukkan angka sesuai daftar yang ada!')
