# La tabla de este objeto fue modificada, ahora uno de sus campos referencia al codigo del plan correspondiente.
# No es un acambio grande solo hay que cambiar el nombre del campo en los execute.
from operator import sub
import sqlite3
from prettytable import PrettyTable

def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        return sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.

class Subscripciones:
    def __init__(self):
        self.__cedulaCliente=None
        self.__codigoPlan=None

    def __str__(self) -> str:
        return (
            "cedulaCliente: {}\ncodigoPlan: {}".format(
            self.__cedulaCliente, self.__codigoPlan))    

    @property
    def datos_subscripcion(self):
        return self.__cedulaCliente,self.__codigoPlan
    @property
    def codigo(self):
        return self.__cedulaCliente

    @datos_subscripcion.setter
    def datos_subscripcion(self,listaValores):
         self.__cedulaCliente,self.__codigoPlan = listaValores
    @codigo.setter
    def codigo(self,cedula):
         self.__cedulaCliente = cedula
  
        
    def agregar_subscripcion(self, con, cur):
        """
        Agrega un cliente a un plan, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cliente (list): cedulaCliente, codigoPlan.
        """
        datos=[self.__cedulaCliente,self.__codigoPlan]
        cur.execute("INSERT OR IGNORE INTO subscripciones VALUES (?, ?)", datos)
        con.commit()
        return cur.rowcount     

    def consulta_subscripciones(self, cur, campo="cedulaCliente"):
        """Consulta todos los datos de la tabla subscripciones"""
        cur.execute("SELECT * FROM subscripciones ORDER BY {}".format(campo))
        return cur.fetchall()  

    def buscar_subscripcion(self, cur):
        """
        Consulta un plan por su nombre.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedulaCliente (int): Cedula del cliente
        """
        datos = [self.__cedulaCliente]
        cur.execute("SELECT * FROM subscripciones WHERE cedulaCliente = ?", datos)
        return cur.fetchone() 

    def actualizar_subscripcion(self, con, cur):
        """
        Actualiza los datos en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        datos (list): Codigo del plan (int), cedula del cliente (int).
        """
        datos = [self.__codigoPlan,self.__cedulaCliente]
        cur.execute('''
            UPDATE OR IGNORE subscripciones
            SET codigoPlan = ?
            WHERE cedulaCliente = ?''', datos)
        con.commit() 
        return cur.rowcount   

    def borrar_subscripcion(self, con, cur):
        """
        Borra un registro en la tabla subscripciones, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedulaCliente (int): Cedula del cliente.
        nombrePlan (str): Codigo del plan exactamente como aparece en a base.
        """
        cur.execute("DELETE FROM subscripciones WHERE cedulaCliente = ?", [self.__cedulaCliente])
        con.commit()
        return cur.rowcount      

    def borrar_subscripciones(self, con, cur):
        """
        Borra todo el registro en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
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
        print("0. Salir del programa.")
        case = input()

        if case == "1":
            # Ingresando una nueva subscripción
            cedulaCliente = input("\nIngrese su cedula : ")
            codigoPlan = input("Ingrese codigo para el plan: ")

            # Verficacion de que los datos que son ingresados son correctos
            if cedulaCliente.isdigit() and codigoPlan.isdigit():
                subscripciones.datos_subscripcion = [cedulaCliente, codigoPlan]  # Actualiza los datos del objeto subscripciones
                # Se borran las variables que ya no se utilizan
                del cedulaCliente, codigoPlan

                # Llama al metodo para ingresar la subscripción en la base de datos
                cambios = subscripciones.agregar_subscripcion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nSubscripción ingresada con exito.")
                else:
                    print("\nLa subscripción ya esta registrada, no se han realizado cambios.")
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
                    datos_subscripciones = subscripciones.consulta_subscripciones(cur, campo)
                    
                    # Si la busqueda encuentra resultados estos se representan en la tabla
                    if datos_subscripciones:
                        mi_tabla.add_rows(datos_subscripciones)  # Añade datos las filas a la tabla
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
                except sqlite3.OperationalError:
                    print("\nLa tabla no cuenta con el campo que ha proporcionado.")
                    break
        
        elif case == "3":
            # Consulta especifica de subscripciones por cedula
            mi_tabla = PrettyTable()  # Crea el objeto tabla
            mi_tabla.field_names = ["CedulaCliente", "codigoPlan"] # Asigna los nombres de los campos en la tabla

            cedula = input("\nIngrese la cédula: ")
            # Verficacion de los datos que son ingresados son correctos
            if cedula.isdigit():
                # Actualiza el codigo del objeto canción
                subscripciones.codigo = int(cedula)
                # Almacena todos los datos de la canción
                datos_subscripcion = subscripciones.buscar_subscripcion(cur)

                # Si la busqueda encuentra resultados estos se representan en la tabla
                if datos_subscripcion:
                    mi_tabla.add_row(datos_subscripcion)  # Añade datos las filas a la tabla
                    print("")
                    print(mi_tabla)
                else:
                    print("\nLa tabla no tiene datos")
            else:
                print("\nEl valor de la cedula ingresada no es valido")  

        elif case == "4":
            # Actualizar los datos de canción
            print("\nIngrese los datos nuevos de la nueva subscripción")
            cedulaCliente = input("\nIngrese su cédula: ")
            codigoPlan = input("Ingrese codigo del plan: ")

            print("\nIngrese la cedula de la subscripción que va a modificar:")
            cedula = input()

            # Verficacion de que los datos que son ingresados son correctos
            if cedulaCliente.isdigit() and codigoPlan.isdigit():
                subscripciones.datos_subscripcion = [cedulaCliente, codigoPlan]  # Actualiza los datos del objeto subscripciones
                subscripciones.cedula = int(cedula)
                # Se borran las variables que ya no se utilizan
                del cedulaCliente, codigoPlan

                # Llama al metodo para ingresar la subscripción en la base de datos
                cambios = subscripciones.actualizar_subscripcion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nActualización realizada con exito.")
                else:
                    print("\nEsa cédula no esta registrada, no se han realizado cambios.")
        
        elif case == "5":
            # Eliminar datos especificos de la tabla subscripciones
            print("\nIngrese la cédula de la subscripción que va a eliminar:")
            cedula = input()

            if cedula.isdigit():
                subscripciones.cedula = int(cedula)

                del cedula  # Se borra la variable que no se va a utilizar

                # Llama al metodo que actualiza la subscripción en la base de datos
                cambios = subscripciones.borrar_subscripcion(con, cur)

                # Verifica si se realizaron cambios en la base de datos
                if cambios != 0:
                    print("\nSubscripción eliminada con exito.")
                else:
                    print("\nEsa cédula no esta registrada, no se han realizado cambios.") 

        elif case == "6":
            # Eliminar datos generales de la tabla subscripción
            bandera = input("Esta seguro que desea realizar esta acción, los datos se perderan (S/n): ")

            # Bandera logica por si se quiere ordenar un campo
            if bandera == "S" or bandera == "s":
                cambios = subscripciones.borrar_subscripciones(con, cur)

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

if __name__ == "__main__":
    con = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cur = con.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.
    menu_subscripción(con, cur)
    # subscripciones = Subscripciones(12345,1)
    # subscripciones.borrar_subscripciones(con, cur)
    # subscripciones.borrar_subscripcion(con, cur, 12346, 2)
    # subscripciones.setcodigo(3)
    # subscripciones.actualizar_subscripcion(con, cur)
    # subscripciones.buscar_subscripcion(cur,12345)
    # subscripciones.agregar_subscripcion(con, cur,1) 
    # print(subscripciones.consulta_subscripciones(cur))
    # print(subscripciones.consulta_subscripciones(cur, "codigoPlan"))