import login
import kategori
# import peminjaman
import kelola_buku
import data_peminjam
import pengaturan_admin
import core

core.clear()
# login.login()


def mainmenu():
    while True:
        core.clear()
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
                    data_peminjam.aksi_peminjam()
                case '4':
                    core.clear()
                    # peminjaman.aksi_utama()
                case '5':
                    pengaturan_admin.aksi_pengaturan()
                case '0':

                    print('+' + '='*83 + '+')
                    print('|' + '-'*37 + '[ NOTICE ]' + '-'*36 + '|')
                    print('|' + 'Apakah Anda yakin untuk keluar? (y/n)'.center(83) + '|')
                    print('+' + '='*83 + '+')
                    user = input(f"| > ")
                    if user.lower() == 'y' or 'yes':
                        core.clear()
                        exit()
                    else:
                        core.clear()
                        mainmenu()
                case _:
                    core.clear()
                    mainmenu()
if __name__ == "__main__":
    mainmenu()