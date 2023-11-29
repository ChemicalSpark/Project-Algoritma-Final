# import session
import csv
import pandas as pd
import core
# path file database kategori
nama_file = 'database/kategori.csv'
# function untuk menulis data ke database
def tulis_csv(data):
    core.tulis_csv(nama_file, data)

# function untuk menampilkan daftar kategori
def list_kategori(cari_keyword='',halaman_sekarang=1,halaman_total=1):
    kategori_file = core.baca_csv(nama_file)[1:]
    halaman_limit = 10
    
    data_kategori = [['No,','kategori']]
    if len(cari_keyword) > 0:
        kategori_file = core.cari_list(kategori_file,cari_keyword,1)
        halaman_sekarang = 1
    data_kategori = [['ID','Kategori']]
    i = 1
    for baris in kategori_file:
        # if baris[0] == 'ID':
        #     continue
        kategori = baris[1]
        data_kategori.append([i,kategori])
        i += 1

    data_kategori, halaman_total = core.pagination(data_kategori[1:],halaman_limit,halaman_sekarang)
    
    if len(data_kategori) < 1:
        output = "* Data Kosong *"
    elif "" in kategori_file[len(kategori_file) - 1]:
        df = pd.DataFrame(data_kategori[:len(data_kategori) - 1],columns=['No','Kategori'])
        output = df.to_string(index=False)
    else:
        df = pd.DataFrame(data_kategori,columns=['No','Kategori'])
        output = df.to_string(index=False)

    hasil = ""
    for i in output.split("\n"):
        hasil += " "*35 + i + "\n"
    
    print(hasil)

    print(" "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_kategori,halaman_sekarang,halaman_total
    
# function untuk menambahkan kategori baru
def tambah_kategori(kat):
    data = core.baca_csv(nama_file)
    data_ada = []
    for cek in data[1:]:
        data_ada.append(cek[1])
        if kat in data_ada:
            print('+' + '='*83 + '+')
            print('|' + '[ DATA ALREADY EXIST ]'.center(83) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
            print('+' + '='*83 + '+')
            return False

    if len(data) <= 1:
        new_id = 1
    elif "" in data[len(data) - 1]:
        new_id = int(data[len(data) - 1][0]) + 1
        data.remove(data[len(data) - 1])
    else:
        new_id = int(data[len(data) - 1][0]) + 1

    new_baris = [new_id, kat]
    data.append(new_baris)
    tulis_csv(data)
    print('+' + '='*83 + '+')
    print('|' + '[ NOTICE ]'.center(83) + '|')
    print('|' + 'Kategori berhasil ditambahkan'.center(83) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
    print('+' + '='*83 + '+')

# function untuk memperbaharui kategori
def perbarui_baris_kategori(id, kat):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = kat
            break
    tulis_csv(data)
        
# funciton untuk menghapus kategori 
def hapus_kategori(delete):
    data = core.baca_csv(nama_file)
    nomor_urut = 0
    array = []
    for baris in data:
        if baris[0] != 'ID':
            array.append(baris)
            nomor_urut += 1

    if len(array) >= delete >= 1:
        print(f'| ID: {array[delete - 1][0]}')
        print(f'| Kategori: {array[delete - 1][1]}')
        user = input('| Apakah anda ingin menghapus data diatas?(y/n) ')
        if user.lower() == 'y':
            if delete == len(array):
                index_id = [array[len(array)-1][0],""]
                data.remove(array[delete - 1])
                data.append(index_id)
                with open(nama_file, 'w', newline="") as file:
                    write = csv.writer(file)
                    write.writerows(data)

            else:
                data.remove(array[delete - 1])
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


# main kategori
def aksi_kategori():
    cari_keyword = ''
    halaman_sekarang = 1
    halaman_total = 1
    while True:
        core.clear()
        with open('ui/kategori.txt','r') as kat:
            display = kat.read()
            print(display)
        user = input("| Pilihan: ")
        match user:
            case '1':
                core.clear()
                print('+' + '='*83 + '+')
                print('|' + '[ NOTICE ]'.center(83) + '|')
                print('|' + 'Masukkan kategori baru!'.center(83) + '|')
                print('+' + '='*83 + '+')
                user = input("| Kategori: ")
                if user:
                    tambah_kategori(user.strip().title())
                    enter = input()
                else:
                    print('+' + '='*83 + '+')
                    print('|' + '[ INPUT ERROR ]'.center(83) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    enter  = input()
            case '2':
                while True:
                    core.clear()
                    print(" "*25 + '+' + '='*32 + '+')
                    print(" "*25 + '|' + '[DAFTAR KATEGORI BUKU]'.center(32) + '|')
                    print(" "*25 + '+' + '='*32 + '+')
                    data_kategori,halaman_sekarang,halaman_total = list_kategori(cari_keyword,halaman_sekarang,halaman_total)
                    if len(data_kategori) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page_daftar.txt','r') as page :
                            print(page.read())
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == '1' and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == '2' and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == '9':
                            break
                        elif pilihan == '0':
                            exit()
                        else:
                            continue 
            case '3':
                while True:
                    core.clear()
                    print(" "*25 + '+' + '='*32 + '+')
                    print(" "*25 + '|' + '[DAFTAR KATEGORI BUKU]'.center(32) + '|')
                    print(" "*25 + '+' + '='*32 + '+')
                    data_kategori,halaman_sekarang,halaman_total = list_kategori(cari_keyword,halaman_sekarang,halaman_total)
                    if len(data_kategori) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page.txt','r') as page :
                                print(page.read())
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == '1' and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == '2' and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == '3':
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
                                    data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                                    if data:
                                        print('-'*57)
                                        print("| Kategori lama\t\t      :", data[0][1])
                                        kat_baru = input("| Masukkan Kategori yang baru : ")
                                        print('-'*57)
                                        if kat_baru:
                                            kat = kat_baru 
                                        else:
                                            kat = data[0][1]
                                            print('+' + '='*55 + '+')
                                            print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                                            print('+' + '='*55 + '+')
                                            enter  = input()
                                            aksi_kategori()

                                        perbarui_baris_kategori(id, kat)
                                        print('+' + '='*55 + '+') 
                                        print('|' + '[ NOTICE ]'.center(55) + '|')
                                        print('|' + 'Data Berhasil diperbaharui'.center(55) + '|')
                                        print('|' + 'Klik ENTER untuk meneruskan'.center(55) + '|')
                                        print('+' + '='*55 + '+')
                                        enter  = input()    
                                    else:
                                        print('+' + '='*55 + '+')
                                        print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                                        print('+' + '='*55 + '+')
                                        enter  = input()
                                else:
                                    print('+' + '='*55 + '+')
                                    print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                                    print('+' + '='*55 + '+')
                                    enter  = input()
                            else:
                                print('+' + '='*55 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                                print('+' + '='*55 + '+')
                                enter  = input()
                        elif pilihan == '9':
                            break
                        elif pilihan == '0':
                            exit()
                        else:
                            continue
            case '4':
                while True:
                    core.clear()
                    print(" "*25 + '+' + '='*32 + '+')
                    print(" "*25 + '|' + '[DAFTAR KATEGORI BUKU]'.center(32) + '|')
                    print(" "*25 + '+' + '='*32 + '+')
                    data_kategori,halaman_sekarang,halaman_total = list_kategori(cari_keyword,halaman_sekarang,halaman_total)
                    with open('ui/page.txt','r') as page :
                            print(page.read())
                    pilihan = input('| Pilihlah sesuai nomor diatas: ')
                    if pilihan == '1' and halaman_sekarang > 1:
                        halaman_sekarang -= 1
                    elif pilihan == '2' and halaman_sekarang < halaman_total:
                        halaman_sekarang += 1
                    elif pilihan == '3':
                        user = input("\n| Pilih data yang akan dihapus: ")
                        if user.isdigit():
                            hapus_kategori(int(user))
                            continue
                        else:
                            print('+' + '='*55 + '+')
                            print('|' + '[ DATA NOT FOUND ]'.center(55) + '|')
                            print('|' + 'Klik ENTER untuk melanjutkan!'.center(55) + '|')
                            print('+' + '='*55 + '+')
                            enter  = input()
                            continue
                    elif pilihan == '9':
                        break
                    elif pilihan == '0':
                        exit()
                    else:
                        continue
            case '9':
                core.clear()
                break
            case '0':
                core.clear()
                exit()
            case _:
                core.clear()

if __name__ == "__main__":
    aksi_kategori()