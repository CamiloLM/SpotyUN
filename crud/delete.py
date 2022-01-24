import sqlite3
def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        return sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.
        
def borrar_cancion(con,cur,codigo):
    """
    Borra un registro en la tabla cancion, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM cancion WHERE codigo = ?",[codigo])
    con.commit()

def borrar_canciones(con,cur):
    """
    Borra todo el registro en la tabla cancion, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM cancion")
    con.commit()

def borrar_cliente(con,cur,cedula):
    """
    Borra un registro en la tabla cliente, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM cliente WHERE cedula = ?",[cedula])
    con.commit()

def borrar_clientes(con,cur):
    """
    Borra todo el registro en la tabla cliente, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM cliente")
    con.commit()

def borrar_plan(con,cur,nombre):
    """
    Borra un regristro en la tabla planes, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM planes WHERE nombre = ?",[nombre])
    con.commit()

def borrar_planes(con,cur):
    """
    Borra todo el registro en la tabla planes, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM planes")
    con.commit()

def borrar_subscripcion(con,cur,cedulaCliente,nombrePlan):
    """
    Borra un registro en la tabla subscripciones, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    datos_subscripcion = [cedulaCliente,nombrePlan]
    cur.execute("DELETE FROM subscripciones WHERE cedulaCliente = ? and nombrePlan = ?",datos_subscripcion)
    con.commit()

def borrar_subscripciones(con,cur):
    """
    Borra todo el registro en la tabla subscripciones, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM subscripciones")
    con.commit()

def borrar_listaCanciones(con,cur,nombreLista):
    """
    Borra un registro en la tabla listaCanciones, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM listaCanciones WHERE nombreLista = ?",[nombreLista])
    con.commit()

def borrar_listasCanciones(con,cur):
    """
    Borra todo registro en la tabla listaCanciones, estos deben estar en orden.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM listaCanciones")
    con.commit()

def borrar_administrador(con,cur,cedula):
    """
    Borra un registro en administrador

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM administrador WHERE cedula = ?",[cedula])
    con.commit()

def borrar_administradores(con,cur):
    """
    Borra un registro en administrador

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    valores (list): nombre, ubicacion, genero, album, interprete, codigo.
    """
    cur.execute("DELETE FROM administrador")
    con.commit()
   

if __name__ == "__main__":   
    conexion = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cursor = conexion.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.
    # borrar_cancion(conexion, cursor, 2)
    # borrar_canciones(conexion, cursor)
    # borrar_cliente(conexion,cursor,1000328521)
    # borrar_clientes(conexion,cursor)
    # borrar_plan(conexion,cursor,"Gratis")
    # borrar_planes(conexion,cursor)
    # borrar_subscripcion(conexion,cursor,1000328521,"Gratis")
    # borrar_subscripciones(conexion,cursor)
    # borrar_listaCanciones(conexion,cursor,"Test")
    # borrar_listasCanciones(conexion,cursor)
    # borrar_administrador(conexion,cursor,1000328521)
    # borrar_administradores(conexion,cursor)
    