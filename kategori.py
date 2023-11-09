import csv
import pandas as pd

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

        
while True:
    print("[KATEGORI]")
    print("Menu: ")
    print("""1. List Kategori
2. Tambah Kategori
3. Hapus Kategori
4. Keluar
    """)
    user = int(input("Pilihan: "))
    match user:
        case 1:
            list_kategori()
            print('\n')
        case 2:
            print("Masukkan kategori baru!")
            user = input("Kategori: ")
            tambah_kategori(user)
            print('\n')
        case 3:
            list_kategori()
            user = input("Pilih data yang akan dihapus: ")
            hapus_kategori(user)
            print('\n')
        case 4:
            print("Keluar dari program."+'\n')
            break