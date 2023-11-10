import csv

def login():
    data_admin = []

    with open('database/user.csv', 'r') as data:
        csvr = csv.reader(data, delimiter=',')

        for row in csvr:
            data_admin.append({"id": row[0], "username": row[1], "password": row[2]})

    attempts = 0
    login_session = False

    print('='*51+'\n','Selamat Datang di Aplikasi Manajemen Perpustakaan'+'\n'+'='*51+'\n')
    while attempts < 3 and not login_session:
        username = input("Username: ")
        password = input("Password: ")

        for user in data_admin:
            if username == user['username'] and password == user['password']:
                print('Login berhasil'+'\n')
                login_session = True
                break
        if not login_session:
            print('Login Gagal'+'\n')
            attempts += 1
    if attempts == 3 and not login_session:
        print("Anda telah melebihi batas percobaan login.")
        exit()

if __name__ == "__main__":
    login()
