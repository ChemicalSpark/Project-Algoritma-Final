import csv
import pandas as pd
import core

user_file = "database/data_admin.csv"

def load_data():
    data = []
    with open(user_file, 'r') as file:
        csvr = csv.reader(file, delimiter=",")
        for row in csvr:
            data.append(row)
    return data

def save_data(data):
    with open(user_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def tambah_csv(username, password):
    data = load_data()
    
    if data:
        last_id = int(data[-1][0])
    else:
        last_id = 0

    id_baru = last_id + 1

    for row in data:
        ada_username = row[1]
        if username == ada_username:
            print('Username sudah ada!')
            return False

    data_baru = [str(id_baru), username, password]
    data.append(data_baru)

    save_data(data)

    return id_baru
def kriteria_password(password):
    if len(password) < 8:
        print('pasword minimal 8 karakter!')
        enter = input('Klik ENTER untuk melanjutkan') 
        return False
         
    lower = False
    upper = False
    number = False
    
    for i in range(len(password)):
        if 'a' <= password[i] <= 'z':
            lower = True
        elif 'A' <= password[i] <= 'Z':
            upper = True
        elif '0' <= password[i] <= '9':
            number = True

    if upper and lower and number:
        print("Password ini aman.") 
        return True
    else:
        print("Password tidak sesuai kriteria!.")
        enter = input('Klik ENTER untuk melanjutkan')  
        return False

def register():
    username = input('Masukkan username baru: ')
    if not username:
        print("Username tidak boleh kosong!")
        enter = input('Klik ENTER untuk melanjutkan') 
        return False 
    print('''
Masukkan password yang berisi:
- Minimal 8 karakter
- Setidaknya satu huruf kecil
- Setidaknya satu huruf besar
- Setidaknya satu angka
        ''')
    password = input('Masukkan password baru: ')
    if not password:
        print('Password tidak boleh kosong!')
        enter = input('Klik ENTER untuk melanjutkan')  
        return False

    pengecekan = kriteria_password(password)
    if pengecekan != True:
        print(pengecekan)
        return False

    data_admin = []

    with open("database/data_admin.csv", "r") as data:
        csvr = csv.reader(data, delimiter=",")
        for i in csvr:
            data_admin.append({"id": i[0], "username": i[1], "password": i[2]})

    for admin in data_admin:
        if username == admin['username']:
            print('Username sudah ada')
            enter = input('Klik ENTER untuk melanjutkan')  
            return False
    
    id_baru = tambah_csv(username, password)
    print('+' + '='*39 + '+')
    print('|' + '[ NOTICE ]'.center(39) + '|')
    print('|' + f'Admin dengan ID {id_baru} berhasil ditambahkan'.center(38) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(39) + '|')
    print('+' + '='*39 + '+')
    enter = input()  

def list_data():
    data_admin = load_data()
    df = pd.DataFrame(data_admin, columns=["ID", "Username", "Password"])
    print(df.to_string(index=False))


def hapus_akun(id_to_delete):
    data_admin = load_data()

    found = False
    for admin in data_admin:
        if admin[0] == id_to_delete:
            data_admin.remove(admin)
            found = True
            break

    if found:
        save_data(data_admin)
        print(f"Akun dengan ID {id_to_delete} berhasil dihapus.")
        enter = input('Klik ENTER untuk melanjutkan')
        core.clear()
    else:
        print(f"Akun dengan ID {id_to_delete} tidak ditemukan.")    
        enter = input('Klik ENTER untuk melanjutkan')
        core.clear()

def aksi_pengaturan():
    while True:
        core.clear()
        with open('ui/kelola_akun_admin.txt','r') as settings_admin :
            display = settings_admin.read()
            print(display)
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            register()
            core.clear()
        elif pilihan == '2':
            core.clear()
            print('+' + '='*36 + '+')
            print('|' + '-'*6 + '[ DAFTAR KATEGORI BUKU ]' + '-'*6 + '|')
            print('+' + '='*36 + '+')
            list_data()
            print('+' + '='*36 + '+')
            print('|' + '[ NOTICE ]'.center(36) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(36) + '|')
            print('+' + '='*36 + '+')
            enter = input()
        elif pilihan == '3':
            core.clear()
            print("Data saat ini:")
            list_data()
            id_to_delete = input('Masukkan ID admin yang akan dihapus: ')
            if id_to_delete:
                user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
                if user == 'y':
                    hapus_akun(id_to_delete)
                else:
                    print('Data batal dihapus')
                    enter  = input("Klik ENTER untuk meneruskan")
            else:
                print('+' + '='*36 + '+')
                print('|' + '[ DATA NOT FOUND ]'.center(36) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(36) + '|')
                print('+' + '='*36 + '+')
                enter  = input()
            
        elif pilihan == '9':
            core.clear()
            break
        elif pilihan == '0':
            core.clear()
            exit()
        else:
            core.clear()

if __name__ == "__main__":
    aksi_pengaturan()