from utils.csv_loader import load_songs
from utils.clear_console import clear_console
from utils.format_duration import format_duration
#Filtro por artista
def filter_songs_by_artist(songs, artist_name):
    result = []

    for song in songs:
        artist = song.get("Artist", "").strip()

        #coincidencia parcial e ignorando mayúsculas
        if artist_name.lower() in artist.lower():
            result.append(song)

    return result


def build_top_songs(songs):
    top_songs = []

    for song in songs:

        artist = song.get("Artist", "Unknown")
        track = song.get("Track", "Unknown")
        duration = format_duration(song.get("Duration_ms", 0))
        views = float(song.get("Views", 0) or 0)

        top_songs.append({
            "artist": artist,
            "track": track,
            "duration": duration,
            "views": views
        })

    return top_songs
#Orden de canciones por reproducciones (views) de mayor a menor
def sort_by_views(songs):
    return sorted(songs, key=lambda x: x["views"], reverse=True)

# Función principal para mostrar el Top 10 de canciones por artista

def show_top10_by_artist():
    artist_name = input("Ingrese el nombre del artista: ").strip()
    songs = load_songs()

    # 1. Filtra
    filtered = filter_songs_by_artist(songs, artist_name)

    if not filtered:
        print("\nNo se encontraron canciones para ese artista.")
        input("Presione una tecla para volver...")
        clear_console()
        return

    # 2. constructor
    top_songs = build_top_songs(filtered)

    # 3. orden
    top_songs = sort_by_views(top_songs)

    # 4. muestra por pantalla el top 10
    print(f"\nTop 10 temas de {artist_name} por reproducciones:\n")

    for i, song in enumerate(top_songs[:10], start=1):

        views_m = song["views"] / 1_000_000

        print(
            f"{i}. Artista: {song['artist']}, "
            f"Tema: {song['track']}, "
            f"Duración: {song['duration']}, "
            f"Reproducciones: {views_m:.2f} millones"
        )

    input("\nPresione una tecla para continuar...")
    clear_console()