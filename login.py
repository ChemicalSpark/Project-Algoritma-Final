#Sesi import
import core
import getpass
    

SESSION_GLOBAL = {}
   
user_file = 'database/data_admin.csv'
        
def login():
    #Temp variabel
    data_admin = []
    # Membaca database data_admin
    data = core.baca_csv(user_file)
    # Convert database csv ke dictionary
    for i in data:
        data_admin.append({"id": i[0], "username": i[1], "password": i[2], "role": i[3]})

    #Count kesempatan untuk login
    percobaan = 3
    sesi_login = False
    
    # Main Program
    while percobaan > 0 and not sesi_login:
        # Menampilkan UI CLI dari login session
        with open('ui/login.txt','r') as login_ui:
            print(login_ui.read())
        # Meminta input dari user berupa username dan password
        username = input("| Username: ")
        password = getpass.getpass(prompt="| Password: ")
        # Validasi input username dan password terhadap database
        for user in data_admin:
            # Kondisi benar jika input sesuai dengan database
            if username == user['username'] and password == user['password'] and user['role']:
                # UI Login Berhasil
                salam = f"Selamat Datang {username.title()} dengan role {user['role'].title()}"
                print('+' + '='*83 + '+')
                print('|' + '[ LOGIN SUCCESFUL ]'.center(83) + '|')
                print('|' + salam.center(83) + '|')
                print('+' + '='*83 + '+')
                # setelah masuk, sesi login true
                sesi_login = True
                global SESSION_GLOBAL
                SESSION_GLOBAL = user
                # Pause sebelum di clear
                req = input("| Klik ENTER untuk melanjutkan... ")
                core.clear()
                break
        # -
        if not sesi_login:
            # UI Login Gagal
            print('+' + '='*83 + '+')
            print('|' + '[ LOGIN FAILED ]'.center(83) + '|')
            print('|' + 'Username atau Password salah!'.center(83) + '|')
            print('+' + '='*83 + '+')
            percobaan -= 1
            #  - 
            if percobaan == 0 and not sesi_login:
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
