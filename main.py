import login
import kategori
import kelola_buku
import peminjaman
import data_peminjam
import pengaturan_admin

login.login()

def mainmenu():
    with open('ui/mainmenu.txt','r') as title:
        display = title.read()
        print(display)
        user = int(input("| > Menu: "))
        match user:
            case 1:
                with open('ui/kategori.txt','r') as title:
                    display = title.read()
                    print(display)
                    kategori.aksi_kategori()
            case 2:
               with open('ui/kelola_buku.txt','r') as title:
                    display = title.read()
                    print(display)
                    kelola_buku.aksi_buku()
            case 3:
                with open('ui/data_peminjaman.txt','r') as title:
                    display = title.read()
                    print(display)
                    peminjaman.aksi_peminjaman

            case 4:
                with open('ui/data_peminjam.txt','r') as title:
                    display = title.read()
                    print(display)
                    data_peminjam.aksi_peminjam()
            case 5:
                pengaturan_admin.Pengaturan_Admin()
            case 6:
                print("Keluar dari program.")
                exit()
            case _:
                mainmenu()
if __name__ == "__main__":
    mainmenu()