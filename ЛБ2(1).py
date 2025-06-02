def analyze_log_file(log_file_path):
    response_codes = {}

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) > 8:
                    code = parts[8]
                    if code.isdigit():
                        response_codes[code] = response_codes.get(code, 0) + 1

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка читання файлу '{log_file_path}'.")
    
    return response_codes
