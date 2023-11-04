import os

user_file = 'Project-Algoritma-Final/database/user.csv'
if os.path.exists(user_file):
    with open (user_file, 'r') as file:
        data = [line.strip().split(',') for line in file.readlines()]
else:
    data = []

def tambah_csv(user,pswd):
    new_id = len(data) + 1
    new_rec = f"{new_id},{user},{pswd}"
    data.append(new_rec)

    with open(user_file, 'a') as file:
        file.write(new_rec+'\n')

    if len(pswd) < 8:
        return 'minimal 8 karakter!'
    
    lower = False
    upper = False
    number = False
    
    for i in range(len(pswd) - 1):
        if 'a' <= pswd[i] <= 'z':
            lower = True
        elif 'A' <= pswd[i] <= 'Z':
            upper = True
        elif '0' <= pswd[i] <= '9':
            number = True

    if 'a' <= pswd[-1] <= 'z':
        lower = True
    elif 'A' <= pswd[-1] <= 'Z':
        upper = True
    elif '0' <= pswd[-1] <= '9':
        number = True

    if upper and lower and number:
        return "password ini aman."
    else:
        return "password tidak sesuai kriteria!."

def register():
    user = input("Masukkan username: ")
    print('''
masukkan password yang berisi:
huruf kecil
huruf besar
angka
      ''')
    pswd = input("Masukkan password dengan 8 minimum digit: ")
    final = tambah_csv(user,pswd)
    print(final)

if register() == True:
    print('Berhasil membuat akun!')
else: 
    print('Gagal membuat akun')
