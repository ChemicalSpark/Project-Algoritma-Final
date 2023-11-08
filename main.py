import csv
import core
import pandas as pd

def mainmenu():
    with open('Project-Algoritma-Final/ui/title.txt','r') as title:
        display = title.read()
        print(display)
        user = int(input("| > Menu: "))
        match user:
            case 1:
                 def list_kategori():
                    df = pd.read_csv('Project-Algoritma-Final/database/kategori.csv')
                    print(df)

                 def tambah_kategori(new_kategori):
                    with open('Project-Algoritma-Final/database/kategori.csv','r') as file:
                        data = [row.strip().split(',') for row in file.readlines()]
                        if len(data) <= 1:
                            length = 1
                            data_temp = f"{length},{new_kategori}\n"
                        else:
                            length = int(data[len(data) - 1][0]) + 1
                            data_temp = f"{length},{new_kategori}\n"

                    with open('Project-Algoritma-Final/database/kategori.csv','a') as add_kategori:
                        add_kategori.write(data_temp)
        
                 def hapus_kategori(delete):
                    with open('Project-Algoritma-Final/database/kategori.csv','r') as file:
                        data = list(csv.reader(file))
                        index_hapus = 0
                        for array in data:
                            if array[0] == delete:
                                print(f'ID: {array[0]}')
                                print(f'Kategori: {array[1]}')
                                user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
                                if user == 'y':
                                    data.pop(index_hapus)
                                    with open('Project-Algoritma-Final/database/kategori.csv','w',newline="") as new_data:
                                        write = csv.writer(new_data)
                                        write.writerows(data)
                            index_hapus += 1
                 while True:
                    print("[KATEGORI]")
                    print("Menu: ") 
                    print("""
1. List Kategori
2. Tambah Kategori
3. Hapus Kategori
                    """)
                    user = int(input("Pilihan: "))
                    match user:
                        case 1:
                            list_kategori()
                        case 2:
                            print("Masukkan kategori baru!")
                            user = input("Kategori: ")
                            tambah_kategori(user)
                        case 3:
                            list_kategori()
                            user = input("Pilih data yang akan dihapus: ")
                            hapus_kategori(user)
            
            case 2:
                pass
            case 3:
                print("[Peminjaman]")
                print("Menu: ") 
                print("""
1. Data Peminjam
2. Daftar Peminjaman
                 """)
                peminjam = int(input("Pilihan: "))
                match peminjam:
                     case 1:
                        nama_file = 'Project-Algoritma-Final/database/data_peminjam.csv'

                        def tulis_csv(data):
                            with open(nama_file, 'w', newline='') as file:
                                tulis = csv.writer(file)
                                tulis.writerows(data)

                        def tambah_rec(nama, nim, telp):
                            data = core.baca_csv(nama_file)
                            new_id = len(data) + 1
                            new_rec = [new_id, nama, nim, telp]
                            data.append(new_rec)
                            tulis_csv(data)

                        def baca_rec():
                            data = core.baca_csv(nama_file)
                            for rec in data:
                                print(rec)

                        def perbarui_rec(id, nama, nim, telp):
                            data = core.baca_csv(nama_file)
                            for rec in data:
                                if  rec[0] == id:
                                    rec[1] = nama
                                    rec[2] = nim
                                    rec[3] = telp
                                    break
                            tulis_csv(data)

                        def hapus_rec(id):
                            hasil = core.baca_csv(nama_file)
                            index_baris = 0
                            for baris in hasil:
                                if baris[0] == str(id):
                                    break
                                index_baris += 1

                            if index_baris == 0:
                                # baris 0 merupakan baris kolom
                                print("data tidak ditemukan")
                            else:
                                core.hapus_baris_csv(nama_file,index_baris)


                        while True:
                            print("Pilih operasi:")
                            print("1. Tambah Data Peminjam")
                            print("2. Tampilkan Data peminjam")
                            print("3. Perbarui Data Peminjam")
                            print("4. Hapus Data Peminjam")
                            print("5. Keluar")

                            pilih = int(input("Masukkan pilihan (1/2/3/4/5): "))
                            if pilih == 1:
                                nama = input("Masukkan Nama: ")
                                no = input("Masukkan NIM: ")
                                telp = input("Masukkan Nomor Telepon: ")
                                tambah_rec(nama, no, telp)
                                print("Data telah ditambahkan."+'\n')
                            elif pilih == 2:
                                print("Data saat ini:")
                                baca_rec()
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

                     case 2:
                        pass
            case 4:
                pass
            case 5:
                pass
            case _:
                mainmenu()
        
    
mainmenu()