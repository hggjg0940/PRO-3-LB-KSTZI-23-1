import sqlite3
import hashlib
from getpass import getpass

DB_NAME = 'users.db'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(login, password, full_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (login, password, full_name) VALUES (?, ?, ?)',
                       (login, hash_password(password), full_name))
        conn.commit()
        print("Користувача додано успішно.")
    except sqlite3.IntegrityError:
        print("Користувач з таким логіном вже існує.")
    conn.close()

def update_password(login, new_password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET password = ? WHERE login = ?',
                   (hash_password(new_password), login))
    if cursor.rowcount == 0:
        print("Користувача не знайдено.")
    else:
        print("Пароль оновлено успішно.")
    conn.commit()
    conn.close()

def authenticate_user(login, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE login = ?', (login,))
    row = cursor.fetchone()
    conn.close()
    if row and row[0] == hash_password(password):
        print("Аутентифікація успішна.")
    else:
        print("Невірний логін або пароль.")

def main():
    create_database()
    while True:
        print("\n1. Додати користувача")
        print("2. Оновити пароль")
        print("3. Аутентифікація")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            login = input("Логін: ")
            password = getpass("Пароль: ")
            full_name = input("ПІБ: ")
            add_user(login, password, full_name)

        elif choice == '2':
            login = input("Логін: ")
            new_password = getpass("Новий пароль: ")
            update_password(login, new_password)

        elif choice == '3':
            login = input("Логін: ")
            password = getpass("Пароль: ")
            authenticate_user(login, password)

        elif choice == '4':
            print("Вихід...")
            break

        else:
            print("Невірний вибір.")

if __name__ == '__main__':
    main()
