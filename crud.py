import sqlite3

def conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        con.execute("PRAGMA foreign_keys = 1")
        return con
    except sqlite3.Error:
        print(sqlite3.Error)


# Funcion generadora de tablas
def crear_tablas(con, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS cancion (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ubicacion TEXT NOT NULL,
        genero TEXT,
        album TEXT,
        interprete TEXT
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS cliente (
        cedula INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        pais TEXT,
        ciudad TEXT,
        telefono INTEGER,
        targetaCredito INTEGER,
        fechaPago TEXT,
        pago INTEGER
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS planes (
        nombre TEXT PRIMARY KEY,
        valor float,
        cantidad INTEGER,
        decripcion TEXT
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS subscripciones (
        cedulaCliente INTEGER,
        nombrePlan INTEGER,
        FOREIGN KEY (nombrePlan) REFERENCES planes (nombre),
        FOREIGN KEY (cedulaCliente) REFERENCES cliente (cedula)
        )''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS listaCanciones (
        nombreLista TEXT NOT NULL,
        cedulaCliente INTEGER,
        codigoCancion INTEGER,
        FOREIGN KEY (codigoCancion) REFERENCES cancion (codigo),
        FOREIGN KEY (cedulaCliente) REFERENCES cliente (cedula)
        )''')
    
    con.commit()


# Funciones para agregar datos a las tablas
def insertar_cancion(con, cur, cancion):
    cur.execute("INSERT INTO cancion VALUES (?, ?, ?, ?, ?, ?)", cancion)
    con.commit()


def insertar_canciones(con, cur, canciones):
    cur.executemany("INSERT INTO cancion VALUES (?, ?, ?, ?, ?, ?)", canciones)
    con.commit()


def insertar_cliente(con, cur, cliente):
    cur.execute("INSERT INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", cliente)
    con.commit()


def insertar_clientes(con, cur, clientes):
    cur.executemany("INSERT INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", clientes)
    con.commit()


def insertar_plan(con, cur, plan):
    cur.execute("INSERT INTO planes VALUES (?, ?, ?, ?)", plan)
    con.commit()


def insertar_planes(con, cur, plan):
    cur.executemany("INSERT INTO planes VALUES (?, ?, ?, ?)", plan)
    con.commit()


def agregar_subscripcion(con, cur, datos):
    cur.execute("INSERT INTO subscripciones VALUES (?, ?)", datos)
    con.commit()


def agregar_cancion(con, cur, datos):
    cur.execute("INSERT INTO listaCanciones VALUES (?, ?, ?)", datos)
    con.commit()


# Funciones para hacer consultas
def consulta_canciones(cur):
    cur.execute("SELECT * FROM cancion")
    return cur.fetchall()


def buscar_cancion(cur, nombre):
    datos = [nombre + "%"]
    cur.execute("SELECT * FROM cancion WHERE nombre LIKE ?", datos)
    return cur.fetchall()


def consulta_clientes(cur):
    cur.execute("SELECT * FROM cliente")
    return cur.fetchall()


def buscar_cliente(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT * FROM cliente WHERE cedula = ?", datos)
    return cur.fetchall()


def consulta_planes(cur):
    cur.execute("SELECT * FROM planes")
    return cur.fetchall()


def buscar_plan(cur, nombre):
    datos = [nombre]
    cur.execute("SELECT * FROM planes WHERE nombre = ?", datos)
    return cur.fetchall()


def consulta_subscripciones(cur):
    cur.execute("SELECT * FROM subscripciones")
    return cur.fetchall()


def buscar_subscripcion(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT * FROM subscripciones WHERE cedulaCliente = ?", datos)
    return cur.fetchall()


def consulta_general_listas(cur):
    cur.execute("SELECT * FROM listaCanciones")
    return cur.fetchall()


def consulta_usuario_listas(cur, cedula):
    datos = [cedula]
    cur.execute("SELECT DISTINCT nombreLista FROM listaCanciones WHERE cedulaCliente = ?", datos)
    return cur.fetchall()


def buscar_lista(cur, nombre, cedula):
    datos = [nombre, cedula]
    cur.execute("SELECT * FROM listaCanciones WHERE nombreLista LIKE ? AND cedulaCliente = ?", datos)
    return cur.fetchall()


# Funciones actualizar datos
def actualizar_cancion(con, cur, valores):
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
    datos = [fecha, cedula]
    cur.execute('''
        UPDATE cliente
        SET fechaPago = ?,
        pago = 1
        WHERE cedula = ?''', datos)
    con.commit()


def actualizar_plan(con, cur, valores):
    cur.execute('''
        UPDATE planes
        SET valor = ?,
        cantidad = ?,
        decripcion = ?
        WHERE nombre = ?''', valores)
    con.commit()


if __name__ == "__main__":
    con = conexion()
    cur = con.cursor()
    
    
    
    con.close()
