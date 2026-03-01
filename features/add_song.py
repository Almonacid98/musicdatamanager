import pathlib
from pathlib import Path
from features.csv_manager import manager_csv
from utils.clear_console import clear_console
from utils.csv_utils import find_last_index, append_row
from utils.validators import (
    validate_spotify_url,
    validate_youtube_url,
    validate_spotify_uri,
    validate_duration_manual,
    duration_to_ms,
    validate_likes_vs_views
)

# metodo para agregar cancion de forma manual

def add_song_manual(file_path):

    index = find_last_index(file_path)

    print("\n|--- INGRESO MANUAL DE CANCIÓN ---|")
    title = input("Título: ").strip()# Título o track
    artist = input("Artista: ").strip()
    album = input("Álbum: ").strip()
    while True:
        spotify_url = input("URL Spotify: ").strip()
        if validate_spotify_url(spotify_url):
            break
        print("URL Spotify inválida. Intente nuevamente.")

    while True:
        spotify_uri = input("URI Spotify: ").strip()
        if validate_spotify_uri(spotify_uri):
            break
        print("URI Spotify inválida. Intente nuevamente.")

    while True:
        duration = input("Duración (MM:SS): ").strip()
        if not validate_duration_manual(duration):
            print("Duración inválida. Use formato MM:SS (ej: 3:15)")
            continue
        duration_ms = duration_to_ms(duration)
        if duration_ms is None:
            print("Error al convertir duración.")
            continue

        break

    while True:
        youtube_url = input("URL YouTube: ").strip()
        if validate_youtube_url(youtube_url):
            break
        print("URL YouTube inválida. Intente nuevamente.")

    while True:
        likes = input("Likes: ").strip()
        views = input("Views: ").strip()

        if not likes.isdigit() or not views.isdigit():
            print("Likes y Views deben ser números.")
            continue

        if not validate_likes_vs_views(likes, views):
            print("Likes no pueden ser mayores que Views.")
            continue

        break

    # Construcción del diccionario de la nueva canción con los datos ingresados, y valores por defecto para las columnas que no se solicitan en el ingreso manual
    new_song = {
        "Index": index,
        "Artist": artist,
        "Url_spotify": spotify_url,
        "Track": title,
        "Album": album,
        "Album_type": "0",
        "Uri": spotify_uri,
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
        "Duration_ms": int(duration_ms),
        "Url_youtube": youtube_url,
        "Title": "0",
        "Channel": "0",
        "Views": views,
        "Likes": likes,
        "Comments": "0",
        "Licensed": "0",
        "official_video": "0",
        "Stream": "0"
    }

    append_row(file_path, new_song)
    print("\nCanción agregada correctamente")
# método de importacion otro csv con validaciones, se omiten filas con errores pero el proceso continúa con las siguientes filas, al finalizar se muestra un resumen de cuántas canciones se agregaron correctamente y cuántas filas tuvieron errores
def add_songs_from_csv(csv_path):
    base = pathlib.Path(__file__).resolve().parents[1]
    data = base / "data"

    manager_csv(
        csv_path,
        data / "spotify_and_youtube 2024.csv"
    )


def option_add_song():
    base_path = pathlib.Path(__file__).resolve().parents[1]
    main_csv_path = base_path / "data" / "spotify_and_youtube 2024.csv"

    print("\n--- AGREGAR CANCIONES ---")
    print("1 - Agregar canción manual")
    print("2 - Importar desde CSV")

    choice = input("Seleccione una opción: ").strip()

    if choice == "1":
        add_song_manual(main_csv_path)

    elif choice == "2":
        new_csv = input("Nombre del CSV a importar: ").strip()

        if not new_csv.lower().endswith(".csv"):
            print("El archivo no tiene extensión .csv")
            input("Presione una tecla para continuar...")
            clear_console()
            return

        csv_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / new_csv
        )

        if not csv_path.exists():
            print("El archivo CSV no existe en la carpeta data.")
            input("Presione una tecla para continuar...")
            clear_console()
            return

        add_songs_from_csv(csv_path)

    else:
        print("Opción inválida")

    input("\nPresione una tecla para volver al menú...")
    clear_console()