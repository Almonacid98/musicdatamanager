import csv
from utils.validators import (
    validate_spotify_url,
    validate_youtube_url,
    validate_spotify_uri,
    validate_duration_csv,
    validate_likes_vs_views
)

from utils.csv_utils import find_last_index, append_row


def manager_csv(new_path, main_path):

    imported = 0
    errors = 0
    row_number = 1  # para saber qué fila del CSV falla

    print("\n--- INICIANDO IMPORTACIÓN ---\n")

    with open(new_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        required_columns = [
            'Artist', 'Url_spotify', 'Track', 'Album',
            'Uri', 'Duration_ms', 'Url_youtube', 'Views', 'Likes'
        ]

        # Verificación de columnas obligatorias
        for col in required_columns:
            if col not in reader.fieldnames:
                print(f"Falta columna obligatoria: {col}")
                return

        for row in reader:
            row_number += 1
            row_errors = []

            # validación duración en ms
            duration_value = row['Duration_ms']

            if not validate_duration_csv(duration_value):
                row_errors.append(
                    f"Duración inválida (debe estar en ms): {duration_value}"
                )
            else:
                try:
                    duration_clean = int(float(duration_value))
                except:
                    row_errors.append(
                        f"Duración no convertible a entero: {duration_value}"
                    )

            # validación URL SPOTIFY
            if not validate_spotify_url(row['Url_spotify']):
                row_errors.append(
                    f"URL Spotify inválida: {row['Url_spotify']}"
                )

            # validación URI SPOTIFY
            if not validate_spotify_uri(row['Uri']):
                row_errors.append(
                    f"URI Spotify inválida: {row['Uri']}"
                )

            # validación YOUTUBE URL
            if not validate_youtube_url(row['Url_youtube']):
                row_errors.append(
                    f"URL YouTube inválida: {row['Url_youtube']}"
                )

            # validación Likes vs Views
            if not validate_likes_vs_views(row['Likes'], row['Views']):
                row_errors.append(
                    f"Likes ({row['Likes']}) no pueden ser mayores que Views ({row['Views']})"
                )

            # si existen errores en la fila, se reportan y se omite la importación de esa fila, pero el proceso continúa con las siguientes filas
            if row_errors:
                errors += 1
                print(f"\nError en fila {row_number}:")
                for err in row_errors:
                    print(f"   - {err}")
                continue

            # import_ok si todo está bien, se construye el diccionario final para agregar al CSV principal
            new_song = {
                "Index": find_last_index(main_path),
                "Artist": row['Artist'] or "0",
                "Url_spotify": row['Url_spotify'],
                "Track": row['Track'],
                "Album": row['Album'],
                "Album_type": "0",
                "Uri": row['Uri'],
                "Danceability": "0",
                "Energy": "0",
                "Key": "0",
                "Loudness": "0",
                "Speechiness": "0",
                "Acousticness": "0",
                "Instrumentalness": "0",
                "Liveness": "0",
                "Valence": "0",
                "Tempo": "0",
                "Duration_ms": duration_clean,
                "Url_youtube": row['Url_youtube'],
                "Title": "0",
                "Channel": "0",
                "Views": row['Views'],
                "Likes": row['Likes'],
                "Comments": "0",
                "Licensed": "0",
                "official_video": "0",
                "Stream": "0"
            }

            append_row(main_path, new_song)
            imported += 1
    print("\n|--- RESULTADO DE IMPORTACIÓN ---|")

    if imported == 0:
        print("No se pudo realizar la importación: todos los datos son erróneos")
    else:
        print(f"{imported} canciones agregadas correctamente")
        if errors > 0:
            print(f"{errors} filas no se pudieron importar por errores")