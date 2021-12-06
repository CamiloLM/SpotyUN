# Este archivo maneja las operaciones para la reproduccion del audio
#la libreria pygame se instala en el simbolo del sistema ingresando el siguiente comando: py -m pip install -U pygame --user
from pygame import mixer    #importa la función mixer (reproductor) de la libreria Pygame

def existencia (filePath):  #función que comprueba la existencia del archivo .mp3 en el repositorio
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:  #Si no encuentra el archivo envia un False
        return False
    except IOError as e:    #Si no encuentra el archivo envia un False
        return False

def reproductor(cancion):
    mixer.init()    #Inicia la función mixer de la libreria Pygame
    cancion="canciones/"+cancion+".mp3"     #Busca la canción en el repositorio en base a su código
    while existencia(cancion)==False:   
        cancion=input("Inserte un código valido: ")
        cancion="canciones/"+cancion+".mp3"
        if existencia(cancion)==True:
            break
    mixer.music.load(cancion)   #carga la canción al mixer
    mixer.music.set_volume(0.7) 
    mixer.music.play()  #Reproduce la canción

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