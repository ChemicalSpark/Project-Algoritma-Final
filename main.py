import login
import kategori
import peminjaman
import kelola_buku
import data_peminjam
import pengaturan_admin
import core

core.clear()
login.login()

def mainmenu():
    while True:
        core.clear()
        with open('ui/mainmenu.txt','r') as title:
            display = title.read()
            print(display)
            user = input("| > Menu: ")
            match user:
                case '1':
                    while True:
                        core.clear()
                        with open('ui/kategori.txt','r') as kat:
                            display = kat.read()
                            print(display)
                        user = input("| Pilihan: ")
                        match user:
                            case '1':
                                print("| Masukkan kategori baru!")
                                user = input("| Kategori: ")
                                kategori.tambah_kategori(user)
                                print("| Kategori berhasil ditambahkan!")
                                enter = input("| Klik Enter untuk melanjutkan... ")
                                core.clear()
                            case '2':
                                core.clear()
                                kategori.list_kategori()
                                enter = input("| Klik Enter untuk melanjutkan... ")
                            case '3':
                                kategori.list_kategori()
                                id = input("Masukkan ID data yang akan diperbarui: ")
                                data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                                if data == False:
                                    kategori.list_kategori()
                                    print("Data Tidak ada")
                                    enter  = input("Klik ENTER untuk meneruskan")
                                    core.clear()
                                else:
                                    print("Kategori lama :", data[0][1])
                                    kat_baru = input("Masukkan Kategori yang baru : ")
                                    kat = kat_baru if kat_baru else data[0][1]
                                    kategori.perbarui_baris_kategori(id, kat)
                                    print("Data telah diperbarui.")
                                    enter  = input("Klik ENTER untuk meneruskan")
                                    core.clear()
                            case '4':
                                kategori.list_kategori()
                                user = input("Pilih data yang akan dihapus: ")
                                kategori.hapus_kategori(user)
                                match user:
                                    case _:
                                        core.clear()
                                        print('Data tidak ada')
                                        continue
                            case '9':
                                core.clear()
                                mainmenu()
                            case '0':
                                core.clear()
                                exit()
                            case _:
                                core.clear()
                case '2':
                    while True:
                        core.clear()
                        with open('ui/kelola_buku.txt','r') as buku:
                            display = buku.read()
                            print(display)
                            pilihan = input("Pilihan : ")
                            match pilihan:
                                case '1':
                                    kelola_buku.tambah_buku()
                                    core.clear()
                                case '2':
                                    kelola_buku.dtframe_buku()
                                    enter = input('Klik ENTER untuk melanjutkan...')
                                    core.clear()
                                case '3':
                                    kelola_buku.update_buku()
                                    core.clear()
                                case '4':
                                    kelola_buku.hapus_buku()
                                    core.clear()
                                case '9':
                                    core.clear()
                                    mainmenu()
                                case '0':
                                    core.clear()
                                    exit()
                                case _:
                                    core.clear()
                case '3':
                    core.clear()
                    peminjaman.aksi_utama()
                    # while True:
                    #     core.clear()
                    #     with open('ui/kelola_peminjaman.txt','r') as ui:
                    #         display = ui.read()
                    #         print(display)
                    #     peminjaman = input('| > Pilih: ')
                    #     match peminjaman:
                    #         case '1':
                    #             core.clear()
                    #             data_peminjam.aksi_peminjam()
                    #         case '2':
                    #             core.clear()
                    #             peminjaman.aksi_utama()
                    #         case '9':
                    #             core.clear()
                    #             mainmenu()
                    #         case _:
                    #             continue
                case '4':
                    while True:
                        core.clear()
                        with open('ui/kelola_akun_admin.txt','r') as settings_admin :
                            display = settings_admin.read()
                            print(display)
                        pilihan = input('Masukkan pilihan: ')
                        if pilihan == '1':
                            pengaturan_admin.register()
                            core.clear()
                        elif pilihan == '2':
                            pengaturan_admin.list_data()
                        elif pilihan == '3':
                            id_to_delete = input('Masukkan ID admin yang akan dihapus: ')
                            pengaturan_admin.hapus_akun(id_to_delete)
                            core.clear()
                        elif pilihan == '9':
                            core.clear()
                            mainmenu()
                        elif pilihan == '0':
                            core.clear()
                            exit()
                        else:
                            core.clear()
                case '0':
                    print("Keluar dari program.")
                    exit()
                case _:
                    core.clear()
                    mainmenu()
if __name__ == "__main__":
    mainmenu()