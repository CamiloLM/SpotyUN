def actualizar_cancion(con, cur, valores):
    """
    Actualiza datos en la tabla cancion, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute('''
        UPDATE cancion
        SET nombre = ?,
        ubicacion = ?,
        genero = ?,
        album = ?,
        interprete = ?
        WHERE codigo = ?''', valores)
    con.commit()


def actualizar_cliente(con, cur, valores):
    """
    Actualiza datos en la tabla cliente, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): nombre, apellido, correo, pais, ciudad, telefono, targetaCredito, cedula.
    """
    cur.execute('''
        UPDATE cliente
        SET nombre = ?,
        apellido = ?,
        correo = ?,
        pais = ?,
        ciudad = ?,
        telefono = ?,
        targetaCredito = ?
        WHERE cedula = ?''', valores)
    con.commit()


def actualizar_pago(con, cur, fecha, cedula):
    """
    Ingresa un pago en la tabla cliente, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    fecha (str): Fecha de vencimiento.
    cedula (int): Cedula del cliente.
    """
    datos = [fecha, cedula]
    cur.execute('''
        UPDATE cliente
        SET fechaPago = ?,
        pago = 1
        WHERE cedula = ?''', datos)
    con.commit()


def actualizar_plan(con, cur, valores):
    """
    Ingresa datos en la tabla planes, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): valor, cantidad, descripcion, nombre.
    """
    cur.execute('''
        UPDATE planes
        SET valor = ?,
        cantidad = ?,
        decripcion = ?
        WHERE nombre = ?''', valores)
    con.commit()
