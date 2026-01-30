from utils.csv_loader import load_songs
from utils.clear_console import clear_console
from utils.format_duration import format_duration

def filter_songs_by_artist(songs, artist_name):
    """Filtra canciones por artista."""
    result = []

    for song in songs:
        if song.get("Artist", "").strip().lower() == artist_name.lower():
            result.append(song)

    return result


def build_top_songs(songs, artist_name):
    """Construye la lista con datos"""

    top_songs = []
    for song in songs:

        track = song.get("Track", "Unknown")
        duration = format_duration(song.get("Duration_ms", 0))
        views = float(song.get("Views", 0) or 0)

        top_songs.append({
            "artist": artist_name,
            "track": track,
            "duration": duration,
            "views": views
        })

    return top_songs


def sort_by_views(songs):
    """Ordena canciones por reproducciones."""
    return sorted(songs, key=lambda x: x["views"], reverse=True)

# Función (la que llama el menú)

def show_top10_by_artist():
    """Muestra el Top 10 de canciones por artista."""

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
    top_songs = build_top_songs(filtered, artist_name)

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