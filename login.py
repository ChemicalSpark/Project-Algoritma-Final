import csv

def login():
    data_admin = []

    with open('data_admin.csv', 'r') as data:
        csvr = csv.reader(data, delimiter=',')

        for row in csvr:
            data_admin.append({"id": row[0], "username": row[1], "password": row[2]})

    attempts = 0

    print('='*51+'\n','Selamat Datang di Aplikasi Manajemen Perpustakaan'+'\n'+'='*51+'\n')
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")

        for user in data_admin:
            if username == user['username'] and password == user['password']:
                print('Login berhasil'+'\n')
                return

        print('Login Gagal'+'\n')
        attempts += 1

    print("Anda telah melebihi batas percobaan login.")

if __name__ == "__main__":
    login()