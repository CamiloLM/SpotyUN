from prettytable import PrettyTable
from crud.read import (
    buscar_cancion_especifica, consulta_canciones, buscar_cancion_nombre, buscar_plan, buscar_cliente,
    consulta_nombre_listas, consulta_codigo_listas, consulta_planes, buscar_subscripcion
)
from crud.insert import agregar_cancion, agregar_subscripcion
from crud.update import actualizar_cliente, actualizar_pago, actualizar_subscripcion
from player import reproductor
from correo import enviar_correo
from time import sleep
from datetime import date


def registro_pago(con, cur, datos_cliente):
    """Actualiza la informacion del cliente con una nueva fecha de pago."""
    fecha = date.today()
    mes = fecha.month + 5
    año = fecha.year + mes // 12
    mes = mes % 12 + 1
    dia = fecha.day
    nueva_fecha = date(año, mes, dia)
    actualizar_pago(con, cur, nueva_fecha, 1, datos_cliente[0])
    actualizar_subscripcion(con, cur, datos_cliente[1], datos_cliente[0])


def consulta_fecha_pago(con, cur, datos_cliente):
    """Consulta si el cliente ya se paso de su fecha de pago."""
    fecha = date.today()
    if fecha > datos_cliente[8]:
        actualizar_pago(con, cur, None, 0, datos_cliente[0])
        actualizar_subscripcion(con, cur, "Gratis", datos_cliente[0])


def canciones_cliente(con, cur, cedula, limite):
    while True:
        print("\nSeleccione la acción que desea realizar")
        print("1. Ver canciones disponibles.")
        print("2. Buscar una cancion por nombre.")
        print("3. Reproducir cancion seleccionada.")
        print("4. Añadir cancion a una lista.")
        print("0. Volver al menu principal.")
        case = input()

        if case == "1":
            # Busca todas las canciones en la base de datos con limite de canciones.
            # TODO: Poder ordenar las canciones por cualquier campo
            listado = consulta_canciones(cur, limite)
            if listado:
                mi_tabla = PrettyTable()
                mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
                print("\nEstas son las canciones que puedes escuchar:")
                print(mi_tabla)
                sleep(3)
            else:
                print("\nNo se encuentran canciones disponibles para tu cuenta.")
                sleep(1)
        
        elif case == "2":
            print("\nEscribe el nombre de la cancion que quieres buscar:")
            busqueda = input()
            # Listado de todas las canciones que contienen esa busqueda
            listado = buscar_cancion_nombre(cur, busqueda)
            if listado:
                mi_tabla = PrettyTable()
                mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(2)
            elif not listado:
                print("\nNo se ha ingresado datos en la busqueda.")
                sleep(1)
            else:
                print("\nEl termino que buscaste no ha encontrado resultados.")
                sleep(1)

        elif case == "3":
            print("\nEscriba el numero de la cancion que quiere reproducir:")
            codigo = int(input())
            if codigo < limite:
                # La busqueda se tiene que realizar por codigo para que sea unica.
                cancion = buscar_cancion_especifica(cur, codigo)
                reproductor(cur, cancion)
            else:
                print("\nEl valor que ingreso no es un numero.")
                print("Accion no realizada.")
                sleep(2)
        
        elif case == "4":
            print("\nEscriba el numero de la cancion que quiere añadir:")
            # TODO: Que la entrada sea un entero.
            codigo = int(input())
            print("Ingresa el nombre de la lista donde vas a agregar la cancion.")
            print("Si no hay una lista con ese nombre, se creara una nueva llamada asi.")
            nombre_lista = input()
            # Verificacion que la entrada sea un número
            if codigo < limite:
                # Busca si la cancion existe en la base de datos
                cancion = buscar_cancion_especifica(cur, codigo)
                # TODO: Agregar bloque logico si la cancion no existe.
                if nombre_lista:
                    datos = [nombre_lista, cedula, cancion[0]]
                    # Inserta la cancion en listaCanciones
                    agregar_cancion(con, cur, datos)
                    print("\nLa cancion ha sido añadida a la lista")
                    sleep(1)
                else:
                    print("\nNo se le ha puesto un nombre a la lista.")
                    print("Accion no realizada.")
                    sleep(2)
            else:
                print("\nEl valor de cancion que ingreso no esta disponible.")
                print("Accion no realizada.")
                sleep(2)

        elif case == "0":
            print("\nVolviendo al menu de usuario.")
            break

        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)


