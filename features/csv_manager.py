import csv
from utils.validators import (
    validate_spotify_url,
    validate_youtube_url,
    validate_spotify_uri,
    validate_duration,
    validate_likes_vs_views
)

from utils.csv_utils import find_last_index, append_row


def manager_csv(new_path, main_path):

    imported = 0
    errors = 0

    with open(new_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        required_columns = [
            'Artist', 'Url_spotify', 'Track', 'Album',
            'Uri', 'Duration_ms', 'Url_youtube', 'Views', 'Likes'
        ]

        for col in required_columns:
            if col not in reader.fieldnames:
                print(f"Falta columna obligatoria: {col}")
                return

        for row in reader:
            new_song = {
                "Index": find_last_index(main_path),
                "Artist": row['Artist'],
                "Url_spotify": row['Url_spotify'],
                "Track": row['Track'],
                "Album": row['Album'],
                "Album_type": "0",
                "Uri": row['Uri'],
                "Danceability": "0.0",
                "Energy": "0.0",
                "Key": "0",
                "Loudness": "0.0",
                "Speechiness": "0.0",
                "Acousticness": "0.0",
                "Instrumentalness": "0.0",
                "Liveness": "0.0",
                "Valence": "0.0",
                "Tempo": "0.0",
                "Duration_ms": row['Duration_ms'],
                "Url_youtube": row['Url_youtube'],
                "Title": "0",
                "Channel": "0",
                "Views": row['Views'],
                "Likes": row['Likes'],
                "Comments": "0.0",
                "Licensed": "0.0",
                "official_video": "0.0",
                "Stream": "0.0",
            }

            # Validaciones
            if not validate_spotify_url(new_song["Url_spotify"]):
                print(f"URL Spotify inválida: {new_song['Url_spotify']}")
                errors += 1
                continue

            if not validate_spotify_uri(new_song["Uri"]):
                print(f"URI Spotify inválida: {new_song['Uri']}")
                errors += 1
                continue

            if not validate_duration(new_song["Duration_ms"]):
                print(f"Duración inválida: {new_song['Duration_ms']}")
                errors += 1
                continue

            if not validate_youtube_url(new_song["Url_youtube"]):
                print(f"URL YouTube inválida: {new_song['Url_youtube']}")
                errors += 1
                continue

            if not validate_likes_vs_views(new_song["Likes"], new_song["Views"]):
                print("Likes no pueden ser mayores que Views")
                errors += 1
                continue

            append_row(main_path, new_song)
            imported += 1

    if imported == 0:
        print("No se pudo realizar la importación: todos los datos son erróneos")
    else:
        print(f"Importación finalizada: {imported} canciones agregadas ({errors} con errores)")