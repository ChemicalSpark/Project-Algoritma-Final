import login
import kategori
import kelola_buku
# import peminjaman
# import data_peminjam
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
                core.clear()
                kategori.aksi_kategori()
            case '2':
                core.clear()
                kelola_buku.aksi_buku()
            case '3':
                pass
                # core.clear()
                # peminjaman.aksi_peminjaman()
            case '4':
                pass
                # core.clear()
                # data_peminjam.aksi_peminjam()
            case '5':
                core.clear()
                pengaturan_admin.Pengaturan_Admin()
            case '6':
                print("Keluar dari program.")
                exit()
            case _:
                core.clear()
                mainmenu()
if __name__ == "__main__":
    mainmenu()