def lista_canciones(con, cur, datos_cliente):
    while True:
        print("\nSeleccione la acción que desea realizar")
        print("1. Ver mis listas de canciones.")
        print("2. Eliminar lista de canciones")
        print("3. Enviar lista de canción al correo.")
        print("0. Volver al menu principal.")
        case = input()

        if case == "1":
            nombres_listas = consulta_nombre_listas(cur, datos_cliente[0])  # Consulta el nombre de las listas del usuario
            if nombres_listas:
                # Consultar los codigos de las canciones teniendo el nombre de la lita
                for nombre in nombres_listas:
                    codigos_canciones = consulta_codigo_listas(cur, datos_cliente[0], nombre[0])
                    # Ya teniendo los codigos es posible consultar la informacion de cada cancion
                    mi_tabla = PrettyTable()
                    mi_tabla.title = nombre[0]
                    mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
                    for codigo in codigos_canciones:
                        datos = buscar_cancion_especifica(cur, codigo[0])
                        # Los datos de cada cancion son agregados a una nueva fila de la tabla
                        mi_tabla.add_row([datos[0], datos[1], datos[5], datos[4], datos[3]])
                    print(f"\nCanciones de la lista {nombre[0]}:")
                    print(mi_tabla)
                    sleep(3)
            else:
                print("\nEl usuario no tiene listas de canciones.")
                sleep(1)
        
        elif case == "2":
            pass
        
        elif case == "3":
            # Consulta las listas del usuario
            nombres_listas = consulta_nombre_listas(cur, datos_cliente[0])  # Consulta el nombre de las listas del usuario

            print("\nEscriba el nombre de la lista que quiere enviar:")
            nombre = input()

            # Verifica que el nombre esté en sus listas de canciones
            if nombre in nombres_listas[0]:
                mi_tabla = PrettyTable()
                mi_tabla.title = f"Canciones de la lista {nombre}"
                mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
                # Busca las canciones de la lista específica
                for codigo in consulta_codigo_listas(cur, datos_cliente[0], nombre):
                    cancion = buscar_cancion_especifica(cur, codigo[0])
                    mi_tabla.add_row([cancion[0], cancion[1], cancion[5], cancion[4], cancion[3]])
                enviar_correo(datos_cliente[3], mi_tabla.get_html_string())
                sleep(1)
            else:
                print("\nEl nombre que ingreso no forma parte de sus listas o esta mal escrito.")
                print("Operación no realizada.")
                sleep(2)
        
        elif case == "0":
            print("\nVolviendo al menu de usuario.")
            break

        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)
        

