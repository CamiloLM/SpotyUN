# La tabla de este objeto fue modificada, ahora uno de sus campos referencia al codigo del plan correspondiente.
# No es un acambio grande solo hay que cambiar el nombre del campo en los execute.
import sqlite3
def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        return sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.

class Subscripciones:
    def __init__(self,cedulaCliente,codigoPlan):
        self.cedulaCliente=cedulaCliente
        self.codigoPlan=codigoPlan

    def setcodigo(self,codigo):
         self.codigoPlan= codigo
    def setCedula(self,cedula):
         self.cedula = cedula    
        
    def agregar_subscripcion(self, con, cur, datos):
        """
        Agrega un cliente a un plan, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cliente (list): cedulaCliente, codigoPlan.
        """
        datos=[self.cedulaCliente,self.codigoPlan]
        cur.execute("INSERT INTO subscripciones VALUES (?, ?)", datos)
        con.commit()    

    def consulta_subscripciones(self, cur):
        """Consulta todos los datos de la tabla subscripciones"""
        cur.execute("SELECT * FROM subscripciones")
        return cur.fetchall()  

    def buscar_subscripcion(self, cur, cedula):
        """
        Consulta un plan por su nombre.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedulaCliente (int): Cedula del cliente
        """
        datos = [cedula]
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
        datos = [self.codigoPlan,self.cedulaCliente]
        cur.execute('''
            UPDATE subscripciones
            SET codigoPlan = ?
            WHERE cedulaCliente = ?''', datos)
        con.commit()    

    def borrar_subscripcion(self, con, cur, cedulaCliente, codigoPlan):
        """
        Borra un registro en la tabla subscripciones, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedulaCliente (int): Cedula del cliente.
        nombrePlan (str): Codigo del plan exactamente como aparece en a base.
        """
        datos_subscripcion = [cedulaCliente, codigoPlan]
        cur.execute("DELETE FROM subscripciones WHERE cedulaCliente = ? and codigoPlan = ?", datos_subscripcion)
        con.commit()     

    def borrar_subscripciones(self, con, cur):
        """
        Borra todo el registro en la tabla subscripciones.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM subscripciones")
        con.commit()      

if __name__ == "__main__":
    con = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cur = con.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.
    subscripciones = Subscripciones(12346,2)
    # subscripciones.borrar_subscripciones(con, cur)
    # subscripciones.borrar_subscripcion(con, cur, 12346, 2)
    subscripciones.setcodigo(3)
    subscripciones.actualizar_subscripcion(con, cur)
    # subscripciones.buscar_subscripcion(cur,12345)
    # subscripciones.consulta_subscripciones(cur)
    # subscripciones.agregar_subscripcion(con, cur,1) 