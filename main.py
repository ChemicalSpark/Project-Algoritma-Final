import pandas as pd
import login

login.main()

def mainmenu():
    with open('Project-Algoritma-Final/ui/title.txt','r') as title:
        display = title.read()
        print(display)
        user = int(input("| > Menu: "))
        match user:
            case 1:
                import kategori
            case 2:
                import kelola_buku
            case 3:
                print("[PEMINJAMAN]")
                print("Menu: ") 
                print("""
1. Data Peminjam
2. Daftar Peminjaman
                 """)
                peminjam = int(input("Pilihan: "))
                match peminjam:
                     case 1:
                        import data_peminjam
                     case 2:
                        pass
            case 4:
                pass
            case 5:
                print("Keluar dari program.")
            case _:
                mainmenu()
        
    
mainmenu()