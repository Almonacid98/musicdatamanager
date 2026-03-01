def get_artist_album_info(artista, registros):
    albums = {}
    real_artist_name = None

    for registro in registros:
        artist_name = registro.get('Artist', '').strip()

        if artista.lower() in artist_name.lower():

            # Guardamos el nombre real la primera vez
            if real_artist_name is None:
                real_artist_name = artist_name

            album = registro.get('Album', 'Desconocido')
            duracion = int(float(registro.get('Duration_ms', 0)))

            if album not in albums:
                albums[album] = {
                    'canciones': 0,
                    'duracion_total': 0
                }

            albums[album]['canciones'] += 1
            albums[album]['duracion_total'] += duracion

    return real_artist_name, albums