def informacion_cliente(con, cur, datos_cliente):
    while True:
        print("\nSeleccione la acción que desea realizar")
        print("1. Consultar mis datos.")
        print("2. Actualizar mi informacion.")
        print("3. Eliminar cuenta.")
        print("0. Volver al menu principal.")
        case = input()

        if case == "1":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Tarjeta credito", "Fecha Pago", "Pago"]
            lista = buscar_cliente(cur, datos_cliente[0])
            mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]])
            print("\nEstos son los resultados:")
            print(mi_tabla)
            sleep(1)
        
        elif case == "2":
            nombre = input("\nIngrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            correo = input("Ingrese su correo electronico: ")
            pais = input("Ingrese el nombre del pais donde habita: ")
            ciudad = input("Ingrese el nombre de la ciudad donde habita: ")
            telefono = input("Ingrese su numero telefono: ")
            targeta_credito = input("Ingrese el numero de tarjeta de credito: ")

            # Verficacion de datos en la entrada
            if nombre.isalpha() and apellido.isalpha() and bool(correo):
                # Insercion del cliente en la base de datos
                datos = [nombre, apellido, correo, pais, ciudad, telefono, targeta_credito, datos_cliente[0]]
                actualizar_cliente(con, cur, datos)
                del nombre, apellido, correo, pais, ciudad, telefono, targeta_credito
                print("\nLos datos se han actualizado.")
                sleep(1)
            else:
                print("\nAlguno de los datos NO se ingresaron correctamente.")
                sleep(2)
        
        elif case == "3":
            pass
        
        elif case == "0":
            print("\nVolviendo al menu de usuario.")
            break

        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)


def informacion_planes(con, cur, datos_cliente):
    while True:
        print("\nSeleccione la acción que desea realizar")
        print("1. Informacion de mi plan")
        print("2. Consultar planes premium.")
        print("3. Subscribirme a un plan premium.")
        print("4. Actualizar pago")
        print("0. Volver al menu principal.")
        case = input()

        if case == "1":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            datos_plan = buscar_subscripcion(cur, datos_cliente[0])
            mi_tabla.add_row([datos_plan[0], datos_plan[1], datos_plan[2], datos_plan[3]])
            print("\nEstos son los resultados:")
            print(mi_tabla)
            sleep(1)
        
        elif case == "2":
            # TODO: Modificar los planes, en cantidad es numero de canciones disponibles.
            # Busca todas los plnes en la base de datos
            listado = consulta_planes(cur)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            for fila in listado:
                mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
            print("\nEstas son los planes a los que puedes subscribirte:")
            print(mi_tabla)
            sleep(3)
        
        elif case == "3":
            print("\nIngrese el nombre del plan al que se quiere subscribir:")
            nombre = input()
            # TODO: Verificar que el el plan esta ofertado en la lista de planes
            if nombre.isalpha():
                datos = [datos_cliente[0], nombre]
                # TODO: El cliente solo deberia tener una subscripcion posible
                # TODO: No agregar suscripción nueva.
                agregar_subscripcion(con, cur, datos)
                registro_pago(con, cur, datos)
                print("\nSubscripcion añadida satisfactoriamente.")
                sleep(1)
            else:
                print("\nEl nombre del plan que ingreso no es correcto.")
                sleep(2)
        
        elif case == "4":
            pass
        
        elif case == "0":
            print("\nVolviendo al menu de usuario.")
            break

        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)


def cliente_logueado(con, cur, data):
    """
    Función principal maneja todas las acciones del cliente.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    data (list): Datos del cliente.
    """
    print(f"Bienvenido {data[1]} {data[2]}")
    sleep(1)
    # TODO: Testeo de las opciones de usuario
    # TODO: Testeo funciones de pago

    while True:
        print("\nSeleccione la accion que desea realizar")
        print("1. Buscar y reproducir canciones.")
        print("2. Consultar mis listas de canciones.")
        print("3. Consultar los datos de mi cuenta.")
        print("4. Consulta de planes")
        print("0. Cerrar sesion.")
        case = input()

        if case == "1":
            # TODO: Mirar que pasa si se busca un usuario que no tenga una subscripcion registrada
            nombreplan = buscar_subscripcion(cur, data[0])[1]
            limite = buscar_plan(cur, nombreplan)[2]
            canciones_cliente(con, cur, data[0], limite)

        elif case == "2":
            lista_canciones(con, cur, data)

        elif case == "3":
            informacion_cliente(con, cur, data)

        elif case == "4":
            informacion_planes(con, cur, data)

        elif case == "0":
            print("\nSesion terminada.")
            print("Hasta Pronto.\n")
            sleep(1)
            break
        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)
