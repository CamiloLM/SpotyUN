import sqlite3  # Modulo para realizar operaciones a la base de datos
from crud.read import buscar_cliente, buscar_admin  # Funciones para comprobar los datos ingresados.
from crud.insert import agregar_subscripcion, insertar_cliente  # Función para agregar un nuevo cliente.
from cliente import cliente_logueado  # Función que controla las funcionalidades del cliente.
from admin import admin_logueado, crear_base  # Funciones para controlar al administrador y la creación de la BD.
from time import sleep  # Funcion estetica para controlar el comportamiento de la consola.


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        return sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.


def conexion_administrador(con, cur):
    """
        Determina si los datos ingresados coinciden con algun registro en la base de datos.
        Si los datos son correctos se crea una conexión con los datos del administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """

    print("\nIngrese el documento del administrador")
    entrada = input()

    # Verifica que los datos que se ingresan son correctos y no causaran un error.
    while not entrada.isdecimal():
        print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
        sleep(1)
        print("Intentelo nuevamente:")
        entrada = input()
    print("Validando informacion...")

    # Confirma que los datos ingresados coinciden con un registro en la tabla de administrador.
    datos = buscar_admin(cur, int(entrada))
    if datos is not None:
        admin_logueado(con, cur, datos)  # Si encuentra una coincidencia llama a la función controladora.
        # Cuando la conexión con el administrador termina se borran los datos locales y se cierra la base de datos.
        sleep(1)
        con.close()
        del datos
    else:
        print("\nAdministrador no registrado, verifique el numero de identificación.")
        print("Volviendo al menu principal.\n")
        # Cierra la conexion a la base de datos.
        sleep(1)
        con.close()


def conexion_cliente(con, cur):
    """
        Determina si los datos ingresados coinciden con algun registro en la base de datos.
        Si los datos son correctos se crea una conexión con los datos del cliente, tambien se pueden ingresar
        los datos de un nuevo cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """

    print("\nSeleccione la opcion de ingreso:")
    print("1. Ingresar con una cuenta ya registrada.")
    print("2. Crear una cuenta nueva.")
    opcion = input()

    if opcion == "1":
        print("\nIngrese el documento del cliente")
        entrada = input()

        # Verifica que los datos que se ingresan son correctos y no causaran un error.
        while not entrada.isdecimal():
            print("Su entrada es incorrecta. Solo ingrese numeros sin puntos ni comas.")
            sleep(1)
            print("Intentelo nuevamente:")
            entrada = input()
        entrada = int(entrada)
        print("Validando informacion...")

        # Confirma que los datos ingresados coinciden con un registro en la tabla de clientes.
        datos_cliente = buscar_cliente(cur, entrada)
        if datos_cliente is not None:
            cliente_logueado(con, cur, datos_cliente)  # Si encuentra una coincidencia llama a la función controladora.
            # Cuando la conexión con el cliente termina se borran los datos locales y se cierra la base de datos.
            sleep(1)
            con.close()
            del datos_cliente
        else:
            print("\nCliente no registrado. Verifique el numero de identificación")
            print("Volviendo al menu principal.\n")
            # Cierra la conexion a la base de datos.
            sleep(1)
            con.close()
            
    elif opcion == "2":
        cedula = int(input("\nIngrese su numero de cedula: "))
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        correo = input("Ingrese su correo electronico: ")
        
        # Verficacion de los datos que son ingresados
        if cedula and nombre.isalpha() and apellido.isalpha() and bool(correo):
            # Insercion del cliente en la base de datos
            datos_cliente = [cedula, nombre, apellido, correo, None, None, None, None, None, 0]
            insertar_cliente(con, cur, datos_cliente)  # Si los datos son correctos se crea el nuevo cliente.
            agregar_subscripcion(con, cur, [cedula, "Gratis"])  # Agrega la subscripción obligatoria.

            print("Cliente registrado satisfactoriamente")
            cliente_logueado(con, cur, datos_cliente)  # Llama a la función controladora con los datos registrados.
            # Cuando la conexión con el cliente termina se borran los datos locales y se cierra la base de datos.
            del cedula, nombre, apellido, correo
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
    # TODO: Mejorar presentacion del menu y tablas

    print("╔" + "═"*32 + "╗")
    print("║ Bienvenido al Programa SpotyUN ║")
    print("╚" + "═"*32 + "╝\n")

    conexion = conexion_base_datos()  # Almacena un objeto con la conexión a la base de datos.
    cursor = conexion.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.

    while True:
        print("Seleccione la opcion que desea realizar:")
        print("1. Ingresar como Administrador.")
        print("2. Ingresar como Cliente.")
        print("3. Crear base de datos basica.")
        print("0. Salir del programa.")
        case = input()

        # Bloque logico donde se escogen las opciones principales del programa.
        if case == "1":
            conexion_administrador(conexion, cursor)  # Llamada a la función que maneja el ingreso como administrador.

        elif case == "2":
            conexion_cliente(conexion, cursor)  # Llamada a la función que maneja el ingreso como cliente.

        elif case == "3":
            crear_base(conexion, cursor)  # Llamada a la funcion que devuelve a la base de datos a su estado base.

        elif case == "0":
            print("\nHasta Luego.")
            sleep(1)
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.\n")
