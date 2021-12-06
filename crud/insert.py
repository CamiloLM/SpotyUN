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
