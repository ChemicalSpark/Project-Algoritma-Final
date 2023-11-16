import csv
import pandas as pd
import core

def tulis_csv(data):
    with open('database/kategori.csv', 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

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

if __name__ == "__main__":
    list_kategori()
    tambah_kategori()
    perbarui_baris_kategori()
    hapus_kategori()