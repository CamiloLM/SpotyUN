from usuario import Usuario


class Administrador(Usuario):
    def __init__(self, cedula, nombre, apellido, correo):
        super().__init__(cedula, nombre, apellido, correo)


    def __str__(self) -> str:
        return ("Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}".format(self._cedula, self._nombre, self._apellido, self._correo))


    @property
    def cedula(self):
        return self._cedula


    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula


    @property
    def datos(self):
        return self._nombre, self._apellido, self._correo


    @datos.setter
    def datos(self, datos_usuario):
        self._nombre, self._apellido, self._correo = datos_usuario


    def ingresar_usuario(self, con, cur):
        """
        Ingresa datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        datos (list): cedula, nombre, apellido, correo.
        """
        datos = self._cedula, self._nombre, self._apellido, self._correo
        # Inserta los valores de datos en la tabla administrador si no se generan conflictos
        cur.execute("INSERT OR IGNORE INTO administrador VALUES (?, ?, ?, ?)", datos)
        con.commit()

    
    def consulta_usuario_especifica(self, cur):
        """
        Consulta los datos de un administrador por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.

        Regresa:
        datos_administrador (tuple): Si encuentra un administrador con esa cedula-
        None: Si no encuentra ninguna coincidencia.
        """
        datos = [self._cedula]
        # Trae toda la información de la tabla administrador donde la cedula coincida con el parametro
        cur.execute("SELECT * FROM administrador WHERE cedula = ?", datos)
        return cur.fetchone()
    

    def consulta_usuario_general(self, cur, campo="cedula"):
        """
        Consulta todos los datos de la tabla administrador ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.
        """
        cur.execute("SELECT * FROM administrador ORDER BY {}".format(campo))
        return cur.fetchall()
    

    def actualizar_usuario(self, con, cur):
        """
        Actualiza datos en la tabla administrador, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        datos = self._nombre, self._apellido, self._correo, self._cedula
        cur.execute('''
            UPDATE OR IGNORE administrador
            SET nombre = ?,
            apellido = ?,
            correo = ?
            WHERE cedula = ?''', datos)
        con.commit()
    

    def borrar_usuario_especifico(self, con, cur):
        """
        Borra un registro la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM administrador WHERE cedula = ?", [self._cedula])
        con.commit()
    

    def borrar_usuario_general(self, con, cur):
        """
        Borra todos los registros en la tabla administrador.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM administrador")
        con.commit()


# def menu_administrador(con, cur):
if __name__ == "__main__":
    admin1 = Administrador(123, "Camilo", "Londoño", "camilo@correo.com")
    print(admin1)
    
    # admin1.ingresar_usuario(conexion, cursor)

    # admin1.cedula = 123
    # print(admin1.consulta_usuario_especifica(cursor))

    # print(admin1.consulta_usuario_general(cursor))
    # print(admin1.consulta_usuario_general(cursor, "nombre"))

    # admin1.cedula = 456
    # admin1.datos = [None, "Doe", "john@mail.com"]
    # admin1.actualizar_usuario(conexion, cursor)

    # admin1.borrar_usuario_especifico(conexion, cursor)
    # admin1.borrar_usuario_general(conexion, cursor) 
    