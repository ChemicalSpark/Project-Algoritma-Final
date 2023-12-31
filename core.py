import csv
import os

# membaca csv dengacn format list perbaris csv
def baca_csv(nama_file):
    data = []
    with open(nama_file, mode='r', newline='') as file_csv:
        csv_reader = csv.reader(file_csv)
        for baris in csv_reader:
            if len(baris) < 2:
                continue
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
        csv_writer.writerow(data_baru)

# menulis data baru ke baris index 
# nilai argumen harus list contoh : ['2', 'Fauzan', '232410102011', '0888888888']
def perbarui_baris_csv(nama_file, indeks_baris, data_baris_baru):
    data = baca_csv(nama_file)
    data[indeks_baris] = data_baris_baru
    tulis_csv(nama_file, data) #menimpa seluruh data 


# menghapus baris csv menggunakan index baris 
def hapus_baris_csv(nama_file, indeks_baris):
    data = baca_csv(nama_file)
    if 0 <= indeks_baris < len(data): # mengecek jika target index baris harus ada di data
        del data[indeks_baris]
        tulis_csv(nama_file, data) # menimpa seluruh data ke 
        return True
    else:
        return False


# mengembalikan nilai index baris dari id (list kolom index ke 0) yg ditemukan
def cari_index_dengan_id_list(data, id_p):
    index = 0
    for i in data:
        if (str(id_p) == str(i[0])):
            break
        index += 1
    return index


# mencari data dengan id (kolom csv index ke 0), dan mengembalikan nilai dari 1 baris jik diemukan
# contoh data yag dikembalikan of func : ['2', 'Fauzan', '232410102011', '0888888888']
def cari_id_list(data, nilai_id):

    return cari_list(data, nilai_id, 0, True)


# adalah fungsi search untuk list, yang dimana mengiterasi kolom setiap baris,
# disini memiliki 2 mode, strict (ketat) apa tidak, yang dimana ketat harus sama persis ( == )
# yang dicari (cocok untuk mencari id) (yang dimana merupaan 2 perbandingan string), 
# jika non strict digunakan untuk mencari jika kolom memiliki karakter yang bersangkutan
def cari_list(data, nilai, index_kolom:int, strict = False):
    hasil = []
    for i in data:
        # print(type(i[index_kolom]))
        if (type(i[index_kolom]) != type(nilai)): # mengecek jika perbandingan 
            print("Warning : Perbandingan memiliki tipe data yang berbeda\nmeloncati baris")
            continue
        if (strict == True):
            if (nilai == i[index_kolom]):
                hasil.append(i)
                break
        elif (strict == False): # jika mode strict
            if (nilai in i[index_kolom]) and (strict == False):
                hasil.append(i)

    return hasil

# adalah singkatan dari dump die, yang dimana merupakan fungsi untuk menampilkan isi variable dan mematikan 
def dd(data):
    print(data)
    exit()


# memecah data menjadi beberapa halaman
# limit : berguna sebagai batas jumlah data per halaman
# offset : dipakai untuk mengambil data dari target halaman
def pagination(data, limit, offset):
    hasil = [[]]  # Indeks 0 berisi array kosong untuk dummy, karena kelemahan list tidak boleh ada index 
    index = 1 # merepresentasikan halaman yang akan disi data (target halaman)
    count = 0 # menghitung jumlah data yang di masukan ke halaman

    
    for i in data: # iterasi data ke per baris
        if count == limit: # jika perhitungan jumlah data perbaris sama dengan limit (batas data per halaman)
            count = 0 # mengeset perhitungan data per halaman kembali ke no
            index += 1 # pindah halaman selanjutnya (mengubah target)
            hasil.append([])  # naambah array kosong untuk indeks berikutnya
        
        if not check_jika_index_ada(hasil, index): # mengecek jika target tidak ada
            hasil.append([])  # naambah array kosong untuk indeks berikutnya
            
        hasil[index].append(i) #menambahkan data ke target
        
        count += 1 # menambahkan perhitungan jumlah data ke perhalaman

    total_halaman = len(hasil) - 1 # dipakai untuk menghitung 

    # mengecek jika target halaman tidak ada
    if not check_jika_index_ada(hasil, offset):
        return [], 1

    return hasil[offset], total_halaman  # Mengembalikan hasil dan jumlah indeks

# fungsi ini untuk mengecek jika index di list ada
def check_jika_index_ada(data_list, index):
    try:
        data_list[index]
    except IndexError:
        return False
    return True

# data = [['1', 'Fauzan', '232410102011', '0888888888'],['2', 'Fauzan', '232410102011', '0888888888']]
# print(pagination(data, 1, 0))

    
# fungsi untuk clear console untuk bisa berfungsi di 2 tipe Sistem operasi
def clear():
    if os.name == 'posix': # jika os tipe unix
        os.system('clear')
    elif os.name == 'nt': # jika os tipe windows
        os.system('cls')
    else:
        print("Sistem operasi tidak didukung.")
