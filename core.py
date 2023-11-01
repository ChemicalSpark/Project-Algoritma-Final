
def perbarui_csv(nama_file, data, indeks_baris, baris_baru):
    if 0 <= indeks_baris < len(data):
        data[indeks_baris] = baris_baru

        file_csv = open(nama_file, 'w')

        for baris in data:
            file_csv.write(','.join(baris) + '\n')

        file_csv.close()
        return True
    else:
        return False

		
def append_ke_csv(nama_file, new_data):
    file_csv = open(nama_file, 'a')
    for baris in new_data:
        file_csv.write(','.join(baris) + '\n')
    file_csv.close()

def baca_csv(nama_file):
    data = []
    file_csv = open(nama_file, 'r')
    for baris in file_csv:
        data.append(baris.strip().split(','))
    file_csv.close()
    return data

def hapus_baris_csv(nama_file, data, indeks_baris):
    if 0 <= indeks_baris < len(data):
        del data[indeks_baris]
        perbarui_data_csv(nama_file, data)
        return True
    else:
        return False

def perbarui_data_csv_berdasarkan_nilai_kolom(nama_file, data, nama_kolom, nilai, baris_baru):
    header = data[0]
    indeks_kolom = header.index(nama_kolom)

    for baris in data[1:]:
        if baris[indeks_kolom] == nilai:
            data[data.index(baris)] = baris_baru

    perbarui_data_csv(nama_file, data)

def hapus_baris_csv_berdasarkan_nilai_kolom(nama_file, data, nama_kolom, nilai):
    header = data[0]
    indeks_kolom = header.index(nama_kolom)

    data_terbaru = [header]
    for baris in data[1:]:
        if baris[indeks_kolom] != nilai:
            data_terbaru.append(baris)

    perbarui_data_csv(nama_file, data_terbaru)




