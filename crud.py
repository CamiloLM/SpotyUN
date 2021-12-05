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
        urlCancion TEXT NOT NULL,
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
        fechaPago TEXT,
        targetaCredito INTEGER,
        pago INTEGER
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS planes (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        valor float,
        cantidad INTEGER
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS subscripciones (
        cedulaCliente INTEGER,
        codigoPlan INTEGER,
        FOREIGN KEY (codigoPlan) REFERENCES planes (codigo),
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


def agregar_subscripcion(con, cur, datos):
    cur.execute("INSERT INTO subscripciones VALUES (?, ?)", datos)
    con.commit()


def agregar_cancion(con, cur, datos):
    cur.execute("INSERT INTO listaCanciones VALUES (?, ?, ?)", datos)
    con.commit()


# Codigo aun no adaptado

# def actualizar_tabla(con):
#     cursorObj=con.cursor()
#     nombre=input("Nombre: ")
#     actualizar='UPDATE cancion set Nombre = "'+nombre+'"'
#     print("La cadena es: ",actualizar)
#     cursorObj.execute(actualizar)
#     con.commit()

# def consulta_individual(con,cod):
#     cursorObj=con.cursor()
#     cursorObj.execute('SELECT ID, Nombre FROM cancion WHERE ID = "'+cod+'"')
#     filas=cursorObj.fetchall()
#     print("Veremos: ",len(filas)," filas.")
#     for row in filas:
#         print (row)

# def consulta_general(con):
#     cursorObj=con.cursor()
#     cursorObj.execute("SELECT * FROM cancion")
#     filas=cursorObj.fetchall()
#     print("La información extrída es: ")
#     for row in filas:
#         numero=row[0]
#         nombre=row[1]
#         album=row[2]
#         print("La información es: ",numero," ",nombre," ",album)
#         print("La informacion de la tupla es: ")
#         print(row)


if __name__ == "__main__":
    con = conexion()
    cur = con.cursor()

    crear_tablas(con, cur)

    con.close()
