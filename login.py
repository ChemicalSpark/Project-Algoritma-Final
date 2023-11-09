import core

user_file = ('database/user.csv')
data = core.baca_csv_sebagai_dict(user_file)

def ceklogin(user,pswd):
    for login in data:
        if login['username'] == user and login['password'] == pswd:
            return True
    return False

def getuser():
    user = input('Username : ')
    pswd = input("password : ")
    return user,pswd

def main():
    print('='*51+'\n','Selamat Datang di Aplikasi Manajemen Perpustakaan'+'\n'+'='*51+'\n')
    attemp = 3
    while attemp > 0:
        user, pswd = getuser()  
        if ceklogin(user, pswd):  
            print('Login Berhasil'+'\n')
            break
        else:
            print('Login Gagal'+'\n')
            attemp -= 1

        if attemp == 0:
            print('Percobaan Login Sudah Habis'+'\n')


if __name__ == '__main__':
    main()
