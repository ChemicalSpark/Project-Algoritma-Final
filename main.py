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
    while True:
        with open('ui/mainmenu.txt','r') as title:
            display = title.read()
            print(display)
            user = input("| > Menu: ")
            match user:
                case '1':
                    core.clear()
                    kategori.aksi_kategori()
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