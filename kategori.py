import csv
import pandas as pd
import core

def tulis_csv(data):
    with open('database/kategori.csv', 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

def list_kategori():
    df = pd.read_csv('database/kategori.csv')
    print(df)

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

def perbarui_baris_kategori(id, kategori):
    data = core.baca_csv('database/kategori.csv')
    for baris in data:
        if  baris[0] == id:
            baris[1] = kategori
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
#             print("[KATEGORI]")
#             print("Menu: ")
#             print("""
# 1. List Kategori
# 2. Tambah Kategori
# 3. Hapus Kategori
# 4. Keluar
#             """)
            user = int(input("Pilihan: "))
            match user:
                case 2:
                    list_kategori()
                    print('\n')
                case 1:
                    print("Masukkan kategori baru!")
                    user = input("Kategori: ")
                    tambah_kategori(user)
                    print('\n')
                case 3:
                    id = input("Masukkan ID data yang akan diperbarui: ")
                    data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                    if data == False:
                        print("Data Tidak ada"+'\n')
                    else:
                        print("Kategori lama :", data[1])
                        kategori = input("Masukkan Kategori yang baru : ")
                        perbarui_baris_kategori(id, kategori)
                        print("Data telah diperbarui."+'\n')
                case 4:
                    list_kategori()
                    user = input("Pilih data yang akan dihapus: ")
                    hapus_kategori(user)
                    print('\n')
                case 9:
                    pass
                case 0:
                    print("Keluar dari program."+'\n')
                    break

if __name__ == "__main__":
    list_kategori()
    tambah_kategori()
    perbarui_baris_kategori()
    hapus_kategori()
    aksi_kategori()