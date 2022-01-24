from prettytable import PrettyTable
import crud.read
import crud.insert
import crud.delete
from crud.create import crear_tablas
from time import sleep


def crear_base(con, cur):
    """Crea el esquema de la base de datos sin ningun dato en sus tablas."""
    cur.execute("SELECT name FROM sqlite_schema WHERE type='table'")  # Busca el nombre de todas las tablas.
    tablas = cur.fetchall()  # El nombre queda guardado en la vatiable tablas.
    
    # Se ejecuta si hay tablas en la base de datos.
    if tablas:
        for tabla, in tablas:  # Recorre la lista de tablas para borrarla una a una.
            if tabla != "sqlite_sequence":  # No se puede borrar la tabla sqlite_sequence.
                sql = f"DROP TABLE {tabla}"
                cur.execute(sql)  # Ejecuta el comando para borrar los datos de la tabla.
    
    crear_tablas(con, cur)  # Crea las tablas del la base de datos si no existe.
    datos_admin = [9876543210, "Administrador", "Basico", "correo@gmail.com"]
    datos_plan = ["Gratis", 0.0, 5, "Plan gratuito disponible para todos los clientes."]

    # Se ingresan los datos basicos que debe poseer la base.
    crud.insert.insertar_admin(con, cur, datos_admin)
    crud.insert.insertar_plan(con, cur, datos_plan)

    del datos_admin, datos_plan
    print("La base de datos basica se ha creado correctamente.\n")


