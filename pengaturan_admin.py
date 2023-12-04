import csv
import core
import pandas as pd
import login

user_file = "database/data_admin.csv"

def tambah_csv(username, password, role):
    data = core.baca_csv(user_file)
    data_ada = []
    for cek in data[1:]:
        data_ada.append(cek[1])
        if username in data_ada:
            print('+' + '='*40 + '+')
            print('|' + '[ USERNAME INI SUDAH ADA ]'.center(40) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
            print('+' + '='*40 + '+')
            enter = input()
            return False
        if len(data) <= 1:
            id_baru = 1
        elif "" in data[len(data) - 1]:
            id_baru = int(data[len(data) - 1][0]) + 1
            data.remove(data[len(data) - 1])
        else:
            id_baru = int(data[len(data) - 1][0]) + 1

    data_baru = [id_baru, username, password, role]
    data.append(data_baru)

    core.tulis_csv(user_file,data)
    return id_baru

def kriteria_password(password):
    if len(password) < 8:
        print('Password minimal 8 karakter!')
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
        print("Password ini aman.\n") 
        return True
    else:
        print('+' + '='*39 + '+')
        print('|' + '[ NOTICE ]'.center(39) + '|')
        print('|' + f'Password tidak sesuai kriteria!'.center(39) + '|')
        print('|' + 'Klik ENTER untuk melanjutkan!'.center(39) + '|')
        print('+' + '='*39 + '+')  
        enter = input()  
        return False

def register():
    username = input('| Masukkan username baru: ').lower()
    if not username:
        print("| Username tidak boleh kosong!")
        enter = input('| Klik ENTER untuk melanjutkan') 
        return False 
    print('''
Masukkan password yang berisi:
- Minimal 8 karakter
- Setidaknya satu huruf kecil
- Setidaknya satu huruf besar
- Setidaknya satu angka
        ''')
    password = input('| Masukkan password: ')
    if not password:
        print('| Password tidak boleh kosong!')
        enter = input('| Klik ENTER untuk melanjutkan')  
        return False

    pengecekan = kriteria_password(password)
    if pengecekan != True:
        print(pengecekan)
        return False
    
    role = "admin"
    
    data_admin = []

    with open(user_file, "r") as data:
        csvr = csv.reader(data, delimiter=",")
        for i in csvr:
            data_admin.append({"id": i[0], "username": i[1], "password": i[2], "role": i[3]})

    for admin in data_admin:
        if username == admin['username']:
            print('+' + '='*39 + '+')
            print('|' + '[ NOTICE ]'.center(39) + '|')
            print('|' + f'Username ini sudah ada!'.center(39) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(39) + '|')
            print('+' + '='*39 + '+')  
            enter = input()
            return False
    
    id_baru = tambah_csv(username, password, role)
    print('+' + '='*39 + '+')
    print('|' + '[ NOTICE ]'.center(39) + '|')
    print('|' + f'Admin dengan ID {id_baru} berhasil ditambahkan'.center(38) + '|')
    print('|' + 'Klik ENTER untuk melanjutkan!'.center(39) + '|')
    print('+' + '='*39 + '+')
    enter = input()  

def list_data(cari_keyword="",halaman_sekarang=1,halaman_total=1):
    admin = core.baca_csv(user_file)[1:]
    halaman_limit = 10
    #masih belum digunakan karena search belum ada
    if len(cari_keyword) > 0:
        admin = core.cari_list(admin,cari_keyword,1)
        halaman_sekarang = 1
        
    data_admin = [['No','Username','Role']]
    i = 1
    for baris in admin:
        if baris[0] == 'ID':
            continue
        username = baris[1]
        role = baris[3]
        data_admin.append([i,username.title(),role.title()])
        i += 1
    data_admin,halaman_total = core.pagination(data_admin[1:],halaman_limit,halaman_sekarang)
    if len(data_admin) < 1:
        output = "* Data Kosong *"
        aksi_pengaturan()
    elif "" in admin[len(admin) - 1]:
        df = pd.DataFrame(data_admin[:len(data_admin) - 1], columns=['No','Username','Role'])
        output = df.to_string(index=False)
    else:
        df = pd.DataFrame(data_admin, columns=['No','Username','Role'])
        output = df.to_string(index=False)
    hasil = ""
    for i in output.split("\n"):
        hasil += " "*30 + i + "\n"
    
    print(hasil)
    print(" "*36 + f'page {halaman_sekarang} to {halaman_total}')
    return data_admin,halaman_sekarang,halaman_total

#fungsi untuk memperbarui 1 baris data peminjam
def perbarui_baris_peminjam(id, username, password):
    data = core.baca_csv(user_file)
    for baris in data:
        if baris[0] == id:
            baris[1] = username
            baris[2] = password
            break
    core.tulis_csv(user_file,data)

def hapus_akun(id_to_delete):
    data = core.baca_csv(user_file)
    nomor_urut = 0
    array = []
    for baris in data:
        if baris[0] != 'ID':
            array.append(baris)
            nomor_urut += 1

    if len(array) >= id_to_delete >= 1:
        print(f'| ID: {array[id_to_delete - 1][0]}')
        print(f'| Username: {array[id_to_delete - 1][1]}')     
        print(f'| Role: {array[id_to_delete - 1][3]}')
        user = input('| Apakah anda ingin menghapus akun diatas?(y/n): ')
        if user.lower() == 'y' and array[id_to_delete - 1][3] != "super admin":
            if id_to_delete == len(array):
                index_id = [array[len(array) - 1][0],"","",""]
                data.remove(array[id_to_delete - 1])
                data.append(index_id)
                core.tulis_csv(user_file,data)
            else:
                data.remove(array[id_to_delete - 1])
                core.tulis_csv(user_file,data)
            print('+' + '='*45 + '+')
            print('|' + '[ DATA BERHASIL DIHAPUS ]'.center(45) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(45) + '|')
            print('+' + '='*45 + '+')
            enter  = input()
        elif user.lower() == 'y' and array[id_to_delete - 1][3] == "super admin":
            print('+' + '='*45 + '+')
            print('|' + '[ AKUN SUPER ADMIN TIDAK BISA DIHAPUS! ]'.center(45) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(45) + '|')
            print('+' + '='*45 + '+')
            enter  = input()
        else:    
            print('+' + '='*45 + '+')
            print('|' + '[ AKUN BATAL DIHAPUS ]'.center(45) + '|')
            print('|' + 'Klik ENTER untuk melanjutkan!'.center(45) + '|')
            print('+' + '='*45 + '+')
            enter  = input()


def aksi_pengaturan():
    cari_keyword = ''
    halaman_sekarang = 1
    halaman_total = 1
    while True:
        core.clear()
        with open('ui/kelola_akun_admin.txt','r') as settings_admin :
            print(settings_admin.read())
        pilihan = input('| Masukkan pilihan: ')
        if pilihan == '1':
            sesi = login.SESSION_GLOBAL["role"] == "super admin"
            if sesi:
                core.clear()
                register()
            elif not sesi:
                print('+' + '='*40 + '+')
                print('|' + '[ AKUN TIDAK ADA ]'.center(40) + '|')
                print('|' + 'ATAU'.center(40) + '|')
                print('|' + '[ BUKAN AKUN SUPER ADMIN! ]'.center(40) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                print('+' + '='*40 + '+')
                enter = input()
        elif pilihan == '2':
            while True:
                core.clear()
                print(" "*23 + '+' + '='*38 + '+')
                print(" "*23 + '|' + '[ DAFTAR AKUN ADMIN ]'.center(38) + '|')
                print(" "*23 + '+' + '='*38 + '+')
                data_admin,halaman_sekarang,halaman_total = list_data(cari_keyword,halaman_sekarang,halaman_total)
                if len(data_admin) < 1:
                    print('+' + '='*60 + '+')
                    print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                    print('+' + '='*60 + '+')
                    enter  = input()
                else:
                    with open('ui/page_daftar.txt','r') as page :
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
            sesi = login.SESSION_GLOBAL["role"] == "super admin"
            if sesi:
                while True:
                    core.clear()
                    data_admin,halaman_sekarang,halaman_total = list_data(cari_keyword,halaman_sekarang,halaman_total)
                    if len(data_admin) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page.txt','r') as page:
                            print(page.read())
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == "1" and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == "2" and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == "3":
                            read_data = core.baca_csv(user_file)
                            nomor_urut = 0
                            array = []
                            for baris in read_data:
                                if baris[0] != 'ID':
                                    array.append(baris)
                                    nomor_urut += 1

                            update = input("| Masukkan Nomor urut data yang akan diperbarui: ")
                            if update.isdigit():
                                update = int(update)
                                if len(array) >= update >= 1:
                                    id = array[update - 1][0]
                                    data = core.cari_id_list(core.baca_csv(user_file),id)
                                    print("Username lama :", data[0][1])
                                    username_baru = input("Masukkan Username yang baru : ").lower()
                                    username = username_baru if username_baru else data[0][1]
                                    
                                    print("password lama :", data[0][2])
                                    print('''
Masukkan password baru yang berisi:
- Minimal 8 karakter
- Setidaknya satu huruf kecil
- Setidaknya satu huruf besar
- Setidaknya satu angka
                                    ''')
                                    password_baru = input("Masukkan Password yang baru : ")
                                    password = password_baru if password_baru else data[0][2]
                                    pengecekan = kriteria_password(password)
                                    if pengecekan != True:
                                        print(pengecekan)
                                        return pilihan

                                    perbarui_baris_peminjam(id, username, password)
                                    print('+' + '='*60 + '+') 
                                    print('|' + '[ NOTICE ]'.center(60) + '|')
                                    print('|' + 'Data Berhasil diperbaharui'.center(60) + '|')
                                    print('|' + 'Klik ENTER untuk meneruskan'.center(60) + '|')
                                    print('+' + '='*60 + '+')
                                    enter  = input()

                                else:
                                    print('+' + '='*60 + '+')
                                    print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                                    print('+' + '='*60 + '+')
                                    enter  = input()
                            else:
                                print('+' + '='*60 + '+')
                                print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                                print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                                print('+' + '='*60 + '+')
                                enter  = input()
                        elif pilihan == "9":
                            break
                        elif pilihan == '0':
                            exit
                        else:
                            continue
            elif not sesi:
                print('+' + '='*40 + '+')
                print('|' + '[ AKUN TIDAK ADA ]'.center(40) + '|')
                print('|' + 'ATAU'.center(40) + '|')
                print('|' + '[ BUKAN AKUN SUPER ADMIN! ]'.center(40) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                print('+' + '='*40 + '+')
                enter = input()
        elif pilihan == '4':
            sesi = login.SESSION_GLOBAL["role"] == "super admin"
            if sesi:
                while True:
                    core.clear()
                    print(" "*23 + '+' + '='*38 + '+')
                    print(" "*23 + '|' + '[ DAFTAR AKUN ADMIN ]'.center(38) + '|')
                    print(" "*23 + '+' + '='*38 + '+')
                    data_admin,halaman_sekarang,halaman_total = list_data(cari_keyword,halaman_sekarang,halaman_total)
                    if len(data_admin) < 1:
                        print('+' + '='*60 + '+')
                        print('|' + '[ DATA NOT FOUND ]'.center(60) + '|')
                        print('|' + 'Klik ENTER untuk melanjutkan!'.center(60) + '|')
                        print('+' + '='*60 + '+')
                        enter  = input()
                    else:
                        with open('ui/page.txt','r') as page :
                                print(page.read())
                        pilihan = input('| Pilihlah sesuai nomor diatas: ')
                        if pilihan == '1' and halaman_sekarang > 1:
                            halaman_sekarang -= 1
                        elif pilihan == '2' and halaman_sekarang < halaman_total:
                            halaman_sekarang += 1
                        elif pilihan == '3':
                                user = input("| Pilih Nomor urut data yang akan dihapus: ")
                                if user.isdigit():
                                    hapus_akun(int(user))
                                    continue
                                else:
                                    print('+' + '='*38 + '+')
                                    print('|' + '[ DATA NOT FOUND ]'.center(38) + '|')
                                    print('|' + 'Klik ENTER untuk melanjutkan!'.center(38) + '|')
                                    print('+' + '='*38 + '+')
                                    enter  = input()
                                    continue
                        elif pilihan == '9':
                            break
                        elif pilihan == '0':
                            exit()
                        else:
                            continue
            elif not sesi:
                print('+' + '='*40 + '+')
                print('|' + '[ AKUN TIDAK ADA ]'.center(40) + '|')
                print('|' + 'ATAU'.center(40) + '|')
                print('|' + '[ BUKAN AKUN SUPER ADMIN! ]'.center(40) + '|')
                print('|' + 'Klik ENTER untuk melanjutkan!'.center(40) + '|')
                print('+' + '='*40 + '+')
                enter = input()
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