def actualizar_cancion(con, cur, valores):
    """
    Actualiza datos en la tabla cancion, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre (str), ubicacion (str), genero, album, interprete, codigo (int).
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
    cliente (list): Nombre (str), apellido (str), correo (str), pais, ciudad, telefono, targetaCredito, cedula(int).
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


def actualizar_pago(con, cur, fecha, pago, cedula):
    """
    Ingresa un pago en la tabla cliente, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    fecha (str): Fecha de vencimiento.
    pago (int): Si el cliente pago 1, si no pago 0.
    cedula (int): Cedula del cliente.
    """
    datos = [fecha, pago, cedula]
    cur.execute('''
        UPDATE cliente
        SET fechaPago = ?,
        pago = ?
        WHERE cedula = ?''', datos)
    con.commit()


def actualizar_plan(con, cur, valores):
    """
    Ingresa datos en la tabla planes, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): valor(float), cantidad (int), descripcion (str), nombre(str).
    """
    cur.execute('''
        UPDATE planes
        SET valor = ?,
        cantidad = ?,
        decripcion = ?
        WHERE nombre = ?''', valores)
    con.commit()


def actualizar_subscripcion(con, cur, datos):
    """
    Actualiza los datos en la tabla subscripciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    datos (list): Nombre del plan (str), cedula del cliente (int).
    """
    cur.execute('''
        UPDATE subscripciones
        SET nombrePlan = ?
        WHERE cedulaCliente = ?''', datos)
    con.commit()


def actualizar_lista_cancion(con, cur, datos):
    """
    Actualiza los datos en la tabla lista canciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    datos (list): Nombre de la lista (str), codigo canción (int), cedula del cliente (int).
    """
    cur.execute('''
        UPDATE listaCanciones
        SET nombreLista = ?,
        codigoCancion = ?
        WHERE cedulaCliente = ?''', datos)
    con.commit()


def actualizar_administrador(con, cur, valores):
    """
    Actualiza datos en la tabla administrador, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): Nombre (str), apellido (str), correo (str), cedula (int).
    """
    cur.execute('''
        UPDATE administrador
        SET nombre = ?,
        apellido = ?,
        correo = ?
        WHERE cedula = ?''', valores)
    con.commit()
