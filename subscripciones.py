from sqlite3 import IntegrityError, OperationalError
from prettytable import PrettyTable
from planes import Plan


class Subscripciones:
    def __init__(self):
        self.__cedulaCliente = None
        self.__codigoPlan = None


    def __str__(self) -> str:
        return "\nCedula del cliente: {}\nCodigo del plan: {}".format(self.__cedulaCliente, self.__codigoPlan)


    @property
    def cedulaCliente(self):
        return self.__cedulaCliente


    @property
    def codigoPlan(self):
        return self.__codigoPlan


    @cedulaCliente.setter
    def cedulaCliente(self, cedula):
        self.__cedulaCliente = cedula


    @codigoPlan.setter
    def codigoPlan(self, codigo):
        self.__codigoPlan = codigo
  
        
    def ingresar_subscripcion(self, con, cur) -> int:
        """
        Agrega los datos de una subscripción.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = [self.__cedulaCliente, self.__codigoPlan]
        cur.execute("INSERT OR IGNORE INTO subscripciones VALUES (?, ?)", datos)
        con.commit()
        return cur.rowcount     


    def consulta_subscripcion_general(self, cur, campo="cedulaCliente") -> list:
        """
        Consulta todos los datos de la tabla subscripciones ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por cedulaCliente
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar..
        
        Regresa:
        datos_subs (list): Lita de tuplas con todos los datos de las subscripciones.
        """
        cur.execute("SELECT * FROM subscripciones ORDER BY {}".format(campo))
        return cur.fetchall()  


    def consulta_subscripcion_especifica(self, cur) -> list:
        """
        Consulta una subscripcion por cedulaCliente.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_subs (list): Todos los datos de las subscripciones.
        """
        cur.execute("SELECT * FROM subscripciones WHERE cedulaCliente = ?", [self.__cedulaCliente])
        return cur.fetchone() 


    def actualizar_subscripcion(self, con, cur) -> int:
        """
        Actualiza los datos en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = [self.__codigoPlan, self.__cedulaCliente]
        cur.execute('''
            UPDATE OR IGNORE subscripciones
            SET codigoPlan = ?
            WHERE cedulaCliente = ?''', datos)
        con.commit() 
        return cur.rowcount   


    def borrar_subscripcion_especifica(self, con, cur) -> int:
        """
        Borra un registro en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        
        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM subscripciones WHERE cedulaCliente = ?", [self.__cedulaCliente])
        con.commit()
        return cur.rowcount      


    def borrar_subscripcion_general(self, con, cur) -> int:
        """
        Borra todo los registro en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM subscripciones")
        con.commit()
        return cur.rowcount       


