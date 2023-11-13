import csv
import core

def login():
    data_admin = []

    with open('database/data_admin.csv', 'r') as data:
        csvr = csv.reader(data, delimiter=',')

        for row in csvr:
            data_admin.append({"id": row[0], "username": row[1], "password": row[2]})

    attempts = 0
    login_session = False
    
    with open('ui/login.txt','r') as login_ui:
        display = login_ui.read()
        print(display)

    while attempts < 3 and not login_session:
        username = input("| Username: ")
        password = input("| Password: ")

        for user in data_admin:
            if username == user['username'] and password == user['password']:
                print('Login berhasil'+'\n')
                login_session = True
                core.clear()
                break
        if not login_session:
            print('Login Gagal'+'\n')
            attempts += 1
    if attempts == 3 and not login_session:
        print("Anda telah melebihi batas percobaan login.")
        exit()

if __name__ == "__main__":
    login()
