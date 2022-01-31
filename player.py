# Este archivo maneja las operaciones para la reproduccion del audio
from pygame import mixer  # Importa el reproductor de música del módulo Pygame


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


def reproductor(lista_canciones):
    """
    Reproduce una cancion usando la funcion Mixer de la libreria Pygame.

    Parametros:
    lista_canciones (list): Lista con los datos de la canciones.
    """
    mixer.init()  # Inicia el reproductor
    i = 0  # Variable para moverse entre la lista de canciones
    cargada = False  # Determina si hay una cancion activa en el reproductor
    while True:
        if not cargada:
            mixer.music.load(f"assets/canciones/{lista_canciones[i][2]}")  # Carga cancion al reproductor
            mixer.music.set_volume(0.2)  # Establece el volumen
            mixer.music.play()  # La cancion se empieza a reproducir
            cargada = True

        print(f"\nLa canción {lista_canciones[i][1]} esta seleccionada.")
        print("Pulsar 'R' para reproducir")
        print("Pulsar 'P' para pausar")
        print("Pulsar 'N' para cambiar a la siguiente canción")
        print("Pulsar 'B' para cambiar a la canción anterior")
        print("Pulsar 'S' para salir")

        opcion = input(">>> ")

        if opcion == "P" or opcion == "p":
            mixer.music.pause()  # Pausa la cancion

        elif opcion == "R" or opcion == "r":
            mixer.music.unpause()  # Despausa la cancion

        elif opcion == "N" or opcion == "n":
            # Verifica que no se sale del rango de la lista
            if i < len(lista_canciones)-1:
                mixer.music.stop()  # Para la cancion y descarga la cancion
                i += 1  # Pasa a la siguiente
                cargada = False
            else:
                print("\nEsta es la ultima canción de la lista")

        elif opcion == "B" or opcion == "b":
            # Verifica que no se sale del rango de la lista
            if i > 0:
                mixer.music.stop()  # Para la cancion y descarga la cancion
                i -= 1  # Pasa a la anterior
                cargada = False
            else:
                print("\nEsta es la primera canción de la lista")

        elif opcion == "S" or opcion == "s":
            mixer.music.stop()  # Para la cancion y descarga la cancion
            break
