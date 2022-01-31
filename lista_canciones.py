from sqlite3 import IntegrityError, OperationalError
from prettytable import PrettyTable
from correo import enviar_correo
from player import reproductor
from cancion import Cancion
from cliente import Cliente
# from planes import Plan


class ListaCanciones():
    def __init__(self):
        self.__cedula_cliente = None
        self.__codigo_cancion = None


    def __str__(self) -> str:
        return "Cedula: {}\nCodigo: {}".format(self.__cedula_cliente, self.__codigo_cancion)


    @property
    def cedula_cliente(self) -> int:
        return self.__cedula_cliente


    @cedula_cliente.setter
    def cedula_cliente(self, cedula) -> None:
        self.__cedula_cliente = cedula


    @property
    def codigo_cancion(self) -> int:
        return self.__codigo_cancion


    @codigo_cancion.setter
    def codigo_cancion(self, codigo) -> None:
        self.__codigo_cancion = codigo


    def ingresar_cancion_lista(self, con, cur) -> int:
        """
        Agrega una cancion a la tabla listaCanciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self.__cedula_cliente, self.__codigo_cancion
        cur.execute("INSERT OR IGNORE INTO listaCanciones VALUES (?, ?)", datos)
        con.commit()
        return cur.rowcount


    def consulta_lista_especifica(self, cur, cedula) -> list:
        """
        Consulta los codigos de la lista canciones por la cedula del cliente.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedula (int): Cedula del cliente.

        Regresa:
        datos_lista (list): Lista de tuplas con los datos de lista canciones del cliente.
        """
        cur.execute("SELECT * FROM listaCanciones WHERE cedulaCliente = ?", [cedula])
        return cur.fetchall()


    def consulta_lista_general(self, cur, campo="cedulaCliente") -> list:
        """       
        Consulta todos los datos de la tabla listaCanciones ordenandolos por el campo suministrado.
        Si no se proporciona un campo por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.

        Regresa:
        datos_lista (list): Lista de tuplas con toda la información de la tabla listaCanciones
        """
        cur.execute("SELECT * FROM listaCanciones ORDER BY {}".format(campo))
        return cur.fetchall()


    def borrar_lista_especifica(self, con, cur) -> int:
        """
        Borra un registro en la tabla listaCanciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM listaCanciones WHERE cedulaCliente = ?", [self.__cedula_cliente])
        con.commit()
        return cur.rowcount


    def borrar_cancion_lista(self, con, cur) -> int:
        """
        Borra un registro en la tabla listaCanciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self.__cedula_cliente, self.__codigo_cancion
        cur.execute("DELETE FROM listaCanciones WHERE cedulaCliente = ? AND codigoCancion = ?", datos)
        con.commit()
        return cur.rowcount


    def borrar_lista_general(self, con, cur) -> int:
        """
        Borra todos los registros en la tabla listaCanciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM listaCanciones")
        con.commit()
        return cur.rowcount


