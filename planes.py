import sqlite3  # Modulo para realizar operaciones a la base de datos
from prettytable import PrettyTable  # Módulo para hacer tablas bonitas
import time  # Modulo que proporciona varias funciones útiles para manejar
# las tareas relacionadas con el tiempo.


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea
    una vacia."""
    try:
        """Retorna una conexón sqlite con la base de datos del programa."""
        return sqlite3.connect('SpotyUN.db')
    except sqlite3.Error:
        """En caso de que suceda un error grave el programa atrapa e imprime el
        error."""
        print(sqlite3.Error)


class Plan:
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto 'Plan'."""
        self.__codigo = ""
        self.__nombre = ""
        self.__valor = ""
        self.__cantidad = ""

    def setdatos(self, codigo, nombre, valor, cantidad):
        """Método para leer el valor de los datos/argumentos privados."""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__valor = valor
        self.__cantidad = cantidad

    def setactualizar(self, nombre, valor, cantidad):
        """Método para leer el valor de los datos/argumentos privados."""
        self.__nombre = nombre
        self.__valor = valor
        self.__cantidad = cantidad

    def setcodigo(self, codigo):
        """Método para leer el código"""
        self.__codigo = codigo

    def getdatos(self):
        """Método se emplea para obtener los datos/argumentos privados de la
        clase.
        """
        return [self.__codigo, self.__nombre, self.__valor, self.__cantidad]

    def getactualizar(self):
        """Método se emplea para obtener los datos/argumentos privados de la
        clase.
        """
        return [self.__nombre, self.__valor, self.__cantidad]

    def getcodigo(self):
        """Método se emplea para obtener el código"""
        return [self.__codigo]

    def consulta_planes_general(self, cur, campo="codigo") -> tuple:
        """Consulta todos los datos de la tabla planes ordenándolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por el código.

        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.

        Regresa:
        datos_planes (tuple): Tupla con todos los planes ordenados por el campo
        None: Si no encuentra ninguna coincidencia."""
        cur.execute("SELECT * FROM planes ORDER BY {}".format(campo))
        return cur.fetchall()

    def consulta_plan_especifica(self, cur) -> tuple:
        """
        Consulta un plan por su nombre.

        Parametros:
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        nombre(str): Nombre del plan
        """
        datos = [self.__codigo]
        cur.execute("SELECT * FROM planes WHERE codigo = ?", datos)
        return cur.fetchone()

    def registrar_plan(self, con, cur, planes):
        """
        Ingresa multiples datos en la tabla planes.

        Parametros:
        con(sqlite3.Connection): Conexion a la base de datos.
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        planes(list): Lista con los datos de los planes.
        """
        cur.executemany(
            "INSERT OR IGNORE INTO planes VALUES (?, ?, ?, ?)", [planes])
        con.commit()
        return cur.rowcount

    def actualizar_plan(self, con, cur, planes, codigo):
        """
        Ingresa datos en la tabla planes, estos datos deben estar en orden.

        Parametros:
        con(sqlite3.Connection): Conexion a la base de datos.
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        plan(list): codigo(int), nombre(str), valor(float), cantidad(int).
        """
        valores = planes + codigo
        cur.execute('''
            UPDATE OR IGNORE planes
            SET nombre = ?,
            valor = ?,
            cantidad = ?
            WHERE codigo = ?''', valores)
        con.commit()
        return cur.rowcount

    def borrar_plan(self, con, cur, codigo):
        """
        Borra un regristro en la tabla planes.

        Parametros:
        con(sqlite3.Connection): Conexion a la base de datos.
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        self.__nombre(str): Nombre del plan exactamente como aparece en
        la base.
        """
        cur.execute("DELETE FROM planes WHERE codigo = ?", codigo)
        con.commit()
        return cur.rowcount

    def borrar_planes(self, con, cur):
        """
        Borra todos los registros en la tabla planes.

        Parametros:
        con(sqlite3.Connection): Conexion a la base de datos.
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM planes")
        con.commit()
        return cur.rowcount


def menu_planes(con, cur):
    planes = Plan()
    while True:
        print("\nSeleccione que opciones desea realizar:")
        print("1. Registrar plan.")
        print("2. Consulta general de planes.")
        print("3. Consulta específica de plan.")
        print("4. Actualizar plan.")
        print("5. Eliminar plan específico.")
        print("6. Eliminar plan general.")
        print("0. Salir del programa.")
        case = input()
        time.sleep(2.5)

        if case == "1":
            # Ingresando un nuevo plan
            codigo = input("\nIngrese el código: ")
            nombre = input("Ingrese nombre: ")
            valor = input("Ingrese el valor: ")
            cantidad = input("Ingrese la cantidad de canciones: ")

            # Verficacion de que los datos que son ingresados son correctos
            if codigo.isdigit() and nombre.isalpha() and valor.isdecimal() and cantidad.isdigit():
                # Actualiza los datos usuario del objeto admin
                planes.setdatos(codigo, nombre, valor, cantidad)
                datos = planes.getdatos()

                # Se borran las variables que ya no se utilizan
                del codigo, nombre, valor, cantidad
                # Llama al metodo para registrar el plan en la base de datos
                cambios = planes.registrar_plan(con, cur, datos)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nPlan ingresado con exito.")
                    time.sleep(2.5)
                else:
                    print(
                        "\nEl plan ya está registrado, no se han realizado cambios.")
                    time.sleep(2.5)
            else:
                print("\nAlguno de los datos que ingreso no son correctos")
                time.sleep(2.5)

        elif case == "2":
            # Consulta general de administradores por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            # Asgina los nombres de los campos en la tabla
            mi_tabla.field_names = [
                "Código", "Nombre", "Valor", "Cantidad Canciones"]
            campo = "codigo"  # Campo por el que se va a ordenar

            # Bucle para poder ordenar las busquedas por campos
            while True:
                # Excepcion por si se ingresan campos que no esten en la tabla
                try:
                    # Busqueda en la tabla usuario general pasando el campo por el que ordena
                    datos_plan = planes.consulta_planes_general(
                        cur, campo)

                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_plan:
                        # Añade datos las filas a la tabla
                        mi_tabla.add_rows(datos_plan)
                        print("")
                        print(mi_tabla)
                        time.sleep(3)
                        bandera = input(
                            "Desea ordenar la busqueda por un campo (S/n): ")

                        # Bandera logica por si se quiere ordenar un campo
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            # Entrada en minisculas
                            campo = input(
                                "Ingrese el campo por el que quiere ordenar la búsqueda: ").lower()
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        time.sleep(2.5)
                        break
                except sqlite3.OperationalError:
                    print(
                        "\nLa tabla no cuenta con el campo que ha proporcionado.")
                    time.sleep(2.5)
                    break

        elif case == "3":
            # Consulta especifica de plan por código
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            # Asgina los nombres de los campos en la tabla
            mi_tabla.field_names = [
                "Código", "Nombre", "Valor", "Cantidad"]

            codigo = input("\nIngrese código del plan: ")
            # Verficacion de los datos que son ingresados son correctos
            if codigo.isdigit():
                # Actualiza la cedula del objeto admin
                planes.setcodigo(int(codigo))
                # Almacena todos los datos del admin
                datos_plan = planes.consulta_plan_especifica(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_plan:
                    # Añade datos las filas a la tabla
                    mi_tabla.add_row(datos_plan)
                    print("")
                    print(mi_tabla)
                    time.sleep(3)
                else:
                    print("\nLa tabla no tiene datos")
                    time.sleep(2.5)
            else:
                print("\nEl código ingresado no es valido")
                time.sleep(2.5)

        elif case == "4":
            # Actualizar los datos del administrador
            print("\nIngrese los nuevos datos del plan.")
            nombre = input("Nombre: ")
            valor = input("Valor: ")
            cantidad = input("Cantidad de canciones: ")

            print("\nIngrese el código del plan que va a modificar:")
            codigo = input()

            # Verficacion de que los datos que son ingresados son correctos
            if codigo.isdigit() and nombre.isalpha() and valor.isdigit() and cantidad.isdigit():
                # Actualiza la cedula del objeto admin
                planes.setcodigo(int(codigo))
                datos2 = planes.getcodigo()
                # Actualiza los datos usuario del objeto planes
                planes.setactualizar(nombre, valor, cantidad)
                datos1 = planes.getactualizar()

                # Se borran las variables que ya no se utilizan
                del codigo, nombre, valor, cantidad

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = planes.actualizar_plan(
                    conexion, cursor, datos1, datos2)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nPlan actualizado con exito.")
                    time.sleep(2.5)
                else:
                    print(
                        "\nCódigo no registrado, no se han realizado cambios.")
                    time.sleep(2.5)

        elif case == "5":
            # Eliminar datos especificos de la tabla planes
            print("\nIngrese el código del plan a eliminar:")
            codigo = input()

            if codigo.isdigit():
                planes.setcodigo(int(codigo))

                del codigo  # Se borra la variable que no se va a utilizar

                # Llama al metodo que borra el plan en la base de datos
                codigo = planes.getcodigo()
                cambios = planes.borrar_plan(conexion, cursor, codigo)
                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nPlan Nº ", codigo, " eliminado con exito.")
                    time.sleep(2.5)
                else:
                    print(
                        "\nCódigo no registrado, no se han realizado cambios.")
                    time.sleep(2.5)

        elif case == "6":
            # Eliminar datos generales de la tabla administrador
            bandera = input(
                "¿Está seguro que desea realizar esta acción, los datos se perderán (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = planes.borrar_planes(conexion, cursor)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print(
                        "\nTodos los datos de la tabla planes han sidos eliminados.")
                    time.sleep(2.5)
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")
                    time.sleep(2.5)

        elif case == "0":
            print("\nSaliendo del menú planes.")
            time.sleep(2.5)
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente de nuevo.")
            time.sleep(2.5)


conexion = conexion_base_datos()
# Almacena un objetos con la conexión a la base de datos.
cursor = conexion.cursor()
# Almacena un objeto cursor para realizar selecciones en la base da datos.

menu_planes(conexion, cursor)
