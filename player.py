# Este archivo maneja las operaciones para la reproduccion del audio
from pygame import mixer

def existencia (filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def reproductor(cancion):
    mixer.init()
    cancion="canciones/"+cancion+".mp3"
    while existencia(cancion)==False:
        cancion=input("Inserte un código valido: ")
        cancion="canciones/"+cancion+".mp3"
        if existencia(cancion)==True:
            break
    mixer.music.load(cancion)
    mixer.music.set_volume(0.7)
    mixer.music.play()

    while True:
        print("Pulsar 'P' para pausar")
        print("Pulsar 'R' para reproducir")
        print("Pulsar 'E' para cambiar de canción")
        print("Pulsar 'S' para salir")

        opcion=input(">>> ")

        if opcion=="P":
            mixer.music.pause()
        elif opcion=="R":
            mixer.music.unpause()
        elif opcion=="E":
            mixer.music.stop()
            cancion=str(input("Código de la canción: "))
            cancion="canciones/"+cancion+".mp3"
            while existencia(cancion)==False:
                cancion=input("Inserte un código valido: ")
                cancion="canciones/"+cancion+".mp3"
                if existencia(cancion)==True:
                    break
            mixer.music.load(cancion)
            mixer.music.set_volume(0.7)
            mixer.music.play() 
        elif opcion=="S":
            mixer.music.stop()
            break