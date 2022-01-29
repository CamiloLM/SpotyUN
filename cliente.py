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


class Cliente(Usuario):
    def __init__(self):
        super().__init__()
        self._pais = None
        self._ciudad = None
        self._telefono = None
        self._tarjeta_credito = None
        self._fecha_pago = None
        self._pago = None


    def __str__(self) -> str:
        return (
            "Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}\nPais: {}\nCiudad: {}\nTelefono: {}\nTarjeta credito: {}\nFecha pago: {}\nPago: {}".format(
            self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito, self._fecha_pago, self._pago)
        )


    @property
    def cedula(self) -> int:
        return self._cedula


    @cedula.setter
    def cedula(self, cedula) -> None:
        self._cedula = cedula


    @property
    def datos_usuario(self) -> tuple:
        return self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito


    @datos_usuario.setter
    def datos_usuario(self, datos) -> None:
        self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito = datos


    @property
    def datos_pago(self) -> tuple:
        return self._fecha_pago, self._pago


    @datos_pago.setter
    def datos_pago(self, datos) -> None:
        self._fecha_pago, self._pago = datos


    def ingresar_usuario(self, con, cur) -> int:
        """
        Ingresa los datos del objeto en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = (self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono,
            self._tarjeta_credito, self._fecha_pago, self._pago)
        cur.execute("INSERT OR IGNORE INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
        con.commit()
        return cur.rowcount


    def consulta_usuario_especifica(self, cur) -> tuple:
        """
        Consulta una cliente por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_cliente (tuple): Todos los datos del cliente.
        """
        cur.execute("SELECT * FROM cliente WHERE cedula = ?", [self._cedula])
        return cur.fetchone()


    def consulta_usuario_general(self, cur, campo="cedula") -> tuple:
        """
        Consulta todos los datos de la tabla cliente ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.
        
        Regresa:
        datos_clientes (tuple): Tuple de listas con todos los datos de los clientes.
        """
        cur.execute("SELECT * FROM cliente ORDER BY {}".format(campo))
        return cur.fetchall()


    def actualizar_usuario(self, con, cur) -> int:
        """
        Actualiza datos en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = (self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito, self._cedula)
        cur.execute('''
            UPDATE OR IGNORE cliente
            SET nombre = ?,
            apellido = ?,
            correo = ?,
            pais = ?,
            ciudad = ?,
            telefono = ?,
            tarjetaCredito = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount
    

    def actualizar_datos_pago(self, con, cur) -> int:
        """
        Ingresa un pago en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        datos = [self._fecha_pago, self._pago, self._cedula]
        cur.execute('''
            UPDATE OR IGNORE cliente
            SET fechaPago = ?,
            pago = ?
            WHERE cedula = ?''', datos)
        con.commit()
        return cur.rowcount


    def borrar_usuario_especifico(self, con, cur) -> int:
        """
        Borra un registro en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedula (int): Cedula del cliente.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM cliente WHERE cedula = ?", [self._cedula])
        con.commit()
        return cur.rowcount


    def borrar_usuario_general(self, con, cur) -> int:
        """
        Borra todos los registros en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        rowcount (int): Numero de filas modificadas, si el valor es 0 no se realizaron cambios.
        """
        cur.execute("DELETE FROM cliente")
        con.commit()
        return cur.rowcount


def menu_cliente(con, cur):
    cliente = Cliente()
    
    # Ingresando un nuevo cliente
    # cliente.cedula = 123
    # cliente.datos_usuario = ["Camilo", "Londoño", "camilo@correo.com", "Colombia", "Bogota", 123456789, 987654321]
    # cliente.datos_pago = ["2022-02-01", 1]
    # print(cliente.ingresar_usuario(con, cur))

    # # Consulta cliente por cedula
    # cliente.cedula = 123
    # print(cliente.consulta_usuario_especifica(cur))

    # # Consulta general clientes por campo
    # print(cliente.consulta_usuario_general(cursor))
    # print(cliente.consulta_usuario_general(cursor, "nombre"))

    # # Actualizar datos del cliente y datos del pago
    # cliente.cedula = 123
    # cliente.datos = ["John", "Doe", "john@mail.com", "United States", "Chicago", 6349742378, 123456789]
    # print(cliente.actualizar_usuario(conexion, cursor))

    # cliente.datos_pago = ["2022-02-01", 1]
    # print(cliente.actualizar_datos_pago(conexion, cursor))

    # # Eliminar datos especificos y general
    # cliente.cedula = 123
    # print(cliente.borrar_usuario_especifico(conexion, cursor))
    # print(cliente.borrar_usuario_general(conexion, cursor))


if __name__ == "__main__":
    conexion = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cursor = conexion.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.

    menu_cliente(conexion, cursor)
    