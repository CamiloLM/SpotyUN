from prettytable import PrettyTable
from crud.read import (
    buscar_cancion_especifica, consulta_canciones, buscar_cancion_nombre,
    consulta_usuario_listas, consulta_planes, buscar_lista
)
from crud.insert import agregar_cancion, agregar_subscripcion
from crud.update import actualizar_cliente, actualizar_pago
from player import reproductor
from correo import enviar_correo
from time import sleep
from datetime import date


def registro_pago(con, cur, cedula,):
    """Actualiza la informacion del cliente con una nueva fecha de pago."""
    fecha = date.today()
    mes = fecha.month + 5
    año = fecha.year + mes // 12
    mes = mes % 12 + 1
    dia = fecha.day
    nueva_fecha = date(año, mes, dia)
    actualizar_pago(con, cur, nueva_fecha, cedula)


def cliente_logueado(con, cur, data):
    """
    Función principal maneja toda las acciones del cliente.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    data (list): Datos del cliente.
    """
    # TODO: Separar las acciones en subfunciones.
    # TODO: Añadir mas opciones al cliente.

    print(f"Bienvenido {data[1]} {data[2]}")
    sleep(1)
    while True:
        print("\nSeleccione la accion que desea realizar")
        print("1. Ver canciones disponibles.")
        print("2. Buscar una cancion por nombre.")
        print("3. Reproducir la cancion seleccionada.")
        print("4. Añadir cancion a una lista.")
        print("5. Ver mis listas de canciones.")
        print("6. Actualizar mi informacion.")
        print("7. Consultar planes premium.")
        print("8. Subscribirme a un plan premium.")
        print("9. Enviar lista de canción al correo.")
        print("0. Cerrar sesion.")
        case = input()
        
        if case == "1":
            # TODO: Modificar consulta canciones, añadir limite y aleatoriedad.
            # Busca todas las canciones en la base de datos
            listado = consulta_canciones(cur)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
            for fila in listado:
                mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
            print("\nEstas son las canciones que puedes elegir:")
            print(mi_tabla)
            sleep(3)
        
        elif case == "2":
            print("\nEscribe el nombre de la cancion que quieres buscar:")
            busqueda = input()
            # TODO: Añadir confirmacion de busqueda no vacia
            # Listado de todas las canciones que contienen esa busqueda
            listado = buscar_cancion_nombre(cur, busqueda)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(2)
            else:
                print("\nEl termino que buscaste no ha encontrado resultados.")
                sleep(1)
        
        elif case == "3":
            print("\nEscriba el numero de la cancion que quiere reproducir:")
            codigo = input()
            if codigo.isdecimal():
                codigo = int(codigo)
                # La busqueda se tiene que realizar por codigo para que sea unica.
                cancion = buscar_cancion_especifica(cur, codigo)
                reproductor(cur, cancion)
            else:
                print("\nEl valor que ingreso no es un numero.")
                print("Accion no realizada.")
                sleep(2)
        
        elif case == "4":
            print("\nEscriba el numero de la cancion que quiere añadir:")
            codigo = input()
            print("Ingresa el nombre de la lista donde vas a agregar la cancion.")
            print("Si no hay una lista con ese nombre, se creara una nueva llamada asi.")
            nombreLista = input()
            # Verificacion que la entrada sea un numero
            if codigo.isdecimal():
                codigo = int(codigo)
                # Busca si la cancion existe en la base de datos
                cancion = buscar_cancion_especifica(cur, codigo)
                # TODO: Agregar bloque logico si la cancion no existe.
                if nombreLista:
                    datos = [nombreLista, data[0], cancion[0]]
                    # Inserta la cancion en listaCanciones
                    agregar_cancion(con, cur, datos)
                    print("\nLa cancion ha sido añadida a la lista")
                    sleep(1)
                else:
                    print("\nNo se le ha puesto un nombre a la lista.")
                    print("Accion no realizada.")
                    sleep(2)
            else:
                print("\nEl valor de cancion que ingreso no es un numero.")
                print("Accion no realizada.")
                sleep(2)
        
        elif case == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre de la Lista"]
            # Consulta de la tabla usuarioCanciones
            # TODO: Mostrar la lista de canciones completa.
            listado = consulta_usuario_listas(cur, data[0])
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0],])
                print("\nEstos son los resultados:")
                print(mi_tabla)
                sleep(2)
            else:
                print("\nEl usuario no tiene listas de canciones.") 
                sleep(1)
        
        elif case == "6":
            nombre = input("\nIngrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            correo = input("Ingrese su correo electronico: ")
            pais = input("Ingrese el nombre del pais donde habita: ")
            ciudad = input("Ingrese el nombre de la ciudad donde habita: ")
            telefono = input("Ingrese su numero telefono: ")
            targetaCredito = input("Ingrese el numero de tarjeta de credito: ")

            # Verficacion de datos en la entrada
            if nombre.isalpha() and apellido.isalpha() and bool(correo):
                # Insercion del cliente en la base de datos
                datos = [nombre, apellido, correo, pais, ciudad, telefono, targetaCredito, data[0]]
                actualizar_cliente(con, cur, datos)

                del nombre, apellido, correo, pais, ciudad, telefono, targetaCredito
            else:
                print("\nAlguno de los datos se ingresaron incorrectamente.")
                sleep(2)
        
        elif case == "7":
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
        
        elif case == "8":
            print("\nIngrese el nombre del plan al que se quiere subscribir:")
            nombre = input()
            # TODO: Verificar que el el plan esta ofertado en la lista de planes
            if nombre.isalpha():
                datos = [data[0], nombre]
                # TODO: El cliente solo deberia tener una subscripcion posible
                agregar_subscripcion(con, cur, datos)
                registro_pago(con, cur, data[0])
                print("\nSubscripcion añadida satisfactoriamente.")
                sleep(1)
            else:
                print("\nEl nombre del plan que ingreso no es correcto.")
                sleep(2)
        
        elif case == "9":
            #Consulta las listas del usuario
            listado = consulta_usuario_listas(cur, data[0])

            print("\nEscriba el nombre de la lista que quiere enviar:")
            nombre = input()

            # Verifica que el nombre este en sus listas de canciones
            if nombre in listado[0]:
                # TODO: Enviar el cuerpo del correo con una mejor tabla
                mi_tabla = PrettyTable()
                mi_tabla.title = f"Canciones de la lista {nombre}"
                mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
                # Busca las canciones de la lista especifica
                for codigo in buscar_lista(cur, nombre, data[0]):
                    cancion = buscar_cancion_especifica(cur, codigo[0])
                    mi_tabla.add_row([cancion[0], cancion[1], cancion[5], cancion[4], cancion[3]])
                # TODO: Encontrar una mejor forma de almacenar las credenciales
                enviar_correo(data[3], mi_tabla.get_string())
                sleep(1)
            else:
                print("\nEl nombre que ingreso no forma parte de sus listas o esta mal escrito.")
                print("Operación no realizada.")
                sleep(2)
        
        elif case == "0":
            print("\nSesion terminada.")
            print("Hasta Pronto.\n")
            sleep(1)
            break
        else:
            print("\nEntrada incorrecta. Intente otra vez.")
            sleep(1)
