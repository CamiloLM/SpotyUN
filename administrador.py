from usuario import Usuario
import sqlite3


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        conn = sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
        conn.execute("PRAGMA foreign_keys = 1")  # Activa la selectividad de las llaves foraneas.
        return conn
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.


class Administrador(Usuario):
    def __init__(self):
        super().__init__()


    def __str__(self) -> str:
        return ("Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}".format(self._cedula, self._nombre, self._apellido, self._correo))


    @property
    def cedula(self) -> int:
        return self._cedula


    @cedula.setter
    def cedula(self, cedula) -> None:
        self._cedula = cedula


    @property
    def datos_usuario(self) -> tuple:
        return self._nombre, self._apellido, self._correo


    @datos_usuario.setter
    def datos_usuario(self, datos_usuario) -> None:
        self._nombre, self._apellido, self._correo = datos_usuario


    def ingresar_usuario(self, con, cur) -> int:
        """
        Ingresa datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        datos (list): cedula, nombre, apellido, correo.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self._cedula, self._nombre, self._apellido, self._correo
        # Inserta los valores de datos en la tabla administrador si no se generan conflictos
        cur.execute("INSERT OR IGNORE INTO administrador VALUES (?, ?, ?, ?)", datos)
        con.commit()
        return cur.rowcount

    
    def consulta_usuario_especifica(self, cur) -> tuple:
        """
        Consulta los datos de un administrador por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_administrador (tuple): Si encuentra un administrador con esa cedula-
        None: Si no encuentra ninguna coincidencia.
        """
        # Trae toda la información de la tabla administrador donde la cedula coincida con el parametro
        cur.execute("SELECT * FROM administrador WHERE cedula = ?", [self._cedula])
        return cur.fetchone()
    

    def consulta_usuario_general(self, cur, campo="cedula") -> tuple:
        """
        Consulta todos los datos de la tabla administrador ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.

        Regresa:
        datos_administradores (tuple): Tupla con todos los administradores ordenados por el campo
        None: Si no encuentra ninguna coincidencia.
        """
        cur.execute("SELECT * FROM administrador ORDER BY {}".format(campo))
        return cur.fetchall()
    

    def actualizar_usuario(self, con, cur) -> int:
        """
        Actualiza datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = self._nombre, self._apellido, self._correo, self._cedula
        cur.execute('''
            UPDATE OR IGNORE administrador
            SET nombre = ?,
            apellido = ?,
            correo = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount
    

    def borrar_usuario_especifico(self, con, cur) -> int:
        """
        Borra un registro la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM administrador WHERE cedula = ?", [self._cedula])
        con.commit()
        return cur.rowcount
    

    def borrar_usuario_general(self, con, cur) -> int:
        """
        Borra todos los registros en la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM administrador")
        con.commit()
        return cur.rowcount


def menu_administrador(con, cur):
    admin = Administrador()

    # admin.cedula = 123
    # admin.datos_usuario = ["Camilo", "Londoño", "camilo@correo.com"]
    # print(admin.ingresar_usuario(conexion, cursor))

    # admin.cedula = 123
    # print(admin.consulta_usuario_especifica(cursor))

    # print(admin.consulta_usuario_general(cursor))
    # print(admin.consulta_usuario_general(cursor, "nombre"))

    # admin.cedula = 123
    # admin.datos_usuario = ["John", "Doe", "john@mail.com"]
    # print(admin.actualizar_usuario(conexion, cursor))

    # admin.cedula = 123
    # print(admin.borrar_usuario_especifico(conexion, cursor))
    # print(admin.borrar_usuario_general(conexion, cursor))


if __name__ == "__main__":
    conexion = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cursor = conexion.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.
    
    menu_administrador(conexion, cursor)
    