def get_artist_album_info(artista, registros):
    albums = {}

    for registro in registros:
        artist_name = registro.get('Artist', '').strip()

        #Coincidencia parcial e ignorando mayúsculas
        if artista.lower() in artist_name.lower():

            album = registro.get('Album', 'Desconocido')
            duracion = int(float(registro.get('Duration_ms', 0)))

            if album not in albums:
                albums[album] = {
                    'canciones': 0,
                    'duracion_total': 0
                }

            albums[album]['canciones'] += 1
            albums[album]['duracion_total'] += duracion

    return albums