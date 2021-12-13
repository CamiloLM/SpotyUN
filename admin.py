from prettytable import PrettyTable
import crud.read
import crud.insert
from crud.create import crear_tablas
from time import sleep

def crear_base(con, cur):
    crear_tablas(con, cur)
    datos = [9876543210, "Administrador", "Basico", "correo@gmail.com"]
    crud.insert.insertar_admin(con, cur, datos)


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
            listado = crud.read.consulta_canciones(cur)
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
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Tarjeta credito", "Fecha Pago", "Pago"]
            listado = crud.read.consulta_clientes(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]])
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
    """Consulta especifica de tablas, se usa el cursor para hacer la selección."""

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
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Tarjeta credito", "Fecha Pago", "Pago"]
            cedula = input("Cedula del cliente: ")
            lista = crud.read.buscar_cliente(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]])
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
            listado = crud.read.consulta_usuario_listas(cur, cedula)
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
            targetaCredito = input("Numero tarjeta de credito: ")
            fechaPago = input("Fecha pago: ")
            print("Pago realizado? Si:1, No:0")
            pago = input()

            datos = [int(cedula), nombre, apellido, correo, pais, ciudad, int(telefono), int(targetaCredito), fechaPago, int(pago)]
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
            cedulaCliente = input("Cedula cliente: ")
            nombrePlan = input("Nombre plan: ")
        
            datos = [cedulaCliente, nombrePlan]
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
    # TODO: Crear modulo y funcion para eliminar datos
    # TODO: Agregar consultas y orden por cualquier valor
    # TODO: Crear funcion para vaciar las tablas de la base de datos

    while True:
        print("\nSeleccione la accion que desea realizar:")
        print("1. Realizar consultas generales.")
        print("2. Realizar consultas especificas.")
        print("3. Ingresar nuevos datos a la base.")
        print("0. Salir")
        case = input()
        
        if case == "1":
            consultas_general(cur)

        elif case == "2":
            consultas_especificas(cur)

        elif case == "3":
            insertar_datos(con, cur)

        elif case == "0":
            print("\nSesion terminada.\n")
            break

        else:
            sleep(1)
            print("\nEntrada incorrecta. Por favor, intente otra vez.")
