import login
import kategori
# import kelola_buku
# import peminjaman
import data_peminjam
import pengaturan_admin
import core

core.clear()
login.login()

def mainmenu():
    with open('ui/mainmenu.txt','r') as title:
        display = title.read()
        print(display)
        user = input("| > Menu: ")
        match user:
            case '1':
                while True:
                    core.clear()
                    with open('ui/kategori.txt','r') as kategori:
                        display = kategori.read()
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
                        case '3':
                            id = input("Masukkan ID data yang akan diperbarui: ")
                            data = core.cari_id_list(core.baca_csv('database/kategori.csv'), id)
                            if data == False:
                                print("Data Tidak ada"+'\n')
                                core.clear()
                            else:
                                print("Kategori lama :", data[1])
                                kategori = input("Masukkan Kategori yang baru : ")
                                kategori.perbarui_baris_kategori(id, kategori)
                                print("Data telah diperbarui."+'\n')
                                core.clear()
                        case '4':
                            kategori.list_kategori()
                            user = input("Pilih data yang akan dihapus: ")
                            kategori.hapus_kategori(user)
                            print('\n')
                            core.clear()
                        case '9':
                            core.clear()
                            mainmenu()
                        case '0':
                            core.clear()
                            exit()
                        case _:
                            core.clear()
            case '2':
                core.clear()
                # kelola_buku.aksi_buku()
            case '3':
                while True:
                    core.clear()
                    with open('ui/kelola_peminjaman.txt','r') as ui:
                        display = ui.read()
                        print(display)
                    peminjaman = input('| > Pilih: ')
                    match peminjaman:
                        case '1':
                            core.clear()
                            data_peminjam.aksi_peminjam()
                        case '2':
                            pass
                        case '9':
                            core.clear()
                            mainmenu()
                        case _:
                            continue
                        
            case '4':
                core.clear()
                pengaturan_admin.Pengaturan_Admin()
            case '0':
                print("Keluar dari program.")
                exit()
            case _:
                core.clear()
                mainmenu()
if __name__ == "__main__":
    mainmenu()