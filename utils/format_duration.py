from datetime import timedelta

def format_duration(ms):
    try:
        ms = int(float(ms))
        duration = timedelta(milliseconds=ms)

        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02}:{minutes:02}:{seconds:02}"
    except:
        return "00:00:00"