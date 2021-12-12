import sqlite3
from crud.read import buscar_cliente, buscar_admin
from crud.insert import insertar_cliente
from cliente import cliente_logueado
from admin import admin_logueado
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
    print("Seleccione la opcion de ingreso:")
    print("1. Ingresar con una cuenta ya registrada.")
    print("2. Crear una cuenta nueva.")
    opcion = input()

    if opcion == "1":
        print("Ingrese el documento del cliente")
        entrada = input()
        while not entrada.isdecimal():
            print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
            print("Intentelo nuevamente:")
        entrada = int(entrada)
        print("Validando informacion...")
        datos = buscar_cliente(cur, entrada)
        if datos is not None:
            cliente_logueado(con, cur, datos)
            con.close()
        else:
            print("Cliente no registrado. Verifique el numero de identificación")
            print("Volviendo al menu principal.")
            con.close()
            
    elif opcion == "2":
        cedula = input("Ingrese su numero de cedula: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo electronico: ")
        
        if cedula.isdecimal() and nombre.isalpha() and apellido.isalpha() and bool(correo):
            datos = [int(cedula), nombre, apellido, correo, None, None, None, None, None, 0]
            insertar_cliente(con, cur, datos)
            print("Cliente registrado satisfactoriamente")
            del cedula, nombre, apellido, correo
            cliente_logueado(con, cur, datos)
            con.close()
        else:
            print("Alguno de los datos se ingresaron incorrectamente.")
            print("Volviendo al menu principal.")
            con.close()
            
    else:
        print("Entrada incorrecta volviendo al menu principal.")
        con.close()


if __name__ == "__main__":

    print("╔" + "═"*32 + "╗")
    print("║ Bienvenido al Programa SpotyUN ║")
    print("╚" + "═"*32 + "╝\n")

    while True:
        print("Seleccione la opcion que desea realizar:")
        print("1. Ingresar como Administrador.")
        print("2. Ingresar como Cliente.")
        print("0. Salir del programa.")
        case = input()

        if case == "1":
            conexion_administrador()

        elif case == "2":
            conexion_cliente()
        
        elif case == "0":
            print("\nHasta Luego.")
            sleep(1)
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.\n")
