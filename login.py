#Sesi import
import csv
import core

def login():
    #Temp variabel
    data_admin = []
    
    # Membaca database data_admin
    with open('database/data_admin.csv', 'r') as data:
        csvr = csv.reader(data, delimiter=',')
        # Convert database csv ke dictionary
        for row in csvr:
            data_admin.append({"id": row[0], "username": row[1], "password": row[2]})

    #Count kesempatan untuk login
    attempts = 0
    # -
    login_session = False
    
    # Main Program
    while attempts < 3 and not login_session:
        # Menampilkan UI CLI dari login session
        with open('ui/login.txt','r') as login_ui:
            display = login_ui.read()
            print(display)

        # Meminta input dari user berupa username dan password
        username = input("| Username: ")
        password = input("| Password: ")

        # Validasi input username dan password terhadap database
        for user in data_admin:
            # Kondisi benar jika input sesuai dengan database
            if username == user['username'] and password == user['password']:
                # UI Login Berhasil
                greeting = f"Selamat Datang Admin {username.title()}"
                print('+' + '='*83 + '+')
                print('|' + '-'*32 + '[ LOGIN SUCCESFUL ]' + '-'*32 + '|')
                print('|' + greeting.center(83) + '|')
                print('+' + '='*83 + '+')
                # -
                login_session = True
                # Pause sebelum di clear
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()
                break
        # -
        if not login_session:
            # UI Login Gagal
            print('+' + '='*83 + '+')
            print('|' + '-'*33 + '[ LOGIN FAILED ]' + '-'*34 + '|')
            print('|' + 'Username atau Password salah!'.center(83) + '|')
            print('+' + '='*83 + '+')
            attempts += 1
            #  - 
            if attempts == 3 and not login_session:
                # UI Login gagal
                print('+' + '='*83 + '+')
                print('|' + '-'*27 + '[ LOGIN SESSION ATTEMPT OUT ]' + '-'*27 + '|')
                print('|' + 'Anda telah melebihi batas percobaan login, Silahkan jalankan ulang program!'.center(83) + '|')
                print('+' + '='*83 + '+')
                # Keluar dari program
                exit()
            # Melanjutkan percobaan login
            else:
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()

# -
if __name__ == "__main__":
    login()