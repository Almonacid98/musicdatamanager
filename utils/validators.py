import re

# SPOTIFY URL
# Acepta: spotify.com ,open.spotify.com ,www.open.spotify.com, con o sin http/https
# Si incluye /track/ valida ID de 22 caracteres
def validate_spotify_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?(www\.)?(open\.)?spotify\.com'
        r'(\/track\/[a-zA-Z0-9]{22}(\?.*)?)?$'
    )
    return pattern.match(url) is not None

# YOUTUBE URL
# Acepta: youtube.com ,www.youtube.com youtu.be, con o sin http/https
# Si incluye watch?v= valida ID de 11 caracteres
def validate_youtube_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?(www\.)?'
        r'(youtube\.com(\/watch\?v=[\w-]{11}(&.*)?)?|youtu\.be(\/[\w-]{11})?)$'
    )
    return pattern.match(url) is not None

# SPOTIFY URI debe ser exactamente spotify:track: + 22 caracteres sino es inválida
def validate_spotify_uri(uri):
    pattern = re.compile(r'^spotify:track:[a-zA-Z0-9]{22}$')
    return pattern.match(uri) is not None

#VALIDACIÓN DURACIÓN MANUAL
#Solo acepta: 3:15, 12:04, 01:03:45
def validate_duration_manual(duration):                                                             
    pattern = re.compile(r'^(\d{1,2}):([0-5]\d)(?::([0-5]\d))?$')       
    return pattern.match(str(duration).strip()) is not None


def validate_duration_csv(duration):                # VALIDACIÓN DURACIÓN CSV Solo acepta milisegundos (números)
    return str(duration).strip().isdigit()


def duration_to_ms(duration):   # CONVERTIR FORMATO HUMANO A MS
    parts = duration.split(":")

    try:
        if len(parts) == 2:  # MM:SS
            minutes, seconds = map(int, parts)
            total_seconds = minutes * 60 + seconds

        elif len(parts) == 3:  # HH:MM:SS
            hours, minutes, seconds = map(int, parts)
            total_seconds = hours * 3600 + minutes * 60 + seconds

        else:
            return None

        return total_seconds * 1000

    except ValueError:
        return None

def validate_likes_vs_views(likes, views):  # Likes <= Views
    try:
        return int(likes) <= int(views)
    except ValueError:
        return False