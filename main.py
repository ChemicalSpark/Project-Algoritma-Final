import login
import kategori
import kelola_buku
import peminjaman
import data_peminjam
import pengaturan_admin
import core

login.login()

def mainmenu():
    with open('ui/mainmenu.txt','r') as title:
        display = title.read()
        print(display)
        user = input("| > Menu: ")
        match user:
            case '1':
                kategori.aksi_kategori()
            case '2':
                kelola_buku.aksi_buku()
            case '3':
                peminjaman.aksi_peminjaman()
            case '4':
                data_peminjam.aksi_peminjam()
            case '5':
                pengaturan_admin.Pengaturan_Admin()
            case '6':
                print("Keluar dari program.")
                exit()
            case _:
                core.clear()
                mainmenu()
if __name__ == "__main__":
    mainmenu()