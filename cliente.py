from usuario import Usuario


class Cliente(Usuario):
    def __init__(self, cedula, nombre, apellido, correo, pais, ciudad, telefono, tarjeta_credito, fecha_pago, pago):
        super().__init__(cedula, nombre, apellido, correo)
        self._pais = pais
        self._ciudad = ciudad
        self._telefono = telefono
        self._tarjeta_credito = tarjeta_credito
        self._fecha_pago = fecha_pago
        self._pago = pago


    def __str__(self) -> str:
        return (
            "Cedula: {}\nNombre: {}\nApellido: {}\nCorreo: {}\nPais: {}\nCiudad: {}\nTelefono: {}\nTarjeta credito: {}\nFecha pago: {}\nPago: {}".format(
            self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito, self._fecha_pago, self._pago)
        )


    @property
    def cedula(self):
        return self._cedula


    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula


    @property
    def datos(self):
        return self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito


    @datos.setter
    def datos(self, datos_usuario):
        self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono, self._tarjeta_credito = datos_usuario


    @property
    def datos_pago(self):
        return self._fecha_pago, self._pago


    @datos_pago.setter
    def datos_pago(self, datos):
        self._fecha_pago, self._pago = datos


    def ingresar_usuario(self, con, cur):
        """
        Ingresa los datos del objeto en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        datos = (self._cedula, self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono,
            self._tarjeta_credito, self._fecha_pago, self._pago)
        cur.execute("INSERT OR IGNORE INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
        con.commit()


    def consulta_usuario_especifica(self, cur):
        """
        Consulta una cliente por su cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        datos = [self._cedula]
        cur.execute("SELECT * FROM cliente WHERE cedula = ?", datos)
        return cur.fetchone()


    def consulta_usuario_general(self, cur, campo="cedula"):
        """
        Consulta todos los datos de la tabla cliente ordenandolos por el campo suministrado.
        Si no se proporciona uno, por defecto ordena por la cedula.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        campo (str): Nombre de la columna por la que se va a ordenar.
        """
        cur.execute("SELECT * FROM cliente ORDER BY {}".format(campo))
        return cur.fetchall()


    def actualizar_usuario(self, con, cur):
        """
        Actualiza datos en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        datos = (self._nombre, self._apellido, self._correo, self._pais, self._ciudad, self._telefono,
            self._tarjeta_credito, self._cedula)
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
    

    def actualizar_datos_pago(self, con, cur):
        """
        Ingresa un pago en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        datos = [self._fecha_pago, self._pago, self._cedula]
        cur.execute('''
            UPDATE OR IGNORE cliente
            SET fechaPago = ?,
            pago = ?
            WHERE cedula = ?''', datos)
        con.commit()


    def borrar_usuario_especifico(self, con, cur):
        """
        Borra un registro en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        cedula (int): Cedula del cliente.
        """
        datos = [self._cedula]
        cur.execute("DELETE FROM cliente WHERE cedula = ?", datos)
        con.commit()


    def borrar_usuario_general(self, con, cur):
        """
        Borra todos los registros en la tabla cliente.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM cliente")
        con.commit()


# def menu_cliente(con, cur):
if __name__ == "__main__":
    clt1 = Cliente(123, "Camilo", "Londoño", "camilo@correo.com", "Colombia", "Bogota", 123456789, 987654321, None, None)
    print(clt1)

    # clt1.ingresar_usuario(con, cur)

    # clt1.cedula = 123
    # print(clt1.consulta_usuario_especifica(cursor))

    # print(clt1.consulta_usuario_general(cursor))
    # print(clt1.consulta_usuario_general(cursor, "nombre"))

    # clt1.cedula = 124
    # clt1.datos = ["John", "Doe", "john@mail.com", "United States", "Chicago", 6349742378, 123456789]
    # clt1.actualizar_usuario(conexion, cursor)

    # clt1.datos_pago = ["2022-02-01", 1]
    # clt1.actualizar_datos_pago(conexion, cursor)

    # clt1.borrar_usuario_especifico(conexion, cursor)
    # clt1.borrar_usuario_general(conexion, cursor)
    