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