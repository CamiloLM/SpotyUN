import sqlite3

def conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    except sqlite3.Error:
        print(sqlite3.Error)


def crear_tablas(con, cur):
    cur.execute("CREATE TABLE cancion (ID integer PRIMARY KEY AUTOINCREMENT, Nombre text, Genero text, Album text, Interprete text)")
    cur.execute("CREATE TABLE usuario (ID integer PRIMARY KEY AUTOINCREMENT, Cedula integer, Nombre text, Apellido text, Pais text, Ciudad text, Telefono integer, FechaPago text, TDD integer, Pago integer)")
    con.commit()


def insertar_tabla_cancion (con, cur, cancion):
    cur.execute('''INSERT INTO cancion VALUES (?,?,?,?,?)''', cancion)
    con.commit()


def insertar_tabla_usuario (con, cur, usuario):
    cur.execute('''INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?,?)''', usuario)
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
    con.close()
