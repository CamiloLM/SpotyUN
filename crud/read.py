def consulta_canciones(cur):
    cur.execute("SELECT * FROM cancion")
    return cur.fetchall()


def buscar_cancion_nombre(cur, nombre):
    datos = [nombre + "%"]
    cur.execute("SELECT * FROM cancion WHERE nombre LIKE ?", datos)
    return cur.fetchall()


def buscar_cancion_especifica(cur, codigo):
    datos = [codigo]
    cur.execute("SELECT * FROM cancion WHERE codigo = ?", datos)
    return cur.fetchone()


def consulta_clientes(cur):
    cur.execute("SELECT * FROM cliente")
    return cur.fetchall()


def buscar_cliente(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT * FROM cliente WHERE cedula = ?", datos)
    return cur.fetchone()


def consulta_planes(cur):
    cur.execute("SELECT * FROM planes")
    return cur.fetchall()


def buscar_plan(cur, nombre):
    datos = [nombre]
    cur.execute("SELECT * FROM planes WHERE nombre = ?", datos)
    return cur.fetchone()


def consulta_subscripciones(cur):
    cur.execute("SELECT * FROM subscripciones")
    return cur.fetchall()


def buscar_subscripcion(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT * FROM subscripciones WHERE cedulaCliente = ?", datos)
    return cur.fetchone()


def consulta_general_listas(cur):
    cur.execute("SELECT * FROM listaCanciones")
    return cur.fetchall()


def consulta_usuario_listas(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT DISTINCT nombreLista FROM listaCanciones WHERE cedulaCliente = ?", datos)
    return cur.fetchall()


def buscar_lista(cur, nombre, cedula):
    datos = [nombre, cedula]
    cur.execute("SELECT codigoCancion FROM listaCanciones WHERE nombreLista LIKE ? AND cedulaCliente = ?", datos)
    return cur.fetchall()


def consulta_admins(cur):
    cur.execute("SELECT * FROM administrador")
    return cur.fetchall()


def buscar_admin(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT * FROM administrador WHERE cedula = ?", datos)
    return cur.fetchone()
