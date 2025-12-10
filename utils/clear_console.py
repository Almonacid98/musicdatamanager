import os

def clear_console():
    """Limpia la consola en Windows, Linux y macOS."""
    os.system('cls' if os.name == 'nt' else 'clear')
