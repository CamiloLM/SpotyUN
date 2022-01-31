import sqlite3  # Modulo para realizar operaciones a la base de datos
from os import environ
from create import crear_tablas
from cliente import menu_cliente
from administrador import menu_administrador
from cancion import menu_cancion
from planes import menu_planes
from lista_canciones import menu_lista_canciones
from subscripciones import menu_subscripción

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

    conexion = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    # Almacena un objeto cursor para realizar selecciones en la base da datos.
    cursor = conexion.cursor()

    while True:
        print("\nSeleccione que opciones desea ver:")
        print("1. Cliente.")
        print("2. Administrador.")
        print("3. Cancion.")
        print("4. Planes.")
        print("5. Lista canciones.")
        print("6. Subscripciones.")
        print("7. Crear base de datos.")
        print("0. Salir del programa.")
        case = input()

        # Bloque logico donde se escogen las opciones principales del programa.
        if case == "1":
            menu_cliente(conexion, cursor)

        elif case == "2":
            menu_administrador(conexion, cursor)

        elif case == "3":
            menu_cancion(conexion, cursor)

        elif case == "4":
            menu_planes(conexion, cursor)

        elif case == "5":
            menu_lista_canciones(conexion, cursor)

        elif case == "6":
            menu_subscripción(conexion, cursor)

        elif case == "7":
            # Busca el nombre de todas las tablas.
            cursor.execute("SELECT name FROM sqlite_schema WHERE type='table'")
            tablas = cursor.fetchall()  # El nombre queda guardado en la vatiable tablas.

            # Se ejecuta si hay tablas en la base de datos.
            if tablas:
                for tabla, in tablas:  # Recorre la lista de tablas para borrarla una a una.
                    if tabla != "sqlite_sequence":  # No se puede borrar la tabla sqlite_sequence.
                        sql = f"DROP TABLE {tabla}"
                        cursor.execute(sql)  # Ejecuta el comando para borrar los datos de la tabla.
                conexion.commit()  # Los cambios son llevados a cabo en la base de datos.

            crear_tablas(conexion, cursor)  # Crea las tablas del la base de datos si no existe.
            print("La base de datos ha sido creada desde cero.")

        elif case == "0":
            print("\nHasta Luego.")
            conexion.close()
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.\n")
