from utils.csv_loader import load_songs
from utils.clear_console import clear_console
from service.artist_service import get_artist_album_info

def show_artist_info():
    artista = input("Ingrese el nombre del artista: ").strip()
    registros = load_songs()

    #nombre real + albums
    real_name, albums = get_artist_album_info(artista, registros)

    if not albums:
        print(f"No se encontraron álbumes para el artista '{artista}'.")
        input("Presiona una tecla para continuar...")
        clear_console()
        return

    print(f"\nArtista: {real_name}")
    print(f"Cantidad de álbumes: {len(albums)}\n")

    for album, info in albums.items():
        minutos = info['duracion_total'] // 60000
        segundos = (info['duracion_total'] % 60000) // 1000

        print(f"Álbum: {album}")
        print(f"  Canciones: {info['canciones']}")
        print(f"  Duración total: {minutos} minutos y {segundos} segundos")
        print("-" * 50)

    input("Presiona una tecla para continuar...")
    clear_console()