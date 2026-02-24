import csv 
import re  
from datetime import timedelta  
import pathlib
from dataclasses import dataclass

@dataclass
class SongsDto:
    track: str
    artist: str
    album: str
    duration_ms: int
    views: int
    likes: int
    uri: str
    url: str
# Carga el csv y devuelve una lista de objetos SongsDto
def load_dataset(path: str = None) -> list:
        songs = []
        csv_path = (
        pathlib.Path(__file__).resolve().parent.parent 
        / "data" 
        / "spotify_and_youtube 2024.csv"
        )

        try:
            with open(csv_path, "r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    song = SongsDto(
                        track=row["Track"],
                        artist=row["Artist"],
                        album=row["Album"],
                        duration_ms=int(row["Duration_ms"]),
                        views=int(row["Views"]),
                        likes=int(row["Likes"]),
                        uri=row["Url_spotify"],
                        url=row["Url_youtube"]
                    )
                    songs.append(song)

            return songs

        except FileNotFoundError:
            print(f"[ERROR] Archivo no encontrado en: {csv_path}")
            exit(1)

        except Exception as e:
            print(f"[ERROR] No se pudo leer el archivo CSV: {e}")
            exit(1)
# Cargar canciones como diccionarios
def load_songs(file_path: str = None) -> list:

        songs = []

        # Si no se especifica un path, usa el archivo dentro de /data
        if file_path is None:
            file_path = (
            pathlib.Path(__file__).resolve().parent.parent 
            / "data" 
            / "spotify_and_youtube 2024.csv"
        )
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    songs.append(row)

            return songs

        except FileNotFoundError:
            print(f"[ERROR] El archivo '{file_path}' no fue encontrado.")
            return []

        except Exception as e:
            print(f"[ERROR] Error al cargar las canciones: {e}")
            return []

