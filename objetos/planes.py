from prettytable import PrettyTable  # Módulo para hacer tablas bonitas
from sqlite3 import OperationalError, IntegrityError


class Plan:
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto 'Plan'."""
        self.__codigo = None
        self.__nombre = None
        self.__valor = None
        self.__cantidad = None


    def setdatos(self, nombre, valor, cantidad):
        """Método para leer el valor de los datos/argumentos privados."""
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


    def registrar_plan(self, con, cur, datos):
        """
        Ingresa multiples datos en la tabla planes.

        Parametros:
        con(sqlite3.Connection): Conexion a la base de datos.
        cur(sqlite3.Cursor): Cursor para realizar las operaciones.
        datos(list): Lista con los datos de los planes.
        """
        cur.execute("INSERT OR IGNORE INTO planes VALUES (?, ?, ?, ?)", datos)
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
        print("0. Salir del menu planes.")
        case = input()

        if case == "1":
            # Ingresando un nuevo plan
            nombre = input("\nIngrese nombre: ").strip()
            valor = input("Ingrese el valor: ").strip()
            cantidad = input("Ingrese la cantidad de canciones: ").strip()

            # Verficacion de que los datos que son ingresados son correctos
            if nombre.isalpha() and valor and cantidad.isdigit():
                # Actualiza los datos usuario del objeto admin
                planes.setdatos(nombre, valor, cantidad)
                datos = planes.getdatos()

                # Se borran las variables que ya no se utilizan
                del nombre, valor, cantidad
                # Llama al metodo para registrar el plan en la base de datos
                cambios = planes.registrar_plan(con, cur, datos)

                # Verifica si se realizaron cambios en la base de datos
                if cambios > 0:
                    print("\nPlan ingresado con exito.")
                else:
                    print(
                        "\nEl plan ya está registrado, no se han realizado cambios.")
            else:
                print("\nAlguno de los datos que ingreso no son correctos")

        elif case == "2":
            # Consulta general de administradores por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            # Asgina los nombres de los campos en la tabla
            mi_tabla.field_names = [
                "Código", "Nombre", "Valor", "Cantidad"]
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
                        break
                except OperationalError:
                    print(
                        "\nLa tabla no cuenta con el campo que ha proporcionado.")
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
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl código ingresado no es valido")

        elif case == "4":
            # Actualizar los datos del administrador
            print("\nIngrese los nuevos datos del plan.")
            nombre = input("Nombre: ").strip()
            valor = input("Valor: ").strip()
            cantidad = input("Cantidad de canciones: ").strip()

            print("\nIngrese el código del plan que va a modificar:")
            codigo = input().strip()

            # Verficacion de que los datos que son ingresados son correctos
            if codigo.isdigit() and nombre.isalpha() and valor and cantidad.isdigit():
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
                    con, cur, datos1, datos2)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nPlan actualizado con exito.")
                else:
                    print(
                        "\nCódigo no registrado, no se han realizado cambios.")
            else:
                print("\nAlguno de los campos que ingreso esta vacio.")

        elif case == "5":
            # Eliminar datos especificos de la tabla planes
            print("\nIngrese el código del plan a eliminar:")
            codigo = input()

            if codigo.isdigit():
                planes.setcodigo(int(codigo))

                del codigo  # Se borra la variable que no se va a utilizar
                codigo = planes.getcodigo()

                try:
                    # Llama al metodo que borra el plan en la base de datos
                    cambios = planes.borrar_plan(con, cur, codigo)
                    # Verifica si se realizaron cambios en la base de datos
                    if cambios != 0:
                        print("\nPlan Nº ", codigo, " eliminado con exito.")
                    else:
                        print(
                            "\nCódigo no registrado, no se han realizado cambios.")
                except IntegrityError:
                    print("\nEl plan no se ha podido eliminar por que forma parte de una subscripción.")

        elif case == "6":
            # Eliminar datos generales de la tabla administrador
            bandera = input("¿Está seguro que desea realizar esta acción, los datos se perderan? (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = planes.borrar_planes(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                try:
                    if cambios != 0:
                        print(
                            "\nTodos los datos de la tabla planes han sidos eliminados.")
                    else:
                        print("\nAlgo ha ido mal, no se han realizado cambios.")
                except IntegrityError:
                    print("\nAlgun plan no se ha podido eliminar por que forma parte de una subscripción.")

        elif case == "0":
            print("\nSaliendo del menú planes.")
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente de nuevo.")
