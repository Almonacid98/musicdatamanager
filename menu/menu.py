from utils.colors import *
from features.search import perform_search
def menu():

    file_path = "data/spotify_and_youtube_2024.csv"
    #songs = load_songs(file_path)

    while True:
        print(f"\n{CYAN}========== MENÚ PRINCIPAL =========={RESET}")
        print(f"{YELLOW}1 - Buscar por título o artista{RESET}")
        print(f"{YELLOW}2 - Mostrar Top 10 con mayor popularidad (reproducciones) por artista{RESET}")
        print(f"{YELLOW}3 - Insertar registro{RESET}") 
        print(f"{YELLOW}4 - Información de artista{RESET}")
        print(f"{YELLOW}5 - Salir{RESET}")
        print(f"{CYAN}===================================={RESET}")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            perform_search()

        elif opcion == "2":
            pass

        elif opcion == "3":
            pass

        elif opcion == "4":
            pass 

        elif opcion == "5":
            print("Musicdatamanager finalizado...")
            break

        else:
            print("Opción inválida.")

