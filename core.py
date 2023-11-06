import csv

def baca_csv(nama_file):
    data = []
    with open(nama_file, mode='r', newline='') as file_csv:
        csv_reader = csv.reader(file_csv)
        for baris in csv_reader:
            data.append(baris)
    return data

def baca_csv_sebagai_dict(nama_file):
    data = []
    with open(nama_file, mode='r', newline='') as file_csv:
        csv_reader = csv.DictReader(file_csv)
        for baris in csv_reader:
            data.append(baris)
    return data

def tulis_csv(nama_file, data):
    with open(nama_file, mode='w', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerows(data)

def tambah_ke_csv(nama_file, data_baru):
    with open(nama_file, mode='a', newline='') as file_csv:
        csv_writer = csv.writer(file_csv)
        csv_writer.writerows(data_baru)

def perbarui_baris_csv(nama_file, data, indeks_baris, baris_baru):
    if 0 <= indeks_baris < len(data):
        data[indeks_baris] = baris_baru
        tulis_csv(nama_file, data)
        return True
    else:
        return False

def hapus_baris_csv(nama_file, data, indeks_baris):
    if 0 <= indeks_baris < len(data):
        del data[indeks_baris]
        tulis_csv(nama_file, data)
        return True
    else:
        return False
<<<<<<< HEAD

def perbarui_baris_csv_berdasarkan_nilai_kolom(nama_file, data, nama_kolom, nilai, baris_baru):
    header = data[0]
    indeks_kolom = header.index(nama_kolom)

    for baris in data[1:]:
        if baris[indeks_kolom] == nilai:
            data[data.index(baris)] = baris_baru

    tulis_csv(nama_file, data)

def hapus_baris_csv_berdasarkan_nilai_kolom(nama_file, data, nama_kolom, nilai):
    header = data[0]
    indeks_kolom = header.index(nama_kolom)

    data_terbaru = [header]
    for baris in data[1:]:
        if baris[indeks_kolom] != nilai:
            data_terbaru.append(baris)

    tulis_csv(nama_file, data_terbaru)
=======
>>>>>>> ac17927823bbb76ef9396002257dab85071396f8
