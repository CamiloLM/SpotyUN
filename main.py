import sqlite3  # Modulo para realizar operaciones a la base de datos
from create import crear_tablas  # Función para crear las tablas
# Se importan los menus de cada uno de los objetos
from objetos.cliente import menu_cliente
from objetos.administrador import menu_administrador
from objetos.cancion import menu_cancion
from objetos.lista_canciones import menu_lista_canciones
from objetos.subscripciones import menu_subscripción
from objetos.planes import menu_planes
from user_interface.mainUI import mainui
from os import environ  # Importa funcion para modificar las variables de entorno
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Oculta mensaje de Pygame


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        # Retorna una conexón sqlite con la base de datos del programa.
        conn = sqlite3.connect('SpotyUN.db')
        conn.execute("PRAGMA foreign_keys = 1")  # Activa la selectividad de las llaves foraneas.
        return conn
    except sqlite3.Error:
        # En caso de que suceda un error grave el programa atrapa e imprime el error.
        print(sqlite3.Error)


if __name__ == "__main__":
    print("╔" + "═"*32 + "╗")
    print("║ Bienvenido al Programa SpotyUN ║")
    print("╚" + "═"*32 + "╝")

    # Almacena un objeto con la conexión a la base de datos.
    conexion = conexion_base_datos()
    # Almacena un objeto cursor para realizar selecciones en la base da datos.
    cursor = conexion.cursor()

    while True:
        print("\nSeleccione que opciones desea ver:")
        print("1. Cliente.")
        print("2. Administrador.")
        print("3. Cancion.")
        print("4. Planes.")
        print("5. Lista canciones.")
        print("6. Suscripciones.")
        print("7. Crear base de datos.")
        print("8. Interfaz gráfica.")
        print("0. Salir del programa.")
        case = input()

        # Bloque logico donde se escogen las opciones principales del programa.
        if case == "1":
            # Llamada al menu cliente para hacer realizar operaciones
            menu_cliente(conexion, cursor)

        elif case == "2":
            # Llamada al menu administrador para hacer realizar operaciones
            menu_administrador(conexion, cursor)

        elif case == "3":
            # Llamada al menu cancion para hacer realizar operaciones
            menu_cancion(conexion, cursor)

        elif case == "4":
            # Llamada al menu planes para hacer realizar operaciones
            menu_planes(conexion, cursor)

        elif case == "5":
            # Llamada al menu lista canciones para hacer realizar operaciones
            menu_lista_canciones(conexion, cursor)

        elif case == "6":
            # Llamada al menu subscripciones para hacer realizar operaciones
            menu_subscripción(conexion, cursor)

        elif case == "7":
            # Almacena el nombre de las tablas usadas por el programa.
            tablas = ("listaCanciones", "subscripciones", "administrador", "cancion", "cliente", "planes")

            # Recorre las tablas para borrarlas por orden.
            for nombre in tablas:
                sql = f"DROP TABLE IF EXISTS {nombre}"  # Se crea la sentencia
                cursor.execute(sql) # Elimina las tablas si no existen
            cursor.execute("DELETE FROM SQLITE_SEQUENCE")  # Borra los indices de las llaves auto incrementables
            conexion.commit()  # Los cambios son llevados a cabo en la base de datos.

            # Crea las tablas del la base de datos si no existen.
            crear_tablas(conexion, cursor)
            print("La base de datos ha sido creada desde cero.")

        elif case == "8":
            # Llamada a la interfaz gráfica para hacer realizar operaciones
            mainui()

        elif case == "0":
            print("\nHasta Luego.")
            # Se cierra la conexión con la base de datos
            conexion.close()
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.\n")
