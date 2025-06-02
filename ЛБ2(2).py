import hashlib

def generate_file_hashes(*file_paths):
    file_hashes = {}

    for path in file_paths:
        try:
            with open(path, 'rb') as file:
                file_data = file.read()
                hash_obj = hashlib.sha256(file_data)
                file_hashes[path] = hash_obj.hexdigest()
        except FileNotFoundError:
            print(f"Помилка: файл '{path}' не знайдено.")
        except IOError:
            print(f"Помилка читання файлу '{path}'.")

    return file_hashes
