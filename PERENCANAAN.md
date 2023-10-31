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
	3. Kelola Peminjaman
	4. Data Peminjam
	5. Pengaturan Admin

	[Submenu Kelola Genre]
		1. Tambah Genre
		2. Edit Genre 
		3. Hapus Genre
 	
 	[Submenu Kelola Buku]
		1. Tambah Buku (judul, penulis, penerbit, join genre)
		2. Edit Buku 
		3. Hapus Buku
		4. Cari Buku
  		
    	[Submenu Peminjam]
		1. Tambah Data Peminjam (nama, NIK, alamat)
		2. Update Data Peminjam
  		3. Hapus Peminjam

	[Submenu Peminjaman]
		1. Tambah Peminjaman (join buku, join peminjam)
		2. Update Peminjaman
		3. Hapus Peminjaman
  		4. Tanggal Pinjam
    		5. Tanggal Kembali

	[Submenu Pengaturan Admin]
		1. Pengaturan (ganti pass, hapus akun)
		2. Tambah Admin

		


	[DATABASE]

		[Admin] 		: id, username, Password
  		[genre] 		: id, nama_genre
		[buku]  		: id, id_genre, judul, penulis, penerbit
  		[peminjam] 		: id, nama_peminjam, nik_peminjam, update_peminjam, hapus_peminjam
		[peminjaman]		: id, id_buku, id_admin , tanggal_peminjaman, tanggal_pengembalian, status_peminjaman, denda_terlambat 







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