def menu_lista_canciones(con, cur):
    lista = ListaCanciones()

    while True:
        print("\nSeleccione que opciones desea realizar:")
        print("1. Añadir canción a una lista.")
        print("2. Consulta general listas de canciones.")
        print("3. Consulta especifica lista de canciones.")
        print("4. Eliminar canción de una lista.")
        print("5. Eliminar una lista de canciones.")
        print("6. Eliminar tabla lista de canciones.")
        print("7. Enviar lista al correo electronico.")
        print("8. Reproducir lista de canciones.")
        print("0. Salir del programa.")
        case = input()


        if case == "1":
            # Añadir canción a una lista especificada por la cedula
            cedula = input("Ingrese la cedula del cliente: ")
            codigo = input("Ingrese el codigo de la canción: ")

            # Verifica que las entradas sean enteros positivos
            if cedula.isdigit() and codigo.isdigit():
                cedula = int(cedula)
                codigo = int(codigo)
                
                # TODO: Consultar el limite de canciones del cliente
                # Verifica que el usuario no tenga la cancion ya agregada a la lista
                datos_lista = lista.consulta_lista_especifica(cur, cedula)
                if codigo not in (elem for datos_cancion in datos_lista for elem in datos_cancion):
                    # Se asignan los valores al objeto lista
                    lista.cedula_cliente = cedula
                    lista.codigo_cancion = codigo

                    # Borrar las entradas ya que no se necesitan
                    del cedula, codigo

                    # Excepcion por si los datos no estan en la tabla cliente y cancion
                    try:
                        # Llama a la funcion que agrega la cancion a la lista
                        cambios = lista.ingresar_cancion_lista(con, cur)
                        
                        # Verifica si se realizaron cambios en la base de datos
                        if cambios != 0:
                            print("\nCanción agredaga con exito.")
                    except IntegrityError:
                        print("Los datos ingresados no corresponden a ningun cliente o canción.")
                else:
                    print("La canción que ingreso ya ha sido agregada")
            else:
                print("Los datos que ingreso no son correctos, ingrese enteros positivos.")


        elif case == "2":
            # Consulta general de lista de canciones por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            # Asgina los nombres de los campos en la tabla
            mi_tabla.field_names = ["cedulaCliente", "codigoCancion"]
            campo = "cedulaCliente"  # Campo por el que se va a ordenar

            while True:
                # Excepcion por si se ingresan un campo que no este en la tabla
                try:
                    # Busqueda general en la tabla lista canciones pasando el campo por el que ordena
                    datos_lista = lista.consulta_lista_general(cur, campo)

                    if datos_lista:
                        mi_tabla.add_rows(datos_lista)  # Añade datos las filas a la tabla

                        print("")
                        print(mi_tabla)  # Imprime la tabla con los datos añadidos

                        # Bandera logica por si se quiere ordenar un campo
                        bandera = input("Desea ordenar la busqueda por un campo (S/n): ")
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            campo = input("Ingrese el campo por el que quiere ordenar la busqueda: ").strip()
                            print(campo)
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        break
                except OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha ingresado.")
                    break


        elif case == "3":
            # Consulta especifica de la lista de canciones por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Codigo", "Nombre", "Ubicación", "Género", "Album", "Interprete", "Fotografía"]

            cedula = input("\nIngrese número de cedula: ")
            # Verficacion de los datos que son ingresados son correctos
            if cedula.isdigit():
                # Actualiza la cedula del objeto cliente
                lista.cedula_cliente = int(cedula)
                # Almacena los datos de la lita del cliente
                datos_lista = lista.consulta_lista_especifica(cur, lista.cedula_cliente)

                # Si la busqueda encuentra resultados se busca la informacion de la cancion
                if datos_lista:
                    cancion = Cancion()  # Crea un objeto cancion para realizar la busqueda

                    for elem in datos_lista:
                        cancion.codigo = elem[1]  # Asigna los codigos de la lista al objeto cancion
                        datos_cancion = cancion.buscar_cancion_especifica(cur)
                        mi_tabla.add_row(datos_cancion)  # La informacion de cada cancion se agrega a la tabla

                    print("")
                    print(mi_tabla)  # Imprime los datos de la tabla
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor de la cedula ingresada no es valido")


        elif case == "4":
            # Eliminar canción a una lista especificada por la cedula
            cedula = input("\nIngrese la cedula del cliente que corresponde a la lista: ")
            codigo = input("Ingrese el codigo de la canción que va a eliminar: ")

            if cedula.isdigit() and codigo.isdigit():
                lista.cedula_cliente = int(cedula)
                lista.codigo_cancion = int(codigo)

                del cedula, codigo  # Se borran las variables que no se van a utilizar

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = lista.borrar_cancion_lista(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nCancion eliminada con exito.")
                else:
                    print("\nEl cliente no tiene agregada la canción a su lista, no se han realizado cambios.")


        elif case == "5":
            # Eliminar lista de canciones especificada por la cedula
            cedula = input("\nIngrese la cedula del cliente que corresponde a la lista: ")

            if cedula.isdigit():
                lista.cedula_cliente = int(cedula)

                del cedula  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza el usuario en la base de datos
                cambios = lista.borrar_lista_especifica(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nLista de canciones eliminada con exito.")
                else:
                    print("\nEl cliente no tiene una lista de canciones, no se han realizado cambios.")


        elif case == "6":
            # Eliminar datos completos de la tabla lista canciones
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = lista.borrar_lista_general(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nTodos los datos de la tabla cliente han sidos eliminados.")
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")


        elif case == "7":
            # Envia al correo del cliente los datos de su lista de canciones.
            cedula = input("Ingrese la cedula del cliente: ")
            
            if cedula.isdigit():
                cedula = int(cedula)
                # Consulta si el cliente tiene canciones agregadas en la lista
                datos_lista = lista.consulta_lista_especifica(cur, cedula)
                if datos_lista:
                    # Creacion del objeto cliente para realizar busquedas
                    cliente = Cliente()
                    cliente.cedula = cedula
                    # Consulta de datos del cliente por la cedula suministrada
                    datos_cliente = cliente.consulta_usuario_especifica(cur)
                    
                    # Creacion de la tabla que se va a enviar
                    mi_tabla = PrettyTable()  # Crea el objeto tabla
                    mi_tabla.title = f"Lista de canciones de {datos_cliente[1]} {datos_cliente[2]}"  # Asgina un titulo a la tabla
                    mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]  # Asgina los nombres de los campos en la tabla

                    # Creacion del objeto canción para realizar busquedas
                    cancion = Cancion()
                    # Itera en una lista compresible los codigos de las canciones
                    for codigo in [elem[1] for elem in datos_lista]:
                        cancion.codigo = codigo
                        # Consulta de la información de las canciones
                        datos_cancion = cancion.buscar_cancion_especifica(cur)
                        mi_tabla.add_row([datos_cancion[0], datos_cancion[1], datos_cancion[5], datos_cancion[4], datos_cancion[3]])

                    del cedula, cliente, datos_cliente, cancion, datos_cancion
                    # Consulta si pudo realizar el envio del mensaje
                    envio = enviar_correo(datos_cliente[3], mi_tabla.get_html_string())
                    if envio:
                        print("\nCorreo enviado con exito.")
                    else:
                        print("\nNo se pudo enviar el correo, las credenciales no fueron aceptadas")
                else:
                    print("\nEl cliente no tiene canciones agregadas")
            else:
                print("\nLa cedula que ingreso no es correcta.")


        elif case == "8":
            # Reprodución de las canciones almacenadas en la lista
            # TODO: Comprobar que pasa si la cancion no tiene una ubicacion
            cedula = input("Ingrese la cedula del cliente: ")
            
            # Verificancion de que la entrada es un entero positivo
            if cedula.isdigit():
                cedula = int(cedula)
                # Consulta si el cliente tiene canciones agregadas en la lista
                datos_lista = lista.consulta_lista_especifica(cur, cedula)
                if datos_lista:
                    lista_cancion = []  # Lista para almacenar los datos de las canciones
                    cancion = Cancion()
                    for codigo in [elem[1] for elem in datos_lista]:
                        cancion.codigo = codigo
                        # Consulta de la informacion de cada cancion
                        lista_cancion.append(cancion.buscar_cancion_especifica(cur))
                    # Se envia la lista completa de canciones al reproductor
                    reproductor(lista_cancion)
                else:
                    print("\nEl cliente no tiene canciones agregadas")
            else:
                print("\nLa cedula que ingreso no es correcta.")


        elif case == "0":
            print("\nSaliendo del menu lista canciones.")
            break


        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")
