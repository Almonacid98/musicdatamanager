import re


def validate_spotify_url(url):
    return re.match(r'^https://open.spotify.com/[a-zA-Z0-9/?=]+$', url) is not None


def validate_youtube_url(url):
    return re.match(r'^https:\/\/www\.youtube\.com\/watch\?v=[\w-]+$', url) is not None


def validate_spotify_uri(uri):
    return re.match(r'spotify:track:[a-zA-Z0-9]{22}', uri) is not None


def validate_duration(duration):
    return str(duration).isdigit()


def validate_likes_vs_views(likes, views):
    try:
        return int(likes) <= int(views)
    except ValueError:
        return False