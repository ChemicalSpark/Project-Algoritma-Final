#perubahan

def perbarui_csv(nama_file, data, indeks_baris, baris_baru):
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

def perbarui_baris_csv_berdasarkan_nilai_kolom(nama_file, nama_kolom, nilai, baris_baru):
    data = baca_data_csv(nama_file)
    data_terbaru = [data[0]]
    indeks_kolom = data_terbaru[0].index(nama_kolom)

    for baris in data[1:]:
        if baris[indeks_kolom] == nilai:
            data_terbaru.append(baris_baru)
        else:
            data_terbaru.append(baris)

    tulis_csv(nama_file, data_terbaru)

def hapus_baris_csv_berdasarkan_nilai_kolom(nama_file, nama_kolom, nilai):
    data = baca_data_csv(nama_file)
    data_terbaru = [data[0]]
    indeks_kolom = data_terbaru[0].index(nama_kolom)

    for baris in data[1:]:
        if baris[indeks_kolom] != nilai:
            data_terbaru.append(baris)

    tulis_csv(nama_file, data_terbaru)

def tambah_csv(nama_file, data):
    with open(nama_file, 'w') as file:
        for baris in data:
            file.write(','.join(baris) + '\n')

def baca_csv(nama_file):
    data = []
    with open(nama_file, 'r') as file:
        for baris in file:
            data.append(baris.strip().split(','))
    return data
