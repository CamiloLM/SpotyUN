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
