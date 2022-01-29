# Este archivo maneja las operaciones para la reproduccion del audio
from pygame import mixer  # Importa el reproductor de música del módulo Pygame
# from crud.read import buscar_cancion_especifica


def existencia(ruta_archivo):
    """
    Comprueba la existencia de un archivo en el sistema.
    
    Parametros:
    filePath (str): Direccion del archivo
    
    Regresa:
    True (bool): Si encuentra el archivo
    False (bool): Si NO encuentra el archivo, imprime el error.
    """
    try:
        with open(ruta_archivo, 'r'):
            return True
    except FileNotFoundError as e:
        print(e)
        return False
    except IOError as e:
        print(e)
        return False


def reproductor(cur, cancion):
    """
    Reproduce una cancion usando la funcion Mixer de la libreria Pygame

    Parametros:
    cur (sqlite3.Cursor): Necesario para cambiar de canción.
    canción (list): Datos de la canción
    """
    mixer.init()
    cancion_url = f"canciones/{cancion[2]}"

    # Verifica la existencia de la canción
    if existencia(cancion_url):
        print("Cargando canción...")
        mixer.music.load(cancion_url)
        mixer.music.set_volume(0.2)
        mixer.music.play()
        print(f"La cancion {cancion[1]} se esta reproduciendo.")

        # Bucle que maneja los controles de la canción
        while True:
            print("Pulsar 'P' para pausar")
            print("Pulsar 'R' para reproducir")
            # print("Pulsar 'E' para cambiar de canción")
            print("Pulsar 'S' para salir")

            opcion = input(">>> ")

            if opcion == "P" or opcion == "p":
                print(f"La cancion {cancion[1]} se encuentra pausada.")
                mixer.music.pause()

            elif opcion == "R" or opcion == "r":
                print(f"La cancion {cancion[1]} se esta reproduciendo.")
                mixer.music.unpause()

            # elif opcion == "E" or opcion == "e":
            #     mixer.music.stop()
            #     print("Escriba el numero de la cancion que quiere reproducir:")
            #     codigo = input()

            #     # Verificación del input
            #     if codigo.isdecimal():
            #         codigo = int(codigo)
            #         cancion = buscar_cancion_especifica(cur, codigo)  # Busca los datos en la BD
            #         cancion_url = f"canciones/{cancion[2]}"

            #         # Verifica nuevamente que la canción exista
            #         if existencia(cancion_url):
            #             print("Cargando canción...")
            #             mixer.music.load(cancion_url)
            #             mixer.music.set_volume(0.2)
            #             mixer.music.play()
            #             print(f"La cancion {cancion[1]} se esta reproduciendo.")
            #         else:
            #             print("No se encuentra la cancion.")
            #             break
            #     else:
            #         print("El valor que ingreso no es un numero.")
            #         break

            elif opcion == "S" or opcion == "s":
                mixer.music.stop()
                break
    else:
        print("No se encuentra la cancion. Accion no realizada.")
