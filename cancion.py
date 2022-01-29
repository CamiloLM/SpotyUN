import sqlite3
def conexion_base_datos():
    """Crea una conexión con la base de datos, si no existe se crea una vacia."""
    try:
        return sqlite3.connect('SpotyUN.db')  # Retorna una conexón sqlite con la base de datos del programa.
    except sqlite3.Error:
        print(sqlite3.Error)  # En caso de que suceda un error grave el programa atrapa e imprime el error.

class Cancion:
    def __init__(self,codigo,nombre,ubicacion):
        self.codigo=codigo
        self.nombre=nombre
        self.ubicacion=ubicacion
        self.genero=None 
        self.album=None
        self.interprete=None
        self.fotografia=None

    def setCancion(self,listaValores):
         self.nombre,self.ubicacion,self.genero,self.album,self.interprete,self.fotografia = listaValores
    def setCodigo(self,codigo):
         self.codigo = codigo
    
    def insertar_cancion(self, con, cur):
        """
        Ingresa datos en la tabla cancion, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cancion=[self.codigo,self.nombre,self.ubicacion,self.genero,self.album,self.interprete,self.fotografia]
        cur.execute("INSERT INTO cancion VALUES (?, ?, ?, ?, ?, ?, ?)", cancion)
        con.commit()    
 
    def consulta_canciones(self, cur, campo="codigo"):
        """
        Consulta todos los datos de la tabla cancion
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        limite (int): Limite de canciones por plan
        """
        cur.execute("SELECT * FROM cancion ORDER BY {}".format(campo))
        return cur.fetchall()

    def buscar_cancion_especifica(self, cur, codigo):
        """
        Consulta una cancion por su codigo.
        
        Parametros:
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        codigo (int): Codigo de la cancion.
        """
        datos = [codigo]
        cur.execute("SELECT * FROM cancion WHERE codigo = ?", datos)
        return cur.fetchone()    

    def actualizar_cancion(self, con, cur):
        """
        Actualiza datos en la tabla cancion, estos deben estar en orden.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        valores = [self.nombre,self.ubicacion,self.genero,self.album,self.interprete,self.fotografia,self.codigo]
        cur.execute('''
            UPDATE cancion
            SET nombre = ?,
            ubicacion = ?,
            genero = ?,
            album = ?,
            interprete = ?,
            fotografia = ?
            WHERE codigo = ?''', valores)
        con.commit()

    def borrar_cancion(self, con, cur, codigo):
        """
        Borra un registro en la tabla cancion.

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        codigo (int): Codigo de la cancion.
        """
        cur.execute("DELETE FROM cancion WHERE codigo = ?", [codigo])
        con.commit()

    def borrar_canciones(self, con, cur):
        """
        Borra todos los registros en la tabla cancion

        Parametros:
        con (sqlite3.Connection): Conexion a la base de datos.
        cur (sqlite3.Cursor): Cursor para realizar las operaciones.
        """
        cur.execute("DELETE FROM cancion")
        con.commit()

if __name__ == "__main__":
    con = conexion_base_datos()  # Almacena un objetos con la conexión a la base de datos.
    cur = con.cursor()  # Almacena un objeto cursor para realizar selecciones en la base da datos.
    cancion = Cancion(None,"More","Predator.mp3") 
    # cancion.setCancion(["prueba","demomento","rock","nuevo","yo",None])
    # cancion.setCodigo(1)
    # cancion.borrar_cancion(con, cur, 1)
    # cancion.borrar_canciones(con, cur)
    # cancion.insertar_cancion(con, cur)           