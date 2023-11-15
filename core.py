import csv
import os

# membaca csv dengacn format list perbaris csv
def baca_csv(nama_file):
    data = []
    with open(nama_file, mode='r', newline='') as file_csv:
        csv_reader = csv.reader(file_csv)
        for baris in csv_reader:
            data.append(baris)
    return data

# membaca csv dengacn format Dictionary perbaris csv
def baca_csv_sebagai_dict(nama_file):
    data = []
    with open(nama_file, mode='r', newline='') as file_csv:
        csv_reader = csv.DictReader(file_csv)
        for baris in csv_reader:
            data.append(baris)
    return data


# menulis baru seluruh data ke csv
def tulis_csv(nama_file, data):
    with open(nama_file, mode='w', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerows(data)

# menambah data ke csv (append data)
def tambah_ke_csv(nama_file, data_baru):
    with open(nama_file, mode='a', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerows(data_baru)

# menulis data baru ke baris index 
# nilai argumen harus list contoh : 
def perbarui_baris_csv(nama_file, indeks_baris, data_baris_baru):
    data = baca_csv(nama_file)
    if 0 <= indeks_baris < len(data):
        data[indeks_baris] = data_baris_baru
        tulis_csv(nama_file, data)
        return True
    else:
        return False

def hapus_baris_csv(nama_file, indeks_baris):
    data = baca_csv(nama_file)
    if 0 <= indeks_baris < len(data):
        del data[indeks_baris]
        tulis_csv(nama_file, data)
        return True
    else:
        return False


# mengembalikan nilai index baris dari id yg ditemukan
def cari_index_dengan_id_list(data, id):
    index = False
    for i in data:
        index += 1
        if (id == i[0]):
            break
    return index


# mencari data dengan id (kolom csv index ke 0), dan mengembalikan nilai dari 1 baris jik diemukan
# contoh data yag dikembalikan of func : ['2', 'Fauzan', '232410102011', '0888888888']
def cari_id_list(data, nilai_id):

    return cari_list(data, nilai_id, 0, True)


# adalaha fungsi search untuk list, yang dimana mengiterasi kolom setiap baris,
# disini memiliki 2 mode, strict (ketat) apa tidak, yang dimana ketat harus sama persis 
# yang dicari (cocok untuk mencari id) (yang dimana merupaan 2 perbandingan string), 
# jika non strict digunakan untuk mencari jika kolom memiliki karakter yang bersangkutan
def cari_list(data, nilai, index_kolom:int, strict = False):
    hasil = []
    for i in data:
        if (type(i[index_kolom]) != type(nilai)):
            # print("Warning : Perbandingan memiliki tipe data yang berbeda\nmeloncati baris")
            continue
        if (nilai == i[index_kolom]) and (strict == True):
            hasil.append(i)
            break
        elif (nilai in i[index_kolom]) and (strict == False):
            hasil.append(i)

    return hasil


def dd(data):
    print(data)
    exit()
    
def pagination(data, limit, offset):
    hasil = {}
    index = 1

    for i in data:
        if len(hasil.get(index, [])) < limit:
            hasil.setdefault(index, []).append(i)
        else:
            index += 1
            hasil.setdefault(index, []).append(i)

    return hasil.get(offset, []), len(hasil)

# data = [['1', 'Fauzan', '232410102011', '0888888888'],['2', 'Fauzan', '232410102011', '0888888888']]
# print(pagination(data, 1, 0))

    
    
def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print("Sistem operasi tidak didukung.")
