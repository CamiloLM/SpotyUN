def crear_tablas(con, cur):
    """
    Función para crear las tablas de la base de datos.

    Parametros:
    con (sqlite3.Connection): Conexion a la base de datos.
    cur (sqlite3.Cursor): Cursor para realizar las operaciones.
    """

    # Comando para crear la tabla cancion con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS cancion (codigo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, 
        ubicacion TEXT NOT NULL, genero TEXT, album TEXT, interprete TEXT) '''
    )

    # Comando para crear la tabla cliente con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS cliente (cedula INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT 
        NULL, correo TEXT NOT NULL, pais TEXT, ciudad TEXT, telefono INTEGER, targetaCredito INTEGER, fechaPago TEXT, 
        pago INTEGER) '''
    )

    # Comando para crear la tabla planes con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS planes (nombre TEXT PRIMARY KEY, valor FLOAT, cantidad INTEGER,
        decripcion TEXT)'''
    )

    # Comando para crear la tabla subscripciones con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS subscripciones (cedulaCliente INTEGER, nombrePlan INTEGER, FOREIGN KEY (
        nombrePlan) REFERENCES planes (nombre), FOREIGN KEY (cedulaCliente) REFERENCES cliente (cedula)) '''
    )

    # Comando para crear la tabla listaCanciones con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS listaCanciones (nombreLista TEXT NOT NULL, cedulaCliente INTEGER, codigoCancion 
        INTEGER, FOREIGN KEY (codigoCancion) REFERENCES cancion (codigo), FOREIGN KEY (cedulaCliente) REFERENCES 
        cliente (cedula)) '''
    )

    # Comando para crear la tabla administrador con sus respectivos campos
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS administrador (cedula INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT 
        NOT NULL, correo TEXT NOT NULL) '''
    )

    # Guarda los cambios en la base de datos
    con.commit()
