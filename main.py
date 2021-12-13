import sqlite3

# from pygame.constants import CONTROLLER_BUTTON_DPAD_RIGHT
from crud.read import buscar_cliente, buscar_admin
from crud.insert import insertar_cliente
from cliente import cliente_logueado
from admin import admin_logueado, crear_base
from time import sleep


def conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    except sqlite3.Error:
        print(sqlite3.Error)


def conexion_administrador():
    con = conexion()
    cur = con.cursor()
    print("\nIngrese el documento del administrador")
    entrada = input()
    while not entrada.isdecimal():
        print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
        sleep(1)
        print("Intentelo nuevamente:")
        entrada = input()
    print("Validando informacion...")

    # Busca en la base de datos al administrador
    datos = buscar_admin(cur, int(entrada))
    if datos is not None:
        admin_logueado(con, cur, datos)
        sleep(1)
        con.close()
        del datos
    else:
        print("\nAdministrador no registrado, verifique el numero de identificación.")
        print("Volviendo al menu principal.\n")
        sleep(1)
        con.close()


def conexion_cliente():
    con = conexion()
    cur = con.cursor()
    print("\nSeleccione la opcion de ingreso:")
    print("1. Ingresar con una cuenta ya registrada.")
    print("2. Crear una cuenta nueva.")
    opcion = input()

    if opcion == "1":
        print("\nIngrese el documento del cliente")
        entrada = input()
        while not entrada.isdecimal():
            print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
            sleep(1)
            print("Intentelo nuevamente:")
            entrada = input()
        entrada = int(entrada)
        print("Validando informacion...")

        # Busca en la base de datos al cliente
        datos = buscar_cliente(cur, entrada)
        if datos is not None:
            cliente_logueado(con, cur, datos)
            con.close()
        else:
            print("\nCliente no registrado. Verifique el numero de identificación")
            print("Volviendo al menu principal.\n")
            con.close()
            
    elif opcion == "2":
        cedula = input("\nIngrese su numero de cedula: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo electronico: ")
        
        # Verficacion de datos en la entrada
        if cedula.isdecimal() and nombre.isalpha() and apellido.isalpha() and bool(correo):
            # Insercion del cliente en la base de datos
            datos = [int(cedula), nombre, apellido, correo, None, None, None, None, None, 0]
            insertar_cliente(con, cur, datos)

            print("Cliente registrado satisfactoriamente")
            del cedula, nombre, apellido, correo

            cliente_logueado(con, cur, datos)
            con.close()
        else:
            print("\nAlguno de los datos se ingresaron incorrectamente.")
            print("Volviendo al menu principal.\n")
            sleep(2)
            con.close()
            
    else:
        print("\nEntrada incorrecta volviendo al menu principal.\n")
        sleep(1)
        con.close()


if __name__ == "__main__":
    #TODO: Mejorar comentarios mas descriptivos
    #TODO: Mejorar presentacion del menu y tablas
    #TODO: Bloque logico si la base no esta creada

    print("╔" + "═"*32 + "╗")
    print("║ Bienvenido al Programa SpotyUN ║")
    print("╚" + "═"*32 + "╝\n")

    while True:
        print("Seleccione la opcion que desea realizar:")
        print("1. Ingresar como Administrador.")
        print("2. Ingresar como Cliente.")
        # TODO: Hotfix para crear una base rapido
        print("3. Crear base de datos.")
        print("0. Salir del programa.")
        case = input()

        if case == "1":
            conexion_administrador()

        elif case == "2":
            conexion_cliente()

        elif case == "3":
            con = conexion()
            cur = con.cursor()
            crear_base(con, cur)
            con.close()
        
        elif case == "0":
            print("\nHasta Luego.")
            sleep(1)
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.\n")
