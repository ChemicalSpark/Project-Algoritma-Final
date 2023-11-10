import pandas as pd
import login
import core
import kategori
import kelola_buku
import data_peminjam

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
#                 print("[PEMINJAMAN]")
#                 print("Menu: ") 
#                 print("""
# 1. Data Peminjam
# 2. Daftar Peminjaman
#                  """)
                with open('ui/data_peminjaman.txt','r') as title:
                    display = title.read()
                    print(display)
                    peminjaman = int(input("Pilihan: "))
                    match peminjaman:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            data_peminjam.aksi_peminjam()
                        case 4:
                            pass
                        case 5:
                            pass
                        case 9:
                            pass
                        case 0:
                            print("Keluar dari program.")
            case 4:
                pass
            case 5:
                print("Keluar dari program.")
            case _:
                mainmenu()
if __name__ == "__main__":
    mainmenu()