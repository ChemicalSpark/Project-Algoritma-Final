**[LOGIN]**
- Username
- Passsword

**[MAIN MENU]**
1. Kategori Buku
2. Buku
3. Peminjaman
4. Pengaturan Admin

	**[[Submenu-Kategori Buku]]**
   	1. List Kategori Buku
   	2. Tambah Kategori Buku
   	4. Hapus Kategori Buku
   	5. Cari Kategori Buku _(pending)_

   	**[[Submenu-Buku]]**
   	1. List Buku
   	2. Tambah Buku
   	3. Hapus Buku
   	4. Cari buku _(pending)_

   	**[[Submenu-Peminjaman]]**
   	1. Peminjaman Buku
   	2. List Data Peminjaman
   	3. List Data Peminjam
   	4. Hapus data peminjaman

   	**[[Submenu-Pengaturan Admin]]**
   	1. Register Admin
   	2. List Admin
   	3. Hapus Akun Admin


**[DATABASE FORMAT]**
- Admin		: ID, Username, Password
- Kategori	: ID, Nama kategori
- Buku		: ID, Kategori, Judul, Penulis, Penerbit, isbn
- Peminjam	: ID, Nama, NIK/NIM, No.Telp, Status
- Peminjaman: ID, Date, Nama Peminjam, Nama Buku, Deadline, Denda

**[]**




# Mockup Versi Kelompok


# Mockup Fitur Peminjaman

+-----+-------------------+------------+----------------------+
| No. |       Nama        |    NIM     |       Status         |
+-----+-------------------+------------+----------------------+
|  1  |  John Doe         | 123456789  | Belum Dikembalikan   |
|  2  |  Jane Smith       | 987654321  | Belum Lunas          |
|  3  |  Robert Johnson   | 456789123  | Dikembalikan         |
+-----+-------------------+------------+----------------------+



page 1 of 1

a ("Pilih Peminjam") , s ("Cari Peminjam") ,  d ("mode kelola peminjam") , z ("pindah halaman ke kiri") , x ("Pindah Halaman ke kanan")
Silahkan Pilih Operasi
operasi : 



# Mockup Pilih Peminjaman 

Identitas Peminjam 
+-------------------------------------------------------------+
| Nama 		: John Doe										  |
| NIM  		: 456789123										  |
| Status	: Belum Dikembalikan | Belum Lunas 				  |
| Jumlah    : 21 / 45 yang telah dikembalikan				  |
+-------------------------------------------------------------+

Daftar Pemimjaman John Doe
+-----+----------------------------------+------------+----------------+--------------+-----------------------+-------------+--------------+
| No. |             Judul                |  Kategori  |     ISBN       | Tgl Dipinjam | Deadline    | Status  | Telat Hari  | Denda        |
+-----+----------------------------------+------------+----------------+--------------+-----------------------+-------------+--------------+
|  1  |  Harry Potter and the Sorcerer's |  Fantasy   |  978-0439554933|  2023-01-15  |  2023-02-15 |   P     |   0         | Rp. 0        |
|  2  |  To Kill a Mockingbird           |  Fiction   |  978-0061120084|  2023-02-10  |  2023-03-10 |   O     |   0         | Rp. 0        |
|  3  |  The Great Gatsby                |  Fiction   |  978-0743273565|  2023-03-05  |  2023-04-05 |   X     |   2         | Rp. 300.000  |
+-----+----------------------------------+------------+----------------+--------------+-------------+---------+-------------+--------------+

page 1 of 3

a ("buat peminjaman baru"), s ("ubah Peminjaman") z ("pindah halaman ke kiri") , x ("Pindah Halaman ke kanan")
Silahkan Pilih Operasi
operasi :



# Mockup tampilan Detail peminjaman

Identitas Peminjam 
+-------------------------------------------------------------+
| Nama 		: John Doe										  |
| NIM  		: 456789123										  |
+-------------------------------------------------------------+

Detail buku yang dipinjam
+-------------------------------------------------------------+
| Judul 				: Harry Potter and the Sorcerer's 	  |
| Kategori 				: Fantasy 							  |
| ISBN 					: 978-0439554933					  |
| Waktu Dipinjam 		: 15 Jan 2023						  |
| Deadline Peminjaman 	: 15 Feb 2023                         |
| Status 				: Belum Dikembalikan                  |
| Telat Hari 			: 0 Hari                              |
| Sisa Hari 			: 21 Hari                             |
| Denda 				: Rp. 0                               |
+-------------------------------------------------------------+


