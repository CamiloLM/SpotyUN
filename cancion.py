from sqlite3 import OperationalError
from prettytable import PrettyTable


class Cancion:
    def __init__(self):
        self.__codigo=None
        self.__nombre=None
        self.__ubicacion=None
        self.__genero=None 
        self.__album=None
        self.__interprete=None
        self.__fotografia=None

    def __str__(self) -> str:
        return (
            "Codigo: {}\nNombre: {}\nUbicación: {}\nGénero: {}\nAlbum: {}\nInterprete: {}\nFotografía: {}".format(
            self.__codigo, self.__nombre, self.__ubicacion, self.__genero, self.__album, self.__interprete, self.__fotografia))
    @property
    def datos_cancion(self):
        return self.__nombre,self.__ubicacion,self.__genero,self.__album,self.__interprete,self.__fotografia
    @property
    def codigo(self):
        return self.__codigo

    @datos_cancion.setter
    def datos_cancion(self,listaValores):
         self.__nombre,self.__ubicacion,self.__genero,self.__album,self.__interprete,self.__fotografia = listaValores
    @codigo.setter
    def codigo(self,codigo):
         self.__codigo = codigo

    
    def insertar_cancion(self, con, cur):
        """
        Ingresa datos en la tabla cancion, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cancion=[self.__codigo,self.__nombre,self.__ubicacion,self.__genero,self.__album,self.__interprete,self.__fotografia]
        cur.execute("INSERT OR IGNORE INTO cancion VALUES (?, ?, ?, ?, ?, ?, ?)", cancion)
        con.commit() 
        return cur.rowcount   
 
    def consulta_canciones(self, cur, campo="codigo"):
        """
        Consulta todos los datos de la tabla cancion
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        limite (int): Limite de canciones por plan
        """
        cur.execute("SELECT * FROM cancion ORDER BY {}".format(campo))
        return cur.fetchall()

    def buscar_cancion_especifica(self, cur):
        """
        Consulta una cancion por su codigo.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        codigo (int): Codigo de la cancion.
        """
        datos = [self.__codigo]
        cur.execute("SELECT * FROM cancion WHERE codigo = ?", datos)
        return cur.fetchone()    

    def actualizar_cancion(self, con, cur):
        """
        Actualiza datos en la tabla cancion, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        valores = [self.__nombre,self.__ubicacion,self.__genero,self.__album,self.__interprete,self.__fotografia,self.__codigo]
        cur.execute('''
            UPDATE OR IGNORE cancion
            SET nombre = ?,
            ubicacion = ?,
            genero = ?,
            album = ?,
            interprete = ?,
            fotografia = ?
            WHERE codigo = ?''', valores)
        con.commit()
        return cur.rowcount  

    def borrar_cancion(self, con, cur):
        """
        Borra un registro en la tabla cancion.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        codigo (int): Codigo de la cancion.
        """
        cur.execute("DELETE FROM cancion WHERE codigo = ?", [self.__codigo])
        con.commit()
        return cur.rowcount  

    def borrar_canciones(self, con, cur):
        """
        Borra todos los registros en la tabla cancion

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM cancion")
        con.commit()
        return cur.rowcount  


def menu_cancion(con, cur):
    cancion = Cancion()

    while True:
        # TODO: Buscar cancion por nombre
        print("\nSeleccione que opciones desea realizar:")
        print("1. Añadir nueva canción.")
        print("2. Consulta general canciones.")
        print("3. Consulta especifica canciones.")
        print("4. Actualizar canción.")
        print("5. Eliminar canción.")
        print("6. Eliminar canciones.")
        print("0. Salir del menu canciones.")
        case = input()

        if case == "1":
            # Ingresando una nueva cancion
            nombre = input("\nIngrese nombre de la canción: ").strip()
            ubicacion = input("Ingrese ubicación: ").strip()
            genero = input("Ingrese género: ").strip()
            album = input("Ingrese album: ").strip()
            interprete = input("Ingrese el interprete de la canción: ").strip()
            fotografia = input("Ingrese la fotografía del album: ").strip()

            # Verficacion de que los datos que son ingresados son correctos
            if nombre and ubicacion and genero and album and interprete and fotografia:
                cancion.datos_cancion = [nombre, ubicacion, genero, album, interprete, fotografia]  # Actualiza los datos del objeto canción
                cancion.codigo=None
                # Se borran las variables que ya no se utilizan
                del nombre, ubicacion, genero, album, interprete

                # Llama al metodo para ingresar la cancion en la base de datos
                cambios = cancion.insertar_cancion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nCanción ingresada con exito.")
                else:
                    print("\nLa canción ya esta registrada, no se han realizado cambios.")
            else:
                print("\nAlguno de los datos que ingreso no son correctos")


        elif case == "2":
            # Consulta general de canciones por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Codigo", "Nombre", "Ubicación", "Género", "Album", "Interprete", "Fotografía"]  # Asgina los nombres de los campos en la tabla
            campo = "codigo"  # Campo por el que se va a ordenar

            # Bucle para poder ordenar las busquedas por campos
            while True:
                # Excepcion por si se ingresan campos que no esten en la tabla
                try:
                    # Busqueda en la tabla canción general pasando el campo por el que ordena
                    datos_cancion = cancion.consulta_canciones(cur, campo)
                    
                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_cancion:
                        mi_tabla.add_rows(datos_cancion)  # Añade datos las filas a la tabla
                        print("")
                        print(mi_tabla)
                        bandera = input("Desea ordenar la busqueda por un campo (S/n): ")

                        # Bandera logica por si se quiere ordenar un campo
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            entrada = input("Ingrese el campo por el que quiere ordenar la busqueda: ").lower()  # Entrada en minisculas
                            campo = entrada.replace(" ", "")  # Si se ingresan espacios estos se remueven
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        break
                except OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha proporcionado.")
                    break

        elif case == "3":
            # Consulta especifica de canciones por codigo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Codigo", "Nombre", "Ubicación", "Género", "Album", "Interprete", "Fotografía"] # Asigna los nombres de los campos en la tabla

            codigo = input("\nIngrese el codigo: ")
            # Verficacion de los datos que son ingresados son correctos
            if codigo.isdigit():
                # Actualiza el codigo del objeto canción
                cancion.codigo = int(codigo)
                # Almacena todos los datos de la canción
                datos_cancion = cancion.buscar_cancion_especifica(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_cancion:
                    mi_tabla.add_row(datos_cancion)  # Añade datos las filas a la tabla
                    print("")
                    print(mi_tabla)
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor del codigo ingresado no es valido")  


        elif case == "4":
            # Actualizar los datos de canción
            print("\nIngrese los datos nuevos de la nueva canción")
            nombre = input("\nIngrese nombre de la canción: ").strip()
            ubicacion = input("Ingrese ubicación: ").strip()
            genero = input("Ingrese género: ").strip()
            album = input("Ingrese album: ").strip()
            interprete = input("Ingrese el interprete de la canción: ").strip()
            fotografia = input("Ingrese la fotografia del album: ").strip()

            print("\nIngrese el codigo de la canción que va a modificar:")
            codigo = input()

            # Verficacion de que los datos que son ingresados son correctos
            if nombre and ubicacion and genero and album and interprete and fotografia and codigo.isdigit():
                cancion.datos_cancion = [nombre, ubicacion, genero, album, interprete, fotografia]  # Actualiza los datos del objeto canción
                cancion.codigo = int(codigo)
                # Se borran las variables que ya no se utilizan
                del nombre, ubicacion, genero, album, interprete

                # Llama al metodo para ingresar la cancion en la base de datos
                cambios = cancion.actualizar_cancion(con, cur)
                

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nActualización realizada con exito.")
                else:
                    print("\nEsa canción no esta registrada, no se han realizado cambios.")

        elif case == "5":
            # Eliminar datos especificos de la tabla canción
            print("\nIngrese el codigo de la canción que va a eliminar:")
            codigo = input()

            if codigo.isdigit():
                cancion.codigo = int(codigo)

                del codigo  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza la canción en la base de datos
                cambios = cancion.borrar_cancion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nCanción eliminada con exito.")
                else:
                    print("\nEse codigo no esta registrado, no se han realizado cambios.") 

        elif case == "6":
            # Eliminar datos generales de la tabla canción
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = cancion.borrar_canciones(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nTodos los datos de la tabla canción han sidos eliminados.")
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")

        elif case == "0":
            print("\nSaliendo del menu canción.")
            break

        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")                       