def consultas_general(cur):
    """Consulta general de tablas, se usa el cursor para hacer la selección."""

    while True:
        print("\nSeleccione las consultas generales a relizar:")
        print("1. Canciones.")
        print("2. Clientes.")
        print("3. Planes.")
        print("4. Subscripciones.")
        print("5. Listas Canciones.")
        print("6. Administradores.")
        print("0. Salir")
        select = input()

        if select == "1":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Codigo", "Nombre", "Ubicacion", "Genero", "Album", "Interprete"]
            # TODO: Añadir limite a la consulta
            listado = crud.read.consulta_canciones(cur, 99)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "2":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono",
                                    "Tarjeta credito", "Fecha Pago", "Pago"]
            listado = crud.read.consulta_clientes(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row(
                        [fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "3":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            listado = crud.read.consulta_planes(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "4":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula cliente", "Nombre plan"]
            listado = crud.read.consulta_subscripciones(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre lista", "Cedula", "Codigo"]
            listado = crud.read.consulta_general_listas(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "6":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]
            listado = crud.read.consulta_admins(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "0":
            break

        else:
            print("\nNumero equivocado.")


def consultas_especificas(cur):
    """Consulta específica de tablas, se usa el cursor para hacer la selección."""

    while True:
        print("\nSeleccione las consultas especificas a realizar:")
        print("1. Cancion.")
        print("2. Cliente.")
        print("3. Plan.")
        print("4. Subscripcion.")
        print("5. Lista Canciones.")
        print("6. Administrador.")
        print("0. Salir")
        select = input()

        if select == "1":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Codigo", "Nombre", "Ubicacion", "Genero", "Album", "Interprete"]
            codigo = input("Codigo de la cancion: ")
            lista = crud.read.buscar_cancion_especifica(cur, codigo)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3], lista[4], lista[5]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "2":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono",
                                    "Tarjeta credito", "Fecha Pago", "Pago"]
            cedula = input("Cedula del cliente: ")
            lista = crud.read.buscar_cliente(cur, cedula)
            if lista:
                mi_tabla.add_row(
                    [lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                     lista[9]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "3":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            nombre = input("Nombre del plan: ")
            lista = crud.read.buscar_plan(cur, nombre)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "4":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula cliente", "Nombre plan"]
            cedula = input("Cedula del cliente: ")
            lista = crud.read.buscar_subscripcion(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre lista", "Cedula", "Codigo"]
            cedula = input("Cedula del cliente: ")
            listado = crud.read.consulta_especifica_listas(cur, cedula)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "6":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]
            cedula = input("Cedula del administrador: ")
            lista = crud.read.buscar_admin(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(1)
            else:
                print("\nLa tabla no tiene datos")

        elif select == "0":
            break

        else:
            print("\nNumero equivocado.")


def insertar_datos(con, cur):
    """
        Función para insertar datos en las tablas de la BD.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    # TODO: Crear bloque logico para verificar los datos en todas las inserciones.
    # TODO: Testear las inserciones en la BD.

    while True:
        print("\nSeleccione la acción que desea realizar::")
        print("1. Insertar cancion.")
        print("2. Insertar cliente.")
        print("3. Insertar plan.")
        print("4. Insertar subscripcion.")
        print("5. Insertar administrador.")
        print("0. Salir")
        select = input()

        if select == "1":
            print("\nIngrese los datos de la canción")
            nombre = input("Nombre: ")
            ubicacion = input("Nombre del archivo: ")
            genero = input("Genero: ")
            album = input("Album: ")
            interprete = input("Interprete: ")

            datos = [None, nombre, ubicacion, genero, album, interprete]
            crud.insert.insertar_cancion(con, cur, datos)
            print("\nInserción realizada con exito.")

        elif select == "2":
            print("\nIngrese los datos del cliente")
            cedula = input("Numero de cedula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo electronico: ")
            pais = input("Pais: ")
            ciudad = input("Ciudad: ")
            telefono = input("Numero de telefono: ")
            targeta_credito = input("Numero tarjeta de credito: ")
            fecha_pago = input("Fecha pago: ")
            print("Pago realizado? Si:1, No:0")
            pago = input()

            datos = [int(cedula), nombre, apellido, correo, pais, ciudad, int(telefono), int(targeta_credito),
                     fecha_pago, int(pago)]
            crud.insert.insertar_cliente(con, cur, datos)
            print("\nInserción realizada con exito.")

        elif select == "3":
            print("\nIngrese los datos del plan")
            nombre = input("Nombre: ")
            valor = input("Valor: ")
            cantidad = input("Cantidad canciones: ")
            descripcion = input("Descripcion: ")

            datos = [nombre, valor, int(cantidad), descripcion]
            crud.insert.insertar_plan(con, cur, datos)
            print("\nInserción realizada con exito.")

        elif select == "4":
            print("\nIngrese los datos de la subscripción")
            cedula_cliente = input("Cedula cliente: ")
            nombre_plan = input("Nombre plan: ")

            datos = [cedula_cliente, nombre_plan]
            crud.insert.agregar_subscripcion(con, cur, datos)
            print("\nInserción realizada con exito.")

        elif select == "5":
            print("\nIngrese los datos del administrador")
            cedula = input("Numero de cedula: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo electronico: ")

            datos = [int(cedula), nombre, apellido, correo]
            crud.insert.insertar_admin(con, cur, datos)
            print("\nInserción realizada con exito.")

        elif select == "0":
            break

        else:
            print("\nNumero equivocado.")


def eliminar_general(con, cur):
    """
        Función para eliminar datos completos en las tablas de la base de datos.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """

    while True:
        print("\nSeleccione la acción que desea realizar::")
        print("1. Eliminar datos de cancion.")
        print("2. Eliminar datos de cliente.")
        print("3. Eliminar datos de planes.")
        print("4. Eliminar datos de subscripciones.")
        print("5. Eliminar datos de listaCanciones.")
        print("6. Eliminar datos de administrador.")
        print("0. Salir")
        select = input()

        if select == "1":
            print("\nEsta seguro de que desea borrar todos los registros de la tabla cancion? S/n")
            bandera = input()
            if bandera == "S":
                crud.delete.borrar_canciones(con, cur)
                print("\nLos datos de la tabla han sido borrados.")
            else:
                print("\nNo se ha realizado ninguna acción.")

        elif select == "2":
            print("\nEsta seguro de que desea borrar todos los registros de la tabla cliente? S/n")
            bandera = input()
            if bandera == "S":
                crud.delete.borrar_clientes(con, cur)
                print("\nLos datos de la tabla han sido borrados.")
            else:
                print("\nNo se ha realizado ninguna acción.")

        elif select == "3":
            print("\nEsta seguro de que desea borrar todos los registros de la tabla planes? S/n")
            bandera = input()
            if bandera == "S":
                crud.delete.borrar_planes(con, cur)
                print("\nLos datos de la tabla han sido borrados.")
            else:
                print("\nNo se ha realizado ninguna acción.")

        elif select == "4":
            print("\nEsta seguro de que desea borrar todos los registros de la tabla subscripciones? S/n")
            bandera = input()
            if bandera == "S":
                crud.delete.borrar_subscripciones(con, cur)
                print("\nLos datos de la tabla han sido borrados.")
            else:
                print("\nNo se ha realizado ninguna acción.")

        elif select == "5":
            print("\nEsta seguro de que desea borrar todos los registros de la tabla listaCanciones? S/n")
            bandera = input()
            if bandera == "S":
                crud.delete.borrar_listasCanciones(con, cur)
                print("\nLos datos de la tabla han sido borrados.")
            else:
                print("\nNo se ha realizado ninguna acción.")

        elif select == "6":
            # TODO: Como salir del bucle principal si no hay administrador
            # print("\nEsta seguro de que desea borrar todos los registros de la tabla administradores? S/n")
            # bandera = input()
            # if bandera == "S":
            #     crud.delete.borrar_administradores(con, cur)
            #     print("\nLos datos de la tabla han sido borrados.")
            # else:
            print("\nNo se ha realizado ninguna acción.")

        elif select == "0":
            break

        else:
            print("\nNumero equivocado.")


def eliminar_especifico(con, cur, cedula_admin):
    """
        Función para eliminar datos especificos en las tablas de la base de datos.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    # TODO: Añadir logica al input en todas las eliminaciones
    while True:
        print("\nSeleccione la acción que desea realizar::")
        print("1. Eliminar registro de cancion.")
        print("2. Eliminar registro de cliente.")
        print("3. Eliminar registro de planes.")
        print("4. Eliminar registro de subscripciones.")
        print("5. Eliminar registro de listaCanciones.")
        print("6. Eliminar registro de administrador.")
        print("0. Salir")
        select = input()

        if select == "1":
            print("\nIngrese el codigo de la cancion a eliminar.")
            entrada = input()
            crud.delete.borrar_cancion(con, cur, entrada)
            print("\nEliminación realizada con exito.")

        elif select == "2":
            print("\nIngrese la cedula del cliente a eliminar.")
            entrada = input()
            crud.delete.borrar_cliente(con, cur, entrada)
            print("\nEliminación realizada con exito.")

        elif select == "3":
            print("\nIngrese el nombre exacto del plan a eliminar.")
            entrada = input()
            crud.delete.borrar_plan(con, cur, entrada)
            print("\nEliminación realizada con exito.")

        elif select == "4":
            print("\nIngrese la cedula del cliente de la subscripcioón correspondiente.")
            cedula = input()

            print("\nIngrese el nombre del plan de la subscripcioón correspondiente.")
            nombre = input()
            crud.delete.borrar_subscripcion(con, cur, cedula, nombre)

            crud.update.actualizar_subscripcion(con, cur, "Gratis", cedula)
            crud.update.actualizar_pago(con, cur, None, None, cedula)

            print("\nEliminación realizada con exito.")

        elif select == "5":
            print("\nIngrese el nombre de la lista que quiere eliminar.")
            nombre = input()

            print("\nIngrese la cedula del cliente al que corresponde la lista.")
            cedula = input()
            crud.delete.borrar_subscripcion(con, cur, nombre, cedula)
            print("\nEliminación realizada con exito.")

        elif select == "6":
            print("\nIngrese la cedula del administrador que quiere eliminar.")
            cedula = int(input())

            if cedula != cedula_admin:
                crud.delete.borrar_administrador(con, cur, cedula)
            else:
                print("El administrador no se puede eliminar a si mismo")

        elif select == "0":
            break

        else:
            print("\nNumero equivocado.")


def admin_logueado(con, cur, data):
    """
        Función principal que maneja las opciones del administrador.

        Parametros:
        con (sqlite3.Connection): Necesario para pasarlo a otras funciones.
        cur (sqlite3.Cursor): Necesario para pasarlo a otras funciones.
        data (list): Datos del administrador.
    """
    print(f"\nBienvenido {data[1]} {data[2]}")
    sleep(1)
    # TODO: Agregar funcion para actualizar datos
    # TODO: Agregar consultas y orden por cualquier valor

    while True:
        print("\nSeleccione la accion que desea realizar:")
        print("1. Realizar consultas generales.")
        print("2. Realizar consultas especificas.")
        print("3. Ingresar nuevos datos a la base.")
        print("4. Eliminar datos especificos de una tabla")
        print("5. Eliminar datos completos de una tabla")
        print("0. Salir")
        case = input()

        if case == "1":
            consultas_general(cur)

        elif case == "2":
            consultas_especificas(cur)

        elif case == "3":
            insertar_datos(con, cur)

        elif case == "4":
            insertar_datos(con, cur)

        elif case == "5":
            insertar_datos(con, cur, data[0])

        elif case == "0":
            print("\nSesion terminada.\n")
            break

        else:
            sleep(1)
            print("\nEntrada incorrecta. Por favor, intente otra vez.")
