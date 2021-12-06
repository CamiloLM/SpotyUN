from prettytable import PrettyTable
import crud.read
import crud.insert


def consultas_general(cur):
    while True:
        print("\nSeleccione las consultas")
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
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "2":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Targeta credito", "Fecha Pago", "Pago"]
            listado = crud.read.consulta_clientes(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "3":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            listado = crud.read.consulta_planes(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "4":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula cliente", "Nombre plan"]
            listado = crud.read.consulta_subscripciones(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre lista", "Cedula", "Codigo"]
            listado = crud.read.consulta_general_listas(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "6":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]
            listado = crud.read.consulta_admins(cur)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2], fila[3]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "0":
            break

        else:
            print("Numero equivocado.")


def consultas_especificas(cur):
    while True:
        print("\nSeleccione las consultas")
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
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "2":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Targeta credito", "Fecha Pago", "Pago"]
            cedula = input("Cedula del cliente: ")
            lista = crud.read.buscar_cliente(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "3":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre", "Valor", "Cantidad", "Descripcion"]
            nombre = input("Nombre del plan: ")
            lista = crud.read.buscar_plan(cur, nombre)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "4":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula cliente", "Nombre plan"]
            cedula = input("Cedula del cliente: ")
            lista = crud.read.buscar_subscripcion(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "5":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Nombre lista", "Cedula", "Codigo"]
            cedula = input("Cedula del cliente: ")
            listado = crud.read.consulta_usuario_listas(cur, cedula)
            if listado:
                for fila in listado:
                    mi_tabla.add_row([fila[0], fila[1], fila[2]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "6":
            mi_tabla = PrettyTable()
            mi_tabla.field_names = ["Cedula", "Nombre", "Apellido", "Correo"]
            cedula = input("Cedula del administrador: ")
            lista = crud.read.buscar_admin(cur, cedula)
            if lista:
                mi_tabla.add_row([lista[0], lista[1], lista[2], lista[3]])
                print("Estos son los resultados:")
                print(mi_tabla)
            else:
                print("La tabla no tiene datos")
        
        elif select == "0":
            break

        else:
            print("Numero equivocado.")


def insertar_datos(con, cur):
    while True:
        print("\nSeleccione la accion que desea realizar")
        print("1. Insertar cancion.")
        print("2. Insertar cliente.")
        print("3. Insertar plan.")
        print("4. Insertar subscripcion.")
        print("5. Insertar administrador.")
        print("0. Salir")
        select = input()

        if select == "1":
            nombre = input("Ingrese nombre: ")
            ubicacion = input("Ingrese ubicacion: ")
            genero = input("Ingrese genero: ")
            album = input("Ingrese album: ")
            interprete = input("Ingrese interprete: ")

            datos = [None, nombre, ubicacion, genero, album, interprete]
            crud.insert.insertar_cancion(con, cur, datos)

        elif select == "2":
            cedula = input("Ingrese cedula: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            correo = input("Ingrese correo electronico: ")
            pais = input("Ingrese pais: ")
            ciudad = input("Ingrese ciudad: ")
            telefono = input("Ingrese telefono: ")
            targetaCredito = input("Ingrese targeta redito: ")
            fechaPago = input("Ingrese fecha pago: ")
            pago = input("Ingrese pago: ")

            datos = [int(cedula), nombre, apellido, correo, pais, ciudad, int(telefono), int(targetaCredito), fechaPago, int(pago)]
            crud.insert.insertar_cliente(con, cur, datos)
        
        elif select == "3":
            nombre = input("Ingrese nombre: ")
            valor = input("Ingrese valor: ")
            cantidad = input("Ingrese cantidad: ")
            descripcion = input("Ingrese descripcion: ")

            datos = [nombre, valor, cantidad, descripcion]
            crud.insert.insertar_plan(con, cur, datos)

        
        elif select == "4":
            cedulaCliente = input("Ingrese cedula cliente: ")
            nombrePlan = input("Ingrese nombre plan: ")
        
            datos = [cedulaCliente, nombrePlan]
            crud.insert.agregar_subscripcion(con, cur, datos)
        
        elif select == "5":
            cedula = input("Ingrese cedula: ")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            correo = input("Ingrese correo electronico: ")

            datos = [int(cedula), nombre, apellido, correo]
            crud.insert.insertar_admin(con, cur, datos)
        
        elif select == "0":
            break

        else:
            print("Numero equivocado.")


def admin_logueado(con, cur, data):
    print(f"Bienvenido Administrador {data[1]} {data[2]}")
    while True:
        print("\nSeleccione la accion que desea realizar")
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
            print("Sesion terminada.")
            break

        else:
            print("Entrada incorrecta. Intente otra vez.")
