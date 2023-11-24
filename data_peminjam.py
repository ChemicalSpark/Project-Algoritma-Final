import csv
import core
import pandas as pd

nama_file = 'database/data_peminjam.csv'
#fungsi untuk meng-write data di database
def tulis_csv(data):
    core.tulis_csv(nama_file, data)

#fungsi untuk menambahkan data peminjam
def tambah_baris_peminjam(nama, nim, telp):
    data = core.baca_csv(nama_file)
    data_ada = []
    for cek in data:
        data_ada.append(cek[2])
        if nim in data_ada:
            print('+' + '='*40 + '+')
            print('|' + '[ NIM INI SUDAH ADA ]'.center(40) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
            print('+' + '='*40 + '+')
            return False
        
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)
    print('+' + '='*40 + '+')
    print('|' + '[ DATA TELAH DITAMBAHKAN ]'.center(40) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
    print('+' + '='*40 + '+')

#fungsi untuk membaca data_peminjam dan memberikan pagination 
def baca_baris_peminjam(cari_keyword='',halaman_sekarang=1,halaman_total=1):
    peminjam = core.baca_csv(nama_file)[1:]
    halaman_limit = 7
    
    data_peminjam = [['No','Nama','NIM','Nomor Telepon']]
    if len(cari_keyword) > 0:
        peminjam = core.cari_list(peminjam,cari_keyword,1)
        halaman_sekarang = 1
    i = 1
    for baris in peminjam:
        if baris[0] == 'ID':
            continue
        nama = baris[1]
        nim = baris[2]
        telp = baris[3]
        data_peminjam.append([i,nama,nim,telp])
        i += 1 
    data_peminjam,halaman_total = core.pagination(data_peminjam[1:],halaman_limit,halaman_sekarang)
    df = pd.DataFrame(data_peminjam, columns=['No','Nama','NIM','Nomor Telepon'])
    # output = print(df.to_string(index=False))
    if len(data_peminjam) < 1:
        output = "* Data Kosong *"
    else:
        output = df.to_string(index=False)

    hasil = ""
    for i in output.split("\n"):
        hasil += " "*15 + i + "\n" 
    print(hasil)

    print(" "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_peminjam,halaman_sekarang,halaman_total
    
#fungsi untuk memperbarui 1 baris data peminjam
def perbarui_baris_peminjam(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)

#fungsi untuk menghapus 1 baris data peminjam
def hapus_baris_peminjam(delete):
    data = core.baca_csv(nama_file)
    nomor_urut = 0
    nomor = []
    for baris in data:
        if baris[0] != 'ID':
            nomor.append(baris)
            nomor_urut += 1

    if 1 <= delete <= len(nomor):
        print(f'| ID: {nomor[delete - 1][0]}')
        print(f'| Nama: {nomor[delete - 1][1]}')
        print(f'| NIM: {nomor[delete - 1][2]}')
        print(f'| Nomor Telepon: {nomor[delete - 1][3]}')     
        user = input('| Apakah anda ingin menghapus data diatas?(y/n) ')
        if user.lower() == 'y':
            data.remove(nomor[delete - 1])
            with open(nama_file, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
                print('+' + '='*40 + '+')
                print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(40) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                print('+' + '='*40 + '+')
                enter  = input()
        else:
            print('+' + '='*40 + '+')
            print('|' + '[ DATA BATAL DIHAPUS ]'.center(40) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
            print('+' + '='*40 + '+')
            enter  = input()
        
#fungsi utama dari semua fungsi dijalankan
def aksi_peminjam():
    cari_keyword= ''
    halaman_sekarang= 1
    halaman_total= 1
    while True:
        core.clear()
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)
        pilih = input("| Pilihan: ")
        match pilih:
            case '1':
                core.clear()
                nama = input("| Masukkan Nama: ")
                nim = input("| Masukkan NIM: ")
                telp = input("| Masukkan Nomor Telepon: ")
                if nama and nim and telp:
                    tambah_baris_peminjam(nama.strip().title(), nim, telp) 
                    enter  = input() 
                    continue
                else:
                    print('+' + '='*40 + '+')
                    print('|' + '[ INPUT TIDAK LENGKAP ]'.center(40) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                    print('+' + '='*40 + '+')
                    enter  = input()
                    continue
            case '2':
                while True:
                    core.clear()
                    print(" "*12 + '+' + '='*60 + '+')
                    print(" "*12 + '|' + '[ DAFTAR DATA PEMINJAM ]'.center(60) + '|')
                    print(" "*12 + '+' + '='*60 + '+')
                    data_peminjam,halaman_sekarang,halaman_total = baca_baris_peminjam(cari_keyword,halaman_sekarang,halaman_total)

                    if len(data_peminjam[1:]) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page.txt','r') as page:
                            print(page.read())
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == "1" and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == "2" and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == "9":
                            break
                        elif pilihan == "0":
                            exit()
                        else:
                            continue
                    # print('+' + '='*60 + '+')
                    # print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    # print('+' + '='*60 + '+')
                    # enter  = input()
            case '3':
                while True:
                    core.clear()
                    print(" "*12 + '+' + '='*60 + '+')
                    print(" "*12 + '|' + '[ DAFTAR DATA PEMINJAM ]'.center(60) + '|')
                    print(" "*12 + '+' + '='*60 + '+')
                    data_peminjam,halaman_sekarang,halaman_total = baca_baris_peminjam(cari_keyword,halaman_sekarang,halaman_total)
                    with open('ui/page.txt','r') as page:
                        print(page.read())
                    pilihan = input('| Pilihlah sesuai nomor diatas: ')
                    if pilihan == "1" and halaman_sekarang > 1:
                        halaman_sekarang -= 1
                    elif pilihan == "2" and halaman_sekarang < halaman_total:
                        halaman_sekarang += 1
                    elif pilihan == "3":
                        read_data = core.baca_csv(nama_file)
                        nomor_urut = 0
                        nomor = []
                        for baris in read_data:
                            if baris[0] != 'ID':
                                nomor.append(baris)
                                nomor_urut += 1

                        update = input("| Masukkan Nomor urut data yang akan diperbarui: ")
                        if update.isdigit():
                            update = int(update)
                            if 1 <= update <= len(nomor):
                                id = nomor[update - 1][0]
                                data = core.cari_id_list(core.baca_csv(nama_file),id)
                                print("Nama lama :", data[0][1])
                                nama_baru = input("Masukkan Nama yang baru : ").strip().title()
                                nama = nama_baru if nama_baru else data[0][1]
                                
                                print("NIM lama :", data[0][2])
                                nim_baru = input("Masukkan NIM yang baru : ")
                                nim = nim_baru if nim_baru else data[0][2]
                                
                                print("Nomor Telepon lama :", data[0][3])
                                telp_baru = input("Masukkan Nomor Telepon yang baru : ")
                                telp = telp_baru if telp_baru else data[0][3]
                                perbarui_baris_peminjam(id, nama, nim, telp)
                                print('+' + '='*60 + '+') 
                                print('|' + '[ NOTICE ]'.center(60) + '|')
                                print('|' + 'Data Berhasil diperbaharui'.center(60) + '|')
                                print('|' + 'Klik ENTER untuk meneruskan'.center(60) + '|')
                                print('+' + '='*60 + '+')
                                enter  = input()

                            else:
                                print('+' + '='*60 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                                print('+' + '='*60 + '+')
                                enter  = input()
                        else:
                            print('+' + '='*60 + '+')
                            print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                            print('+' + '='*60 + '+')
                            enter  = input()
                    elif pilihan == "9":
                        break
                    elif pilihan == '0':
                        exit
                    else:
                        continue
            case '4':
                while True:
                    core.clear()
                    print(" "*12 + '+' + '='*60 + '+')
                    print(" "*12 + '|' + '[ DAFTAR DATA PEMINJAM ]'.center(60) + '|')
                    print(" "*12 + '+' + '='*60 + '+')
                    data_peminjam,halaman_sekarang,halaman_total = baca_baris_peminjam(cari_keyword,halaman_sekarang,halaman_total)
                    with open('ui/page.txt','r') as page:
                        print(page.read())
                    pilihan = input('| Pilihlah sesuai nomor diatas: ')
                    if pilihan == '1' and halaman_sekarang > 1:
                        halaman_sekarang -= 1
                    elif pilihan == '2' and halaman_sekarang < halaman_total:
                        halaman_sekarang += 1
                    elif pilihan == '3':
                        user = input("| Masukkan Nomor urut data yang akan dihapus: ")
                        if user.isdigit():
                            hapus_baris_peminjam(int(user))
                            continue
                        else:
                            print('+' + '='*60 + '+')
                            print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                            print('+' + '='*60 + '+')
                            enter  = input()
                            continue
                    elif pilihan == '9':
                        break
                    elif pilihan == '0':
                        exit()
                    else:
                        continue
            case '9':
                break
            case '0':
                core.clear()
                exit()
            case _:
                core.clear()

#masa gatau?
if __name__ == "__main__":
    aksi_peminjam()