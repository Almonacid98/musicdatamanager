import pathlib
from features.csv_manager import manager_csv
from utils.clear_console import clear_console
from utils.csv_utils import find_last_index, append_row
from utils.validators import (
    validate_spotify_url,
    validate_youtube_url,
    validate_spotify_uri,
    validate_duration,
    validate_likes_vs_views
)

#Agregar cancion manualmente
def add_song_manual(file_path):

    index = find_last_index(file_path)

    title = input("Título: ")
    artist = input("Artista: ")
    album = input("Álbum: ")
    spotify_url = input("URL Spotify: ")
    spotify_uri = input("URI Spotify: ")
    duration = input("Duración (ms): ")
    youtube_url = input("URL YouTube: ")
    likes = input("Likes: ")
    views = input("Views: ")

    if not validate_spotify_url(spotify_url):
        print("URL Spotify inválida")
        return

    if not validate_spotify_uri(spotify_uri):
        print("URI Spotify inválida")
        return

    if not validate_duration(duration):
        print("Duración inválida")
        return

    if not validate_youtube_url(youtube_url):
        print("URL YouTube inválida")
        return

    if not validate_likes_vs_views(likes, views):
        print("Likes no pueden ser mayores que Views")
        return

    new_song = {
        "Index": index,
        "Title": title,
        "Artist": artist,
        "Album": album,
        "Url_spotify": spotify_url,
        "Uri": spotify_uri,
        "Duration_ms": duration,
        "Url_youtube": youtube_url,
        "Likes": likes,
        "Views": views,
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
        "Channel": "0.0",
        "Comments": "0.0",
        "Licensed": "0.0",
        "Stream": "0.0",
        "official_video": "0.0",
    }

    append_row(file_path, new_song)
    print("Canción agregada correctamente")
    clear_console()



#Importar canciones desde otro CSV.

def add_songs_from_csv(csv_name):
    base = pathlib.Path(__file__).resolve().parents[1]
    data = base / "data"

    manager_csv(
        data / csv_name,
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
        new_csv = input("Ruta del CSV a importar: ").strip()
        add_songs_from_csv(new_csv)

    else:
        print("Opción inválida, no es un csv el archivo que se intenta importar.")

    input("\nPresione una tecla para volver al menú...")
    clear_console()