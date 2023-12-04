#Sesi import
import csv
import core
import getpass
    
def superlogin():
        password = getpass.getpass(prompt='| Password Super Admin: ')
        # hidden_password = '*' * len(password)
        with open('database/data_admin.csv', 'r') as data:
            csvr = csv.reader(data, delimiter=',')
            for row in csvr:
                if row[2] == password and row[3] == "super admin":
                    return row
            return None

SESSION_GLOBAL = {}
        
        
def login():
    #Temp variabel
    data_admin = []
    
    # Membaca database data_admin
    with open('database/data_admin.csv', 'r') as data:
        csvr = csv.reader(data, delimiter=',')
        # Convert database csv ke dictionary
        for row in csvr:
            data_admin.append({"id": row[0], "username": row[1], "password": row[2], "role": row[3]})

    #Count kesempatan untuk login
    attempts = 3
    # -
    login_session = False
    
    # Main Program
    while attempts > 0 and not login_session:
        # Menampilkan UI CLI dari login session
        with open('ui/login.txt','r') as login_ui:
            display = login_ui.read()
            print(display)

        # Meminta input dari user berupa username dan password
        username = input("| Username: ")
        password = getpass.getpass(prompt="| Password: ")
        # Validasi input username dan password terhadap database
        for user in data_admin:
            # Kondisi benar jika input sesuai dengan database
            if username == user['username'] and password == user['password'] and user['role']:
                # UI Login Berhasil
                greeting = f"Selamat Datang {username.title()} dengan role {user['role'].title()}"
                print('+' + '='*83 + '+')
                print('|' + '[ LOGIN SUCCESFUL ]'.center(83) + '|')
                print('|' + greeting.center(83) + '|')
                print('+' + '='*83 + '+')
                # setelah masuk, sesi login true
                login_session = True
                global SESSION_GLOBAL
                SESSION_GLOBAL = user
                # Pause sebelum di clear
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()
                break
        # -
        if not login_session:
            # UI Login Gagal
            print('+' + '='*83 + '+')
            print('|' + '[ LOGIN FAILED ]'.center(83) + '|')
            print('|' + 'Username atau Password salah!'.center(83) + '|')
            print('+' + '='*83 + '+')
            attempts -= 1
            #  - 
            if attempts == 0 and not login_session:
                # UI Login gagal
                print('+' + '='*83 + '+')
                print('|' + '[ LOGIN SESSION ATTEMPT OUT ]'.center(83) + '|')
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
    superlogin()