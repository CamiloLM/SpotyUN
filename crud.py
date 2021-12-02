# En este archivo van todas las operaciones para el manejo de la base de datos

import sqlite3
from sqlite3 import Error

def Conexion_BD():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    except Error:
        print(Error)

def crear_tabla(con):
    cursorObj=con.cursor()
    cursorObj.execute("CREATE TABLE cancion (ID integer PRIMARY KEY, Nombre text, Género text, Álbum text, Intérprete text)")
    con.commit()

def leer_info():
    id=input("Código identificador: ")
    id=id.ljust(12)
    nombre=input("Nombre: ")
    genero=input("Género: ")
    album=input("Álbum: ")
    interprete=input("Intérprete: ")
    cancion=(id,nombre,genero,album,interprete)
    return cancion

def insertar_tabla (con,cancion):
    cursorObj=con.cursor()
    cursorObj.execute('''INSERT INTO cancion VALUES (?,?,?,?,?)''',cancion)
    con.commit()

def actualizar_tabla(con):
    cursorObj=con.cursor()
    nombre=input("Nombre: ")
    actualizar='UPDATE cancion set Nombre = "'+nombre+'"'
    print("La cadena es: ",actualizar)
    cursorObj.execute(actualizar)
    con.commit()

def consulta_individual(con,cod):
    cursorObj=con.cursor()
    cursorObj.execute('SELECT ID, Nombre FROM cancion WHERE ID = "'+cod+'"')
    filas=cursorObj.fetchall()
    print("Veremos: ",len(filas)," filas.")
    for row in filas:
        print (row)
    #con.commit()

def consulta_general(con):
    cursorObj=con.cursor()
    cursorObj.execute("SELECT * FROM cancion")
    filas=cursorObj.fetchall()
    print("La información extrída es: ")
    for row in filas:
        numero=row[0]
        nombre=row[1]
        album=row[2]
        print("La información es: ",numero," ",nombre," ",album)
        print("La informacion de la tupla es: ")
        print(row)
    #con.commit()

def cerrar_bd(con):
    con.close()

def menu(con):
    salir=False
    while not salir:
        opcion=input('''MENÚ
                        1. Canciones.
                        2. Planes.
                        3. Clientes.
                        4. Lista de canciones.
                        5. Planes por cliente.
                        6. Salir
        ''')
        if(opcion==1):
            opc1=(input('''
                        1. Crear tabla.
                        2. Ingresar canción.
                        3. Consulta individual.
                        4. Consulta general.
                        5. Actualizar canción.
            '''))
            if (opc1=='1'):
                crear_tabla(con)
            elif (opc1=='2'):
                cancion=leer_info()
                insertar_tabla(con,cancion)  

def main():
    miCon=Conexion_BD()
    menu(miCon)
    #crear_tabla(miCon)
    #cancion=leer_info()
    #print("La canción que se leyó es: ",cancion)
    #insertar_tabla(miCon,cancion)
    #actualizar_tabla(miCon)
    #miCod=input("Codigo a consultar: ")
    #consulta_individual(miCon,miCod)


    miCon.close()

main()
