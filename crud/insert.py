def insertar_cancion(con, cur, cancion):
    """
    Ingresa datos en la tabla cancion, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): nombre, ubicacion, genero, album, interprete.
    """
    cur.execute("INSERT INTO cancion VALUES (?, ?, ?, ?, ?, ?)", cancion)
    con.commit()


def insertar_canciones(con, cur, canciones):
    """
    Ingresa multiples datos en la tabla cancion.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    canciones (list): Lista con los datos de las canciones.
    """
    cur.executemany("INSERT INTO cancion VALUES (?, ?, ?, ?, ?, ?)", canciones)
    con.commit()


def insertar_cliente(con, cur, cliente):
    """
    Ingresa datos en la tabla cliente, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): cedula, nombre, apellido, correo, etc.
    """
    cur.execute("INSERT INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", cliente)
    con.commit()


def insertar_clientes(con, cur, clientes):
    """
    Ingresa multiples datos en la tabla cliente.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    clientes (list): Lista con los datos de los clientes.
    """
    cur.executemany("INSERT INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", clientes)
    con.commit()


def insertar_plan(con, cur, plan):
    """
    Ingresa datos en la tabla planes, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): nombre, valor, cantidad, descripcion.
    """
    cur.execute("INSERT INTO planes VALUES (?, ?, ?, ?)", plan)
    con.commit()


def insertar_planes(con, cur, planes):
    """
    Ingresa multiples datos en la tabla planes.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    planes (list): Lista con los datos de los planes.
    """
    cur.executemany("INSERT INTO planes VALUES (?, ?, ?, ?)", planes)
    con.commit()


def agregar_subscripcion(con, cur, datos):
    """
    Agrega un cliente a un plan, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): cedulaCliente, nombrePlan.
    """
    cur.execute("INSERT INTO subscripciones VALUES (?, ?)", datos)
    con.commit()


def agregar_cancion(con, cur, datos):
    """
    Agrega una cancion a una lista de canciones, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): nombreLista, cedulaCliente, codigoCancion.
    """
    cur.execute("INSERT INTO listaCanciones VALUES (?, ?, ?)", datos)
    con.commit()


def insertar_admin(con, cur, datos):
    """
    Ingresa datos en la tabla administrador, estos datos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cliente (list): cedula, nombre, apellido, correo.
    """
    cur.execute("INSERT INTO administrador VALUES (?, ?, ?, ?)", datos)
    con.commit()
