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

def append_row(file_path, data_dict):

    # Leer el header real del archivo
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

    # Completar cualquier campo faltante con "0"
    complete_row = {field: data_dict.get(field, "0") for field in fieldnames}

    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(complete_row)