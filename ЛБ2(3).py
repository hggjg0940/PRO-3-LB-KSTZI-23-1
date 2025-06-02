def filter_ips(input_file_path, output_file_path, allowed_ips):
    ip_counts = {}

    try:
        with open(input_file_path, 'r') as infile:
            for line in infile:
                parts = line.split()
                if parts:
                    ip = parts[0]
                    if ip in allowed_ips:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1

        try:
            with open(output_file_path, 'w') as outfile:
                for ip, count in ip_counts.items():
                    outfile.write(f"{ip} - {count}\n")
        except IOError:
            print(f"Помилка запису до файлу '{output_file_path}'.")

    except FileNotFoundError:
        print(f"Помилка: файл '{input_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка читання файлу '{input_file_path}'.")

    return ip_counts
