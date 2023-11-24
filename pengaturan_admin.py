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
            print('Username ini sudah ada!')
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
            print('Username ini sudah ada!')
            enter = input('Klik ENTER untuk melanjutkan')  
            return False
    
    id_baru = tambah_csv(username, password)
    print('+' + '='*39 + '+')
    print('|' + '[ NOTICE ]'.center(39) + '|')
    print('|' + f'Admin dengan ID {id_baru} berhasil ditambahkan'.center(38) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(39) + '|')
    print('+' + '='*39 + '+')
    enter = input()  

def list_data(cari_keyword="",halaman_sekarang=1,halaman_total=1):
    admin = core.baca_csv(user_file)
    halaman_limit = 5
    #masih belum digunakan karena search belum ada
    if len(cari_keyword) > 0:
        admin = core.cari_list(admin,cari_keyword,1)
        halaman_sekarang = 1
        
    data_admin = [['No','Username']]
    i = 1
    for baris in admin:
        if baris[0] == 'ID':
            continue
        username = baris[1]
        data_admin.append([i,username])
        i += 1
    data_admin,halaman_total = core.pagination(data_admin[1:],halaman_limit,halaman_sekarang)
    df = pd.DataFrame(data_admin, columns=['No','Username'])
    output = df.to_string(index=False)
    if len(data_admin) < 1:
        output = "* Data Kosong *"
        
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*35 + i + "\n"
    
    print(hasil)
    print('\n' , " "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_admin,halaman_sekarang,halaman_total

def hapus_akun(id_to_delete):
    data = core.baca_csv(user_file)
    nomor_urut = 0
    nomor = []
    for baris in data:
        if baris[0] != 'ID':
            nomor.append(baris)
            nomor_urut += 1

    if 1 <= id_to_delete <= len(nomor):
        print(f'ID: {nomor[id_to_delete - 1][0]}')
        print(f'Username: {nomor[id_to_delete - 1][1]}')   
        print(f'Password: {nomor[id_to_delete - 1][2]}')  
        user = input('Apakah anda ingin menghapus data diatas?(y/n) ')
        if user.lower() == 'y':
            data.remove(nomor[id_to_delete - 1])
            with open(user_file, 'w', newline="") as file:
                write = csv.writer(file)
                write.writerows(data)
                print('+' + '='*38 + '+')
                print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(38) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(38) + '|')
                print('+' + '='*38 + '+')
                enter  = input()
        else:
            print('+' + '='*38 + '+')
            print('|' + '[ DATA BATAL DIHAPUS ]'.center(38) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(38) + '|')
            print('+' + '='*38 + '+')
            enter  = input()


def aksi_pengaturan():
    cari_keyword = ''
    halaman_sekarang = 1
    halaman_total = 1
    while True:
        core.clear()
        with open('ui/kelola_akun_admin.txt','r') as settings_admin :
            display = settings_admin.read()
            print(display)
        pilihan = input('| Masukkan pilihan: ')
        if pilihan == '1':
            core.clear()
            register()
        elif pilihan == '2':
            while True:
                core.clear()
                print(" "*23 + '+' + '='*38 + '+')
                print(" "*23 + '|' + '[ DAFTAR AKUN ADMIN ]'.center(38) + '|')
                print(" "*23 + '+' + '='*38 + '+')
                data_admin,halaman_sekarang,halaman_total = list_data(cari_keyword,halaman_sekarang,halaman_total)
                if len(data_admin[1:]) < 1:
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    enter  = input()
                else:
                    with open('ui/page.txt','r') as page :
                        display = page.read()
                        print(display)
                    pilihan = input('| Pilihlah sesuai nomor diatas: ')
                    if pilihan == '1' and halaman_sekarang > 1:
                        halaman_sekarang -= 1
                    elif pilihan == '2' and halaman_sekarang < halaman_total:
                        halaman_sekarang += 1
                    elif pilihan == '9':
                        break
                    elif pilihan == '0':
                        exit()
                    else:
                        continue 
        elif pilihan == '3':
            while True:
                core.clear()
                print(" "*23 + '+' + '='*38 + '+')
                print(" "*23 + '|' + '[ DAFTAR AKUN ADMIN ]'.center(38) + '|')
                print(" "*23 + '+' + '='*38 + '+')
                list_data(cari_keyword,halaman_sekarang,halaman_total)
                with open('ui/page.txt','r') as page :
                        print(page.read())
                pilihan = input('| Pilihlah sesuai nomor diatas: ')
                if pilihan == '1' and halaman_sekarang > 1:
                    halaman_sekarang -= 1
                elif pilihan == '2' and halaman_sekarang < halaman_total:
                    halaman_sekarang += 1
                elif pilihan == '3':
                    user = input("\n| Pilih Nomor urut data yang akan dihapus: ")
                    if user.isdigit():
                        hapus_akun(int(user))
                    else:
                        print('+' + '='*38 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(38) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(38) + '|')
                        print('+' + '='*38 + '+')
                        enter  = input()
                elif pilihan == '9':
                    break
                elif pilihan == '0':
                    exit()
                else:
                    continue     
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