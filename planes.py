import sqlite3  # Modulo para realizar operaciones a la base de datos


def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        # Retorna una conexón sqlite con la base de datos del programa.
        return sqlite3.connect('SpotyUN.db')
    except sqlite3.Error:
        # En caso de que suceda un error grave el programa atrapa e imprime el error.
        print(sqlite3.Error)


class plan:
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto 'Plan'."""
        self.__codigo = ""
        self.__nombre = ""
        self.__valor = ""
        self.__cantidad = ""

    def setdatos(self, codigo, nombre, valor, cantidad):
        """Método para cambiar el valor de los datos/argumentos privados."""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__valor = valor
        self.__cantidad = cantidad

    def getdatos(self):
        """Método se emplea para obtener los datos/argumentos privados de la
        clase.
        """
        return [self.__codigo, self.__nombre, self.__valor, self.__cantidad]

    def consulta_planes_general(cur, self):
        """Consulta todos los datos de la tabla planes"""
        cur.execute("SELECT * FROM planes")
        return cur.fetchall()

    def consulta_plan_especifica(cur, self):
        """
        Consulta un plan por su nombre.

        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        nombre (str): Nombre del plan
        """
        datos = [self.__nombre]
        cur.execute("SELECT * FROM planes WHERE nombre = ?", datos)
        return cur.fetchone()

    def registrar_plan(con, cur, planes, self):
        """
        Ingresa multiples datos en la tabla planes.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        planes (list): Lista con los datos de los planes.
        """
        planes = plan.getdatos()
        cur.executemany("INSERT INTO planes VALUES (?, ?, ?, ?)", planes)
        con.commit()
    # valores= ¿getdatos?

    def actualizar_plan(con, cur, valores, self):
        """
        Ingresa datos en la tabla planes, estos datos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        plan (list): codigo(int), nombre (str), valor (float), cantidad(int).
        """
        valores = plan.getdatos()
        cur.execute('''
            UPDATE planes
            SET codigo = ?,
            nombre = ?,
            valor = ?,
            cantidad = ?
            WHERE codigo = ?''', valores)
        con.commit()

    def borrar_plan(con, cur, self):
        """
        Borra un regristro en la tabla planes.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        self.__nombre (str): Nombre del plan exactamente como aparece en
        la base.
        """
        cur.execute("DELETE FROM planes WHERE nombre = ?", [self.__nombre])
        con.commit()

    def borrar_planes(con, cur, self):
        """
        Borra todos los registros en la tabla planes.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM planes")
        con.commit()


# Almacena un objetos con la conexión a la base de datos.
conexion = conexion_base_datos()
# Almacena un objeto cursor para realizar selecciones en la base da datos.
cursor = conexion.cursor()
co = input("Código: ")
n = input("Nombre: ")
v = input("Valor: ")
ca = input("Cantidad: ")
12
plan1 = plan()
plan1.setdatos(co, n, v, ca)
print(plan1.getdatos())
