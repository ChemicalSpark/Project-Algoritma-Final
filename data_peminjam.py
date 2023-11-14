import csv
import core
import pandas as pd

nama_file = 'database/data_peminjam.csv'

def tulis_csv(data):
    core.tulis_csv(nama_file, data)

def tambah_baris_peminjam(nama, nim, telp):
    data = core.baca_csv(nama_file)
    new_id = len(data) + 1
    new_baris = [new_id, nama, nim, telp]
    data.append(new_baris)
    tulis_csv(data)

def baca_baris_peminjam():
    # data = core.baca_csv(nama_file)
    df = pd.read_csv(nama_file)
    print(df.to_string(index=False))
    # i = 1
    # data = [["No.", "Nama", "NIM", "Telp", "id"]]
                
    # # var untuk ditampilkan
    # data_tampil = [["No.", "Nama", "NIM", "Telp"]]
                
    # for baris in data:
                    
    #     # me skip baris kolom / header
    #     if baris[0] == "id":
    #         continue
                    
    #     data.append([i, baris[1], baris[2] , baris[3], baris[0]])
                    
    #     data_tampil.append([i, baris[1], baris[2] , baris[3]])
                            
    #     i += 1
                    
    # # membuat dataframe dan me-set kolom custom
    # df = pd.DataFrame(data_tampil[1:], columns=['No.', 'Nama', 'NIM','Telp'])

    # # untuk mengabaikan index bawaan pandas
    # output = df.to_string(index=False)
    # output = output.split("\n")
    # hasil = ""
    # for i in output:
    #     hasil += " "*23 + i + "\n"    
    # print(hasil)

def perbarui_baris_peminjam(id, nama, nim, telp):
    data = core.baca_csv(nama_file)
    for baris in data:
        if  baris[0] == id:
            baris[1] = nama
            baris[2] = nim
            baris[3] = telp
            break
    tulis_csv(data)

def hapus_baris_peminjam(id):
    # user = input('Masukkan ID yang akan dihapus: ')
    # row_delete = user
    # df = data.drop(row_delete)
    data = core.baca_csv(nama_file)
    index_baris = core.cari_index_dengan_id_list(data, id)
    if index_baris == 0:
        # baris 0 merupakan baris kolom
        print("data tidak ditemukan")
    else:
        core.hapus_baris_csv(nama_file,index_baris)

def aksi_peminjam():
    while True:
        with open('ui/data_peminjam.txt','r') as datpnjm:
            display = datpnjm.read()
            print(display)

        pilih = int(input("Pilihan: "))
        if pilih == 1:
            nama = input("Masukkan Nama: ")
            no = input("Masukkan NIM: ")
            telp = input("Masukkan Nomor Telepon: ")
            tambah_baris_peminjam(nama, no, telp)
            print("Data telah ditambahkan."+'\n')
            core.clear()
        elif pilih == 2:
            core.clear()
            print("Data saat ini:")
            baca_baris_peminjam()
            
        elif pilih == 3:
            print("Data saat ini:")
            baca_baris_peminjam()
            id = input("Masukkan ID data yang akan diperbarui: ")
            data = core.cari_id_list(core.baca_csv(nama_file), id)
            if data == False:
                print("Data Tidak ada"+'\n')
                baca_baris_peminjam()
                core.clear()
            else:
                print("Nama lama :", data[1])
                nama = input("Masukkan Nama yang baru : ")
                match nama:
                        case _:
                            pass
                print("NIM lama :", data[2])
                no = input("Masukkan NIM yang baru : ")
                match no:
                    case _:
                        pass
                print("Nomor Telepon lama :", data[3])
                telp = input("Masukkan Nomor Telepon yang baru : ")
                match telp:
                    case _:
                        pass
                perbarui_baris_peminjam(id, nama, no, telp)
                print("Data telah diperbarui."+'\n')
                enter  = print("Klik enter untuk meneruskan")
                core.clear()
        elif pilih == 4:
            id = input("Masukkan ID data yang akan dihapus: ")
            confirm = input('yakin ingin menghapus(y/n)? : ')
            if confirm == 'y':
                hapus_baris_peminjam(id)
                print("Data telah dihapus."+'\n')
                enter  = print("Klik enter untuk meneruskan")
                core.clear()
            elif confirm == 'n':
                print('Data batal dihapus'+'\n')
                enter  = print("Klik enter untuk meneruskan")
                core.clear()
        elif pilih == 9:
            print("Kembali")
        elif pilih == 0:
            print("Keluar dari program.")
            core.clear()
            break
        else:
            print("Pilihan tidak valid! Pilihlah sesuai nomor yang ada."+'\n')
            core.clear()

if __name__ == "__main__":
    aksi_peminjam()
    tulis_csv()
    tambah_baris_peminjam()
    baca_baris_peminjam()
    perbarui_baris_peminjam()
    hapus_baris_peminjam()