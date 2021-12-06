import sqlite3
from crud import buscar_cliente, insertar_cliente
from time import sleep
from player import reproductor


def conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        con.execute("PRAGMA foreign_keys = 1")
        return con
    except sqlite3.Error:
        print(sqlite3.Error)


def conexion_administrador():
    # con = conexion()
    # cur = con.cursor()
    print("Ingrese el documento del administrador")
    entrada = input()
    while not entrada.isdecimal():
        print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
        print("Intentelo nuevamente:")
    entrada = input()
    entrada = int(entrada)
    print("Validando informacion...")
    datos = []
    if datos is not None:
        # Iniciar sesion de administrador
        pass
    else:
        print("Administrador no registrado. Verifique el numero de identificación")
        print("Volviendo al menu principal.")


def conexion_cliente():
    con = conexion()
    cur = con.cursor()
    print("Seleccione la opcion de ingreso:")
    print("\t1. Ingresar con una cuenta ya registrada.")
    print("\t2. Crear una cuenta nueva.")
    opcion = input()

    if opcion == "1":
        print("Ingrese el documento del cliente")
        entrada = input()
        while not entrada.isdecimal():
            print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
            print("Intentelo nuevamente:")
        entrada = input()
        entrada = int(entrada)
        print("Validando informacion...")
        datos = buscar_cliente(cur, entrada)
        if datos is not None:
            # Iniciar sesion de cliente
            pass
        else:
            print("Cliente no registrado. Verifique el numero de identificación")
            print("Volviendo al menu principal.")
            
    elif opcion == "2":
        datos = []
        cedula = input("Ingrese su numero de cedula: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo: ")
        
        print(correo)
        if cedula.isdecimal() and nombre.isalpha() and apellido.isalpha() and bool(correo):
            datos.extend([int(cedula), nombre, apellido, correo, None, None, None, None, None, 0])
            insertar_cliente(con, cur, datos)
            print("Cliente registrado satisfactoriamente")
            del cedula, nombre, apellido, correo
            # Iniciar Sesion Cliente
        else:
            print("Alguno de los datos se ingresaron incorrectamente.")
            print("Volviendo al menu principal.")
            
    else:
        print("Entrada incorrecta volviendo al menu principal.")


if __name__ == "__main__":

    print("╔" + "═"*32 + "╗")
    print("║ Bienvenido al Programa SpotyUN ║")
    print("╚" + "═"*32 + "╝\n")

    while True:
        print("Seleccione la opcion que desea realizar:")
        print("\t1. Ingresar como Administrador.")
        print("\t2. Ingresar como Cliente.")
        print("\t3. Salir del programa.")
        case = input()

        if case == "1":
            conexion_administrador()

        elif case == "2":
            conexion_cliente()
        
        elif case == "3":
            print("Hasta Luego.")
            sleep(1)
            break

        else:
            print("Entrada incorrecta. Intente otra vez.")
    codcan=input("Código de la canción: ")
    reproductor(codcan)
