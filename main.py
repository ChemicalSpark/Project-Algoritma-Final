import pandas as pd
import core
import login
import kategori
import kelola_buku
import data_peminjam

login.login()

def mainmenu():
    with open('ui/mainmenu.txt','r') as title:
        display = title.read()
        print(display)
        user = int(input("| > Menu: "))
        match user:
            case 1:
               while True:
                print("[KATEGORI]")
                print("Menu: ")
                print("""
1. List Kategori
2. Tambah Kategori
3. Hapus Kategori
4. Keluar
                """)
                user = int(input("Pilihan: "))
                match user:
                    case 1:
                        kategori.list_kategori()
                        print('\n')
                    case 2:
                        print("Masukkan kategori baru!")
                        user = input("Kategori: ")
                        kategori.tambah_kategori(user)
                        print('\n')
                    case 3:
                        kategori.list_kategori()
                        user = input("Pilih data yang akan dihapus: ")
                        kategori.hapus_kategori(user)
                        print('\n')
                    case 4:
                        print("Keluar dari program."+'\n')
                        break
            case 2:
                print('-- kelola buku --')
                print(''''
1. list buku
2. tambah buku
3. hapus buku
                      ''')
                pilihan = input("masukkan pilihan : ")
                baca_buku = kelola_buku.list_buku()
                nomor = 0
                match pilihan:
                    case '1':
                        for i in baca_buku:
                            nomor += 1
                            print(f'{nomor} {i}')
                    case '2':
                        kelola_buku.tambah_buku()
                    case '3':
                        kelola_buku.hapus_buku()
            case 3:
                print("[PEMINJAMAN]")
                print("Menu: ") 
                print("""
1. Data Peminjam
2. Daftar Peminjaman
                 """)
                peminjam = int(input("Pilihan: "))
                match peminjam:
                     case 1:
                        while True:
                            print("Pilih operasi:")
                            print("1. Tambah Data Peminjam")
                            print("2. Tampilkan Data peminjam")
                            print("3. Perbarui Data Peminjam")
                            print("4. Hapus Data Peminjam")
                            print("5. Keluar")

                            pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
                            nama_file = 'database/data_peminjam.csv'
                            if pilih == 1:
                                nama = input("Masukkan Nama: ")
                                no = input("Masukkan NIM: ")
                                telp = input("Masukkan Nomor Telepon: ")
                                data_peminjam.tambah_baris(nama, no, telp)
                                print("Data telah ditambahkan."+'\n')
                            elif pilih == 2:
                                print("Data saat ini:")
                                data_peminjam.baca_baris()
                                print("\n")
                            elif pilih == 3:
                                id = input("Masukkan ID data yang akan diperbarui: ")
                                data = core.cari_id_list(core.baca_csv(nama_file), id)
                                if data == False:
                                    print("Data Tidak ada"+'\n')
                                else:
                                    print("Nama lama :", data[1])
                                    nama = input("Masukkan Nama yang baru : ")
                                    print("NIM lama :", data[2])
                                    no = input("Masukkan NIM yang baru : ")
                                    print("Nomor Telepon lama :", data[3])
                                    telp = input("Masukkan Nomor Telepon yang baru : ")
                                    data_peminjam.perbarui_baris(id, nama, no, telp)
                                    print("Data telah diperbarui."+'\n')
                            elif pilih == 4:
                                id = input("Masukkan ID data yang akan dihapus: ")
                                confirm = input('yakin ingin menghapus(y/n)? : ')
                                if confirm == 'y':
                                    data_peminjam.hapus_baris(id)
                                    print("Data telah dihapus."+'\n')
                                elif confirm == 'n':
                                    print('Data batal dihapus'+'\n')
                            elif pilih == 5:
                                print("Keluar dari program.")
                                break
                            else:
                                print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')
                     case 2:
                        pass
            case 4:
                pass
            case 5:
                print("Keluar dari program.")
            case _:
                mainmenu()
        
    
mainmenu()