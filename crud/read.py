def consulta_canciones(cur):
    """Consulta todos los datos de la tabla cancion"""
    cur.execute("SELECT * FROM cancion")
    return cur.fetchall()


def buscar_cancion_nombre(cur, nombre):
    """
    Consulta las canciones que tienen un nombre similar a la busqueda

    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombre (str): Nombre de la cancion.
    """
    datos = [nombre + "%"]
    cur.execute("SELECT * FROM cancion WHERE nombre LIKE ?", datos)
    return cur.fetchall()


def buscar_cancion_especifica(cur, codigo):
    """
    Consulta una cancion por su codigo.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    codigo (int): Codigo de la cancion.
    """
    datos = [codigo]
    cur.execute("SELECT * FROM cancion WHERE codigo = ?", datos)
    return cur.fetchone()


def consulta_clientes(cur):
    """Consulta todos los datos de la tabla cliente"""
    cur.execute("SELECT * FROM cliente")
    return cur.fetchall()


def buscar_cliente(cur, cedula):
    """
    Consulta una cliente por su cedula.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedula (int): Cedula del cliente
    """
    datos = [cedula]
    cur.execute("SELECT * FROM cliente WHERE cedula = ?", datos)
    return cur.fetchone()


def consulta_planes(cur):
    """Consulta todos los datos de la tabla planes"""
    cur.execute("SELECT * FROM planes")
    return cur.fetchall()


def buscar_plan(cur, nombre):
    """
    Consulta una plan por su nombre.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombre (str): Nombre del plan
    """
    datos = [nombre]
    cur.execute("SELECT * FROM planes WHERE nombre = ?", datos)
    return cur.fetchone()


def consulta_subscripciones(cur):
    """Consulta todos los datos de la tabla subscripciones"""
    cur.execute("SELECT * FROM subscripciones")
    return cur.fetchall()


def buscar_subscripcion(cur, cedula):
    """
    Consulta una plan por su nombre.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedulaCliente (int): Cedula del cliente
    """
    datos = [cedula]
    cur.execute("SELECT * FROM subscripciones WHERE cedulaCliente = ?", datos)
    return cur.fetchone()


def consulta_general_listas(cur):
    """Consulta todos los datos de la tabla listaCanciones"""
    cur.execute("SELECT * FROM listaCanciones")
    return cur.fetchall()


def consulta_usuario_listas(cur, cedula):
    """
    Consulta los nombres de las listas por la cedula del cliente.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedulaCliente (int): Cedula del cliente
    """
    datos = [cedula]
    cur.execute("SELECT DISTINCT nombreLista FROM listaCanciones WHERE cedulaCliente = ?", datos)
    return cur.fetchall()


def buscar_lista(cur, nombre, cedula):
    """
    Consulta los codigos de las canciones en la lista.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    nombre (str): Nombre de la lista
    cedulaCliente (int): Cedula del cliente
    """
    datos = [nombre, cedula]
    cur.execute("SELECT codigoCancion FROM listaCanciones WHERE nombreLista LIKE ? AND cedulaCliente = ?", datos)
    return cur.fetchall()


def consulta_admins(cur):
    """Consulta todos los datos de la tabla administrador"""
    cur.execute("SELECT * FROM administrador")
    return cur.fetchall()


def buscar_admin(cur, cedula):
    """
    Consulta una administrador por su cedula.
    
    Parametros:
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    cedula (int): Cedula del administrador
    """
    datos = [cedula]
    cur.execute("SELECT * FROM administrador WHERE cedula = ?", datos)
    return cur.fetchone()
