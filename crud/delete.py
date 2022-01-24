def borrar_cancion(con, cur, codigo):
    """
    Borra un registro en la tabla cancion.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    codigo (int): Codigo de la cancion.
    """
    cur.execute("DELETE FROM cancion WHERE codigo = ?", [codigo])
    con.commit()


def borrar_canciones(con, cur):
    """
    Borra todos los registros en la tabla cancion

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM cancion")
    con.commit()


def borrar_cliente(con, cur, cedula):
    """
    Borra un registro en la tabla cliente.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedula (int): Cedula del cliente.
    """
    cur.execute("DELETE FROM cliente WHERE cedula = ?", [cedula])
    con.commit()


def borrar_clientes(con, cur):
    """
    Borra todos los registros en la tabla cliente.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM cliente")
    con.commit()


def borrar_plan(con, cur, nombre):
    """
    Borra un regristro en la tabla planes.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombre (str): Nombre del plan exactamente como aparece en a base.
    """
    cur.execute("DELETE FROM planes WHERE nombre = ?", [nombre])
    con.commit()


def borrar_planes(con, cur):
    """
    Borra todos los registros en la tabla planes.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM planes")
    con.commit()


def borrar_subscripcion(con, cur, cedulaCliente, nombrePlan):
    """
    Borra un registro en la tabla subscripciones, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedulaCliente (int): Cedula del cliente.
    nombrePlan (str): Nombre del plan exactamente como aparece en a base.
    """
    datos_subscripcion = [cedulaCliente, nombrePlan]
    cur.execute("DELETE FROM subscripciones WHERE cedulaCliente = ? and nombrePlan = ?", datos_subscripcion)
    con.commit()


def borrar_subscripciones(con, cur):
    """
    Borra todo el registro en la tabla subscripciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM subscripciones")
    con.commit()


def borrar_listaCanciones(con, cur, nombreLista, cedulaCliente):
    """
    Borra un registro en la tabla listaCanciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombreLista (str): Nombre de la lista exactamente como aprece en la base.
    cedulaCliente (int): Cedula del cliente.
    """
    datos = [nombreLista, cedulaCliente]
    cur.execute("DELETE FROM listaCanciones WHERE nombreLista = ? AND cedulaCliente = ?", datos)
    con.commit()


def borrar_cancion_lista(con, cur, nombre, cedula, codigo):
    """
    Borra un registro en la tabla listaCanciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombre (str): Nombre de la lista exactamente como aprece en la base.
    cedula (int): Cedula del cliente.
    codigo (int): Codigo de la cancion.
    """
    datos = [nombre, cedula, codigo]
    cur.execute("DELETE FROM listaCanciones WHERE nombreLista = ? AND cedulaCliente = ? AND codigoCancion = ?", datos)
    con.commit()


def borrar_listasCanciones(con, cur):
    """
    Borra todos los registros en la tabla listaCanciones.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM listaCanciones")
    con.commit()


def borrar_administrador(con, cur, cedula):
    """
    Borra un registro la tabla administrador.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedula (int): Cedula del administrador.
    """
    cur.execute("DELETE FROM administrador WHERE cedula = ?", [cedula])
    con.commit()


def borrar_administradores(con, cur):
    """
    Borra todos los registros en la tabla administrador.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """
    cur.execute("DELETE FROM administrador")
    con.commit()
