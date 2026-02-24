def get_artist_album_info(artista, registros):
    albums = {}

    for registro in registros:
        if registro['Artist'].lower() == artista.lower():
            album = registro['Album']
            duracion = int(float(registro['Duration_ms']))

            if album not in albums:
                albums[album] = {
                    'canciones': 0,
                    'duracion_total': 0
                }

            albums[album]['canciones'] += 1
            albums[album]['duracion_total'] += duracion
    return albums