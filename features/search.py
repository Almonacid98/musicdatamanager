from utils.csv_loader import load_songs
from utils.clear_console import clear_console
from datetime import timedelta


def search_song_by_title_or_artist(query, songs):
    """
    Devuelve canciones que coincidan con el artista o título.
    """
    matches = []

    for song in songs:
        artist = song.get("Artist", "")
        title = song.get("Track", "")

        if query.lower() in artist.lower() or query.lower() in title.lower():
            matches.append(song)

    # función auxiliar ordenar por Stream
    def get_stream_value(song):
        try:
            return int(float(song.get("Stream", 0)))
        except:
            return 0

    matches.sort(key=get_stream_value, reverse=True)
    return matches


# -------------------------------------------------------
# Convertir milisegundos a formato HH:MM:SS
# -------------------------------------------------------
def format_duration(ms):
    """Convierte milisegundos a formato HH:MM:SS."""
    try:
        ms = int(float(ms))  # FIX → permite "222640.0"
        duration = timedelta(milliseconds=ms)

        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02}:{minutes:02}:{seconds:02}"

    except Exception:
        return "00:00:00"


def perform_search():
    query = input("Ingrese el título o artista a buscar: ")

    songs = load_songs()      # lista de diccionarios
    results = search_song_by_title_or_artist(query, songs)

    if not results:
        print("\nNo se encontraron coincidencias.")
        input("Presiona cualquier tecla para volver al menú...")  
        clear_console()
        return

    print("\nResultados:\n")

    for song in results:
        duration = format_duration(song["Duration_ms"])  

        print(
            f"Artista: {song['Artist']}, "
            f"Título: {song['Track']}, "
            f"Duración: {duration}"
        )
    input("Presiona cualquier tecla para volver al menú...")  
    clear_console()