import sqlite3
from sqlite3 import IntegrityError
from prettytable import PrettyTable
from correo import enviar_correo


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        conn = sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
        conn.execute("PRAGMA foreign_keys = 1")  # Activa la selectividad de las llaves foraneas.
        return conn
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.


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


    def ingresar_cancion_lista(self, con, cur) -> None:
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
        Lista de tuplas con los codigos de las canciones del cliente.
        """
        cur.execute("SELECT codigoCancion FROM listaCanciones WHERE cedulaCliente = ?", [cedula])
        return cur.fetchall()


    def consulta_lista_general(self, cur, campo="cedulaCliente") -> list:
        """       
        Consulta todos los datos de la tabla listaCanciones ordenandolos por el campo suministrado.
        Si no se proporciona un campo por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.

        Regresa:
        Lista de tuplas con toda la información de la tabla listaCanciones
        """
        cur.execute("SELECT * FROM listaCanciones ORDER BY {}".format(campo))
        return cur.fetchall()


    def borrar_lista_especifica(self, con, cur) -> None:
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


    def borrar_cancion_lista(self, con, cur) -> None:
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


    def borrar_lista_general(self, con, cur) -> None:
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
    

    def reproducir_lista_canciones(self, con, cur) -> None: pass
    

    def enviar_lista_canciones(self, nombre, correo, codigo_canciones) -> None:
        """
        Envia al correo del cliente los datos de su lista de canciones.

        Parametros:
        nombre (str): Nombre del cliente.
        correo (str): Correo del cliente.
        codigo_canciones (list): Lista con los codigos de su lista de canciones.
        """
        mi_tabla = PrettyTable()  # Crea el objeto tabla
        mi_tabla.title = f"Canciones de la lista {nombre}"  # Asgina un titulo a la tabla
        mi_tabla.field_names = ["No.", "Nombre", "Artista", "Album", "Genero"]  # Asgina los nombres de los campos en la tabla
        
        for codigo in codigo_canciones:
            print(codigo[0])
            # cancion = buscar_cancion_especifica(cur, codigo[0])
            # mi_tabla.add_row([cancion[0], cancion[1], cancion[5], cancion[4], cancion[3]])
            enviar_correo(correo, mi_tabla.get_html_string())


def menu_lista_canciones(con, cur):
    lista = ListaCanciones()

    while True:
        print("\nSeleccione que opciones desea ver:")
        print("1. Añadir canción a la lista.")
        print("2. Consulta general listas canciones.")
        print("3. Consulta especifica por cedula.")
        print("4. Eliminar canción de la lista.")
        print("5. Eliminar lista de canciones por cedula.")
        print("6. Eliminar tabla lista canciones.")
        print("7. Enviar lista al correo electronico.")
        print("8. Reproducir lista de canciones.")
        print("0. Salir del programa.")
        case = input()

        if case == "1":
            # Añadir canción a la lista
            print("Ingrese la cedula del cliente:")
            entrada_cedula = input()
            print("Ingrese el codigo de la canción:")
            entrada_codigo = input()

            # Verifica que las entradas sean enteros positivos
            if entrada_cedula.isdigit() and entrada_codigo.isdigit():
                # Se asignan los valores al objeto lista
                lista.cedula_cliente = int(entrada_cedula)
                lista.codigo_cancion = int(entrada_codigo)
                # Borrar las entradas ya que no se necesitan
                del entrada_cedula, entrada_codigo
                # Excepcion por si los datos no estan en la tabla cliente y cancion
                try:
                    # Llama a la funcion que agrega la cancion a la lista
                    lista.ingresar_cancion_lista(con, cur)
                except IntegrityError:
                    print("Los datos ingresados no corresponden a ningun cliente o canción.")
            else:
                print("Los datos que ingreso no son correctos.")

        elif case == "2":
            pass

        elif case == "3":
            pass

        elif case == "4":
            pass

        elif case == "5":
            pass

        elif case == "6":
            pass

        elif case == "7":
            pass

        elif case == "8":
            pass

        elif case == "0":
            print("\nSaliendo del menu lista canciones.")
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")


if __name__ == "__main__":
    conexion = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cursor = conexion.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.

    menu_lista_canciones(conexion, cursor)

    # mi_lista = lst1.consulta_lista_especifica(cur, lst1.cedula_cliente)
    # lst1.enviar_lista_canciones("Camilo", "camilo.londonom@gmail.com", mi_lista)



    # print(lst1.consulta_lista_especifica(cur, lst1.cedula_cliente))

    # print(lst1.consulta_lista_general(cur))
    # print(lst1.consulta_lista_general(cur, "codigoCancion"))

    # lst1.borrar_cancion_lista(con, cur)
    # lst1.borrar_lista_especifica(con, cur)
    # lst1.borrar_lista_general(con, cur)