def menu_subscripción(con, cur):
    subscripciones = Subscripciones()

    while True:
        print("\nSeleccione que opciones desea realizar:")
        print("1. Añadir nueva subscripción.")
        print("2. Consulta general subscripciones.")
        print("3. Consulta especifica subscripciones.")
        print("4. Actualizar subscripción.")
        print("5. Eliminar subscripción.")
        print("6. Eliminar subscripciones")
        print("0. Salir del menu subscripciones.")
        case = input()


        if case == "1":
            # Ingresando una nueva subscripción
            cedula = input("\nIngrese la cedula del cliente: ")
            codigo = input("Ingrese codigo del plan: ")

            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and codigo.isdigit():
                subscripciones.cedulaCliente = int(cedula)
                subscripciones.codigoPlan = int(codigo)
                # Se borran las variables que ya no se utilizan
                del cedula, codigo

                # Excepcion por si los datos no estan en la tabla cliente y cancion
                try:
                    # Llama al metodo para ingresar la subscripción en la base de datos
                    cambios = subscripciones.ingresar_subscripcion(con, cur)

                    # Verifica si se realizaron cambios en la base de datos
                    if cambios != 0:
                        print("\nSubscripción ingresada con exito.")
                    else:
                        print("\nLa subscripción ya esta registrada, no se han realizado cambios.")
                except IntegrityError:
                        print("Los datos ingresados no corresponden a ningun cliente o plan.")
            else:
                print("\nAlguno de los datos que ingreso no son correctos")


        elif case == "2":
            # Consulta general de subscripciones por campo
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["cedulaCliente","codigoPlan"]  # Asgina los nombres de los campos en la tabla
            campo = "cedulaCliente"  # Campo por el que se va a ordenar

            # Bucle para poder ordenar las busquedas por campos
            while True:
                # Excepcion por si se ingresan campos que no esten en la tabla
                try:
                    # Busqueda en la tabla canción general pasando el campo por el que ordena
                    datos_subs = subscripciones.consulta_subscripcion_general(cur, campo)
                    
                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_subs:
                        mi_tabla.add_rows(datos_subs)  # Añade datos las filas a la tabla
                        print("")
                        print(mi_tabla)
                        bandera = input("Desea ordenar la busqueda por un campo (S/n): ")

                        # Bandera logica por si se quiere ordenar un campo
                        if bandera == "S" or bandera == "s":
                            mi_tabla.clear_rows()  # Se limpia los datos en las filas
                            campo = input("Ingrese el campo por el que quiere ordenar la busqueda: ").strip()
                        else:
                            break
                    else:
                        print("\nLa tabla no tiene datos")
                        break
                except OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha proporcionado.")
                    break


        elif case == "3":
            # Consulta especifica de subscripciones por cedula
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["Código", "Nombre", "Valor", "Cantidad Canciones"]

            cedula = input("\nIngrese la cédula: ")
            # Verficacion de los datos que son ingresados son correctos
            if cedula.isdigit():
                # Actualiza el codigo del objeto canción
                subscripciones.cedulaCliente = int(cedula)
                # Almacena todos los datos de la canción
                datos_subs = subscripciones.consulta_subscripcion_especifica(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_subs:
                    plan = Plan()

                    plan.setcodigo(datos_subs[1])
                    datos_plan = plan.consulta_plan_especifica(cur)
                    mi_tabla.add_row(datos_plan)
                    
                    print("")
                    print(mi_tabla)
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor de la cedula ingresada no es valido")  


        elif case == "4":
            # Actualizar los datos de canción
            print("\nIngrese los datos nuevos de la nueva subscripción")
            cedula = input("\nIngrese la cédula del cliente: ")
            codigo = input("Ingrese el codigo del plan: ")

            # Verficacion de que los datos que son ingresados son correctos
            if cedula.isdigit() and codigo.isdigit():
                subscripciones.cedulaCliente = int(cedula)
                subscripciones.codigoPlan = int(codigo)

                # Se borran las variables que ya no se utilizan
                del cedula, codigo

                # Llama al metodo para ingresar la subscripción en la base de datos
                cambios = subscripciones.actualizar_subscripcion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nActualización realizada con exito.")
                else:
                    print("\nEsa cédula no esta registrada, no se han realizado cambios.")


        elif case == "5":
            # Eliminar datos especificos de la tabla subscripciones
            cedula = input("\nIngrese la cédula de la subscripción que va a eliminar: ")

            if cedula.isdigit():
                subscripciones.cedulaCliente = int(cedula)

                del cedula  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza la subscripción en la base de datos
                cambios = subscripciones.borrar_subscripcion_especifica(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nSubscripción eliminada con exito.")
                else:
                    print("\nEsa cédula no tiene un plan registrado, no se han realizado cambios.") 


        elif case == "6":
            # Eliminar datos generales de la tabla subscripción
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = subscripciones.borrar_subscripcion_general(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nTodos los datos de la tabla subscripciones han sidos eliminados.")
                else:
                    print("\nAlgo ha ido mal, no se han realizado cambios.")


        elif case == "0":
            print("\nSaliendo del menu subscripción.")
            break


        else:
            print("\nEntrada incorrecta. Por favor, intente otra vez.")              
