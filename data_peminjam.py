import csv
import core

nama_file = 'database/data_peminjam.csv'

# data = core.baca_csv(nama_file)
# data = core.convert_ke_associative_dict(data)
# print(data)
# exit()


def tulis_csv(data):
    with open(nama_file, 'w', newline='') as file:
        tulis = csv.writer(file)
        tulis.writerows(data)

def tambah_baris(nama, nim, telp):
    data = core.baca_csv(nama_file)
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)

def baca_baris():
    data = core.baca_csv(nama_file)
    for baris in data:
        print(baris)

def perbarui_baris(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)

def hapus_baris(id):
    data = core.baca_csv(nama_file)
    index_baris = core.cari_index_dengan_id_list(data, id)
    if index_baris == 0:
        # baris 0 merupakan baris kolom
        print("data tidak ditemukan")
    else:
        core.hapus_baris_csv(nama_file,index_baris)



if __name__ == "__main__":
    tulis_csv()
    tambah_baris()
    baca_baris()
    perbarui_baris()
    hapus_baris()