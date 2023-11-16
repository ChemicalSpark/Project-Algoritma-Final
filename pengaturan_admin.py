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
            print('Username sudah ada')
            return False

    data_baru = [str(id_baru), username, password]
    data.append(data_baru)

    save_data(data)

    return id_baru
def kriteria_password(password):
    if len(password) < 8:
        return 'pasword minimal 8 karakter!'
         
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
        return "Password ini aman."
    else:
        return "Password tidak sesuai kriteria."

def register():
    username = input('Masukkan username baru: ')
    print('''
Masukkan password yang berisi:
- Minimal 8 karakter
- Setidaknya satu huruf kecil
- Setidaknya satu huruf besar
- Setidaknya satu angka
        ''')
    password = input('Masukkan password baru: ')

    pengecekan = kriteria_password(password)
    if pengecekan != "Password ini aman.":
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
            enter = input('Klik enter untuk melanjutkan')  
            core.clear()
            return False

    id_baru = tambah_csv(username, password)
    print(f"User baru dengan ID {id_baru} berhasil terdaftar.")  
    enter = input('Klik enter untuk melanjutkan')  
    core.clear()




def list_data():
    data_admin = load_data()
    if data_admin:
        df = pd.DataFrame(data_admin, columns=["ID", "Username", "Password"])
        print(df.to_string(index=False))
        enter = input('Klik enter untuk melanjutkan')
        core.clear()
    else:
        print("Tidak ada data admin yang tersedia.")
        enter = input('Klik enter untuk melanjutkan')
        core.clear()


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
        enter = input('Klik enter untuk melanjutkan')
        core.clear()
    else:
        print(f"Akun dengan ID {id_to_delete} tidak ditemukan.")    
        enter = input('Klik enter untuk melanjutkan')
        core.clear()

def aksi_pengaturan():
    while True:
        with open('ui/kelola_akun_admin.txt','r') as settings_admin :
            display = settings_admin.read()
            print(display)
        pilihan = input('Masukkan pilihan: ')
        if pilihan == '1':
            register()
            core.clear()
        elif pilihan == '2':
            list_data()
        elif pilihan == '3':
            id_to_delete = input('Masukkan ID admin yang akan dihapus: ')
            hapus_akun(id_to_delete)
            core.clear()
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
    load_data()
    save_data()
    tambah_csv()
    kriteria_password()
    register()
    list_data()
    hapus_akun()

