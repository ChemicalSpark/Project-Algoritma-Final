Login Screen :

+---------------------------------+
|			CLI Perpus			  |
+---------------------------------+
	Selamat Datang Di CLI Perpus
		  Silahkan Login

Username : fauzan
Password : mulet

[MAIN MENU]

Main Menu :

	1. kelola Genre
 	2. Kelola Buku
	3. Data Peminjam
	4. Kelola Peminjaman
	5. Pengaturan Admin

	1. [Submenu Kelola Genre]
		1. Tambah Genre
		2. Edit Genre 
		3. Hapus Genre
 	
 	2. [Submenu Kelola Buku]
		1. Tambah Buku (judul, penulis, penerbit, join genre)
		2. Edit Buku 
		3. Hapus Buku
		4. Cari Buku
  		
    3. [Submenu Peminjam]
		1. Tambah Data Peminjam (nama, NIK, alamat)
		2. Update Data Peminjam
  		3. Hapus Peminjam

	4. [Submenu Peminjaman]
		1. Tambah Peminjaman (join buku, join peminjam)
		2. Update Peminjaman
		3. Hapus Peminjaman
  		4. Tanggal Pinjam
    		5. Tanggal Kembali

	5. [Submenu Pengaturan Admin]
		1. Pengaturan (ganti pass, hapus akun)
		2. Tambah Admin

		


[DATABASE]

[Admin]:
- id 
- username
- password

[Buku]:
- id 
- id_kategori
- judul
- penulis
- penerbit

[Kategori]:
- id 
- nama_kategori

[Peminjam]
- nik
- nama 
- alamat

[Peminjaman]:
- id 
- id_buku
- tanggal_peminjaman
- tanggal_pengembalian
- status_peminjaman (Misalnya: 'Dipinjam', 'Dikembalikan')
- denda_terlambat








[TAMPILAN_KELOLA_BUKU]

	+-----+--------------------------+------------+-----------------+------------+
	| No. |         Judul            |   Penulis  |    Penerbit     |   Genre    |
	+-----+--------------------------+------------+-----------------+------------+
	|  1  |   Judul Buku 1           |  Penulis 1 |   Penerbit 1    |   Genre 1  |
	|  2  |   Judul Buku 2           |  Penulis 2 |   Penerbit 2    |   Genre 2  |
	|  3  |   Judul Buku 3           |  Penulis 3 |   Penerbit 3    |   Genre 3  |
	|  4  |   Judul Buku 4           |  Penulis 4 |   Penerbit 4    |   Genre 4  |
	+-----+--------------------------+------------+-----------------+------------+
	Page 1 of 1

	Tambah Buku [a], Edit Buku [b], Hapus Buku [c], Cari Buku [d]
		Input : 


