import hashlibAdd commentMore actions

users = {
    "admin": {
        "password": hashlib.md5("admin123".encode()).hexdigest(),
        "name": "Адмін Системи"
    },
    "vlad": {
        "password": hashlib.md5("qwerty".encode()).hexdigest(),
        "name": "Слізченко Володимир Дмитрович"
    }
}

def login():
    username = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if username in users:
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == users[username]["password"]:
            print(f"Вітаю, {users[username]['name']}!")
        else:
            print("Невірний пароль!")
    else:
        print("Користувача не знайдено!")