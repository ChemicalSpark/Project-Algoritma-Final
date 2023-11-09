import csv

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
    hasil = False
    for i in data:
        if (type(i) == type(nilai_id)):
            print("Warning : Perbandingan memiliki tipe data yang berbeda\n")
        if (nilai_id == i[0]):
            hasil = i
            break
    return hasil


def convert_ke_associative_dict(data):
    # Mendapatkan header (key) dari baris pertama
    header = data[0]
    del data[0]
    # Inisialisasi dictionary kosong
    data_dict = {}
    
    # Iterasi melalui baris-baris selanjutnya untuk membuat dict
    for baris in data:
        # Membuat kamus asosiatif untuk setiap baris
        baris_dict = {}
        for i in header:
            baris_dict[header[i]] = baris[i]
        
        # Menambahkan kamus baris ke dalam kamus utama dengan menggunakan 'id' sebagai kunci
        data_dict[baris_dict['id']] = baris_dict
    
    return data_dict


def dd(data):
    print(data)
    exit()