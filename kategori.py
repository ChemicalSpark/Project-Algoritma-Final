import csv
import pandas as pd
import core

def tulis_csv(data):
    core.tulis_csv('database/kategori.csv', data)

def list_kategori():
    df = pd.read_csv('database/kategori.csv')
    print(df.to_string(index=False))

def tambah_kategori(new_kategori):
    with open('database/kategori.csv','r') as file:
        data = [row.strip().split(',') for row in file.readlines()]
        if len(data) <= 1:
            length = 1
            data_temp = f"{length},{new_kategori}\n"
        else:
            length = int(data[len(data) - 1][0]) + 1
            data_temp = f"{length},{new_kategori}\n"

    with open('database/kategori.csv','a') as add_kategori:
        add_kategori.write(data_temp)

def perbarui_baris_kategori(id, kat):
    data = core.baca_csv('database/kategori.csv')
    for baris in data:
        if  baris[0] == id:
            baris[1] = kat
            break
    tulis_csv(data)
        
def hapus_kategori(delete):
    with open('database/kategori.csv','r') as file:
        data = list(csv.reader(file))
        index_hapus = 0
        for array in data:
            if array[0] == delete:
                print(f'ID: {array[0]}')
                print(f'Kategori: {array[1]}')
                user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
                if user == 'y':
                    data.pop(index_hapus)
                    with open('database/kategori.csv','w',newline="") as new_data:
                        write = csv.writer(new_data)
                        write.writerows(data)
            index_hapus += 1

def aksi_kategori():
    while True:
        core.clear()
        with open('ui/kategori.txt','r') as kat:
            display = kat.read()
            print(display)
        user = input("| Pilihan: ")
        match user:
            case '1':
                print("| Masukkan kategori baru!")
                user = input("| Kategori: ")
                tambah_kategori(user)
                print("| Kategori berhasil ditambahkan!")
                enter = input("| Klik Enter untuk melanjutkan... ")
                core.clear()
            case '2':
                core.clear()
                list_kategori()
                enter = input("| Klik Enter untuk melanjutkan... ")
            case '3':
                list_kategori()
                id = input("Masukkan ID data yang akan diperbarui: ")
                data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                if data == False:
                    list_kategori()
                    print("Data Tidak ada")
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
                else:
                    print("Kategori lama :", data[0][1])
                    kat_baru = input("Masukkan Kategori yang baru : ")
                    kat = kat_baru if kat_baru else data[0][1]
                    perbarui_baris_kategori(id, kat)
                    print("Data telah diperbarui.")
                    enter  = input("Klik ENTER untuk meneruskan")
                    core.clear()
            case '4':
                list_kategori()
                user = input("Pilih data yang akan dihapus: ")
                hapus_kategori(user)
                match user:
                    case _:
                        core.clear()
                        print('Data tidak ada')
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
    list_kategori()
    tambah_kategori()
    perbarui_baris_kategori()
    hapus_kategori()