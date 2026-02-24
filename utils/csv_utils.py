import csv


def find_last_index(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            indices = [
                int(row['Index'])
                for row in reader
                if row.get('Index', '').isdigit()
            ]
            return max(indices) + 1 if indices else 1
    except FileNotFoundError:
        return 1


def append_row(file_path, row):
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(row)