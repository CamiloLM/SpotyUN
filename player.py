# Este archivo maneja las operaciones para la reproduccion del audio
#la libreria pygame se instala en el simbolo del sistema ingresando el siguiente comando: py -m pip install -U pygame --user
from pygame import mixer    #importa la función mixer (reproductor) de la libreria Pygame
from crud.read import buscar_cancion_especifica

def existencia (filePath):  #función que comprueba la existencia del archivo .mp3 en el repositorio
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:  #Si no encuentra el archivo envia un False
        return False
    except IOError as e:    #Si no encuentra el archivo envia un False
        return False

def reproductor(cur, cancion):
    mixer.init()    #Inicia la función mixer de la libreria Pygame
    cancionUrl = f"canciones/{cancion[2]}"     #Busca la canción en el repositorio en base a su código
    if existencia(cancionUrl):
        print(f"La cancion {cancion[1]} se esta reproduciendo.")
        mixer.music.load(cancionUrl)   #carga la canción al mixer
        mixer.music.set_volume(0.2) 
        mixer.music.play()  #Reproduce la canción

        while True:
            print("Pulsar 'P' para pausar")
            print("Pulsar 'R' para reproducir")
            print("Pulsar 'E' para cambiar de canción")
            print("Pulsar 'S' para salir")

            opcion = input(">>> ")

            if opcion == "P" or opcion == "p":
                print(f"La cancion {cancion[1]} se encuentra pausada.")
                mixer.music.pause()

            elif opcion == "R" or opcion == "r":
                print(f"La cancion {cancion[1]} se esta reproduciendo.")
                mixer.music.unpause()
            
            elif opcion=="E" or opcion == "e":
                mixer.music.stop()
                print("Escriba el numero de la cancion que quiere reproducir:")
                codigo = input()
                if codigo.isdecimal():
                    codigo = int(codigo)
                    cancion = buscar_cancion_especifica(cur, codigo)
                    cancionUrl = f"canciones/{cancion[2]}"
                    if existencia(cancionUrl):
                        print(f"La cancion {cancion[1]} se esta reproduciendo.")
                        mixer.music.load(cancionUrl)
                        mixer.music.set_volume(0.2)
                        mixer.music.play()
                    else:
                        print("No se encuentra la cancion.")
                        break
                else:
                    print("El valor que ingreso no es un numero.")
                    break
                             
            elif opcion == "S" or opcion == "s":
                mixer.music.stop()
                break
    else:
        print("No se encuentra la cancion. Accion no realizada.")
