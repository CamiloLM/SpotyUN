from prettytable import PrettyTable
from crud.read import buscar_cancion_especifica, consulta_canciones, buscar_cancion, consulta_usuario_listas, consulta_planes
from crud.insert import agregar_cancion, agregar_subscripcion
from crud.update import actualizar_cliente
from player import reproductor


def cliente_logueado(con, cur, data):
    print(f"Bienvenido {data[1]} {data[2]}")
    while True:
        print("Seleccione la accion que desea realizar")
        print("1. Ver canciones disponibles.")
        print("2. Buscar una cancion por nombre.")
        print("3. Reproducir la cancion seleccionada.")
        print("4. Añadir cancion seleccionada a una lista.")
        print("5. Ver mis listas de canciones.")
        print("6. Actualizar mi informacion.")
        print("7. Consultar planes premium.")
        print("8. Subscribirme a un plan premium.")
        print("\t0. Cerrar sesion.")
        case = input()
        
        if case == "1":
            listado = consulta_canciones(cur)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
            for fila in listado:
                mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
            print("Estas son las canciones que puedes elegir:")
            print(mi_tabla)
        
        elif case == "2":
            print("Escribe el nombre de la cancion que quieres buscar:")
            busqueda = input()
            listado = buscar_cancion(cur, busqueda)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[5], fila[4], fila[3]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("El termino que buscaste no ha encontrado resultados.")
        
        elif case == "3":
            print("Escriba el numero de la cancion que quiere reproducir:")
            codigo = input()
            if codigo.isdecimal():
                codigo = int(codigo)
                cancion = buscar_cancion_especifica(cur, codigo)
                reproductor(cur, cancion)
            else:
                print("El valor que ingreso no es un numero.")
                print("Accion no realizada.")
        
        elif case == "4":
            print("Escriba el numero de la cancion que quiere añadir:")
            codigo = input()
            print("Ingresa el nombre de la lista donde vas a agregar la cancion.")
            print("Si no hay una lista con ese nombre, se creara una nueva llamada asi.")
            nombreLista = input()
            if codigo.isdecimal():
                codigo = int(codigo)
                cancion = buscar_cancion_especifica(cur, codigo)
                if nombreLista:
                    datos = [nombreLista, data[0], cancion[0]]
                    agregar_cancion(con, cur, datos)
                    print("La cancion ha sido añadida a la lista")
                else:
                    print("No se le ha puesto un nombre a la lista.")
                    print("Accion no realizada.")
            else:
                print("El valor que ingreso no es un numero.")
                print("Accion no realizada.")
        
        elif case == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre de la Lista"]
            listado = consulta_usuario_listas(cur, data[0])
            if listado:
                for fila in listado:
                    mi_tabla.add_row(fila[0])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("El usuario no tiene listas de canciones.") 
        
        elif case == "6":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            correo = input("Ingrese su correo electronico: ")
            pais = input("Ingrese el nombre de la ciudad pais donde habita: ")
            ciudad = input("Ingrese el nombre de la ciudad donde habita: ")
            telefono = input("Ingrese su numero telefono: ")
            targetaCredito = input("Ingrese el numero de targeta de credito: ")
            if nombre.isalpha() and apellido.isalpha() and bool(correo):
                datos = [nombre, apellido, correo, pais, ciudad, telefono, targetaCredito, data[0]]
                actualizar_cliente(con, cur, datos)
                del nombre, apellido, correo, pais, ciudad, telefono, targetaCredito
            else:
                print("Alguno de los datos se ingresaron incorrectamente.")
        
        elif case == "7":
            listado = consulta_planes(cur)
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            for fila in listado:
                mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
            print("Estas son los planes a los que puedes subscribirte:")
            print(mi_tabla) 
        
        elif case == "8":
            print("Ingrese el nombre del plan al que se quiere subscribir:")
            nombre = input()
            if nombre.isalpha():
                datos = [data[0], nombre]
                agregar_subscripcion(con, cur, datos)
                print("Subscripcion añadida satisfactoriamente.")
            else:
                print("El nombre del plan que ingreso no es correcto.")
        
        elif case == "0":
            print("Sesion terminada.")
            print("Hasta Pronto.")
            break
        else:
            print("Entrada incorrecta. Intente otra vez.")

