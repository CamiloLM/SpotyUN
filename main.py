# Este archivo es el ejecutable, maneja el flujo principal del programa
# Los demas modulos tienen que ser invocados desde este archivo
import sqlite3
from sqlite3 import Error

import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

def Conexion_BD():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    except Error:
        print(Error)

def crear_tabla(con):
    ObjCur=con.cursor()
    ObjCur.execute("CREATE TABLE cancion (ID integer PRIMARY KEY, Nombre text, Genero text, Album text, Interprete text)")
    ObjCur.execute("CREATE TABLE usuario (ID integer PRIMARY KEY, Nombre text, Apellido text, Pais text, Ciudad text, Telefono integer, FechaPago date, TDD integer, Pago yesno)")
    con.commit()

def leer_info_cancion():
    id=input("Código identificador: ")
    cmax=12
    fc='0'
    fc1=' '
    id=id.ljust(cmax,fc)
    nombre=input("Nombre: ")
    nombre=nombre.ljust(cmax,fc1)
    genero=input("Género: ")
    genero=genero.ljust(cmax,fc1)
    album=input("Álbum: ")
    album=album.ljust(cmax,fc1)
    interprete=input("Intérprete: ")
    interprete=interprete.ljust(cmax,fc1)
    cancion=(id,nombre,genero,album,interprete)
    return cancion

def leer_info_usuario():
    id=input("Documento de Identificación: ")
    cmax1=10
    cmax2=16
    cmax=12
    fc=' '
    id=id.ljust(cmax1)
    nombre=input("Nombre: ")
    nombre=nombre.ljust(cmax,fc)
    apellido=input("Apellido: ")
    apellido=apellido.ljust(cmax,fc)
    pais=input("Pais: ")
    pais=pais.ljust(cmax,fc)
    ciudad=input("Ciudad: ")
    ciudad=ciudad.ljust(cmax,fc)
    telefono=input("Teléfono: ")
    telefono=telefono.ljust(cmax1)
    fechapago=date.today()
    fechapago = fechapago + timedelta(days=30)
    tarjeta=input("Tarjeta de Crédito: ")
    tarjeta=tarjeta.ljust(cmax2)
    pago=input("Pagó (Yes/No): ")
    usuario=(id,nombre,apellido,pais,ciudad,telefono,fechapago,tarjeta,pago)
    return usuario

def insertar_tabla_cancion (con,cancion):
    ObjCur=con.cursor()
    ObjCur.execute('''INSERT INTO cancion VALUES (?,?,?,?,?)''',cancion)
    con.commit()

def insertar_tabla_usuario (con,usuario):
    ObjCur=con.cursor()
    ObjCur.execute('''INSERT INTO usuario VALUES (?,?,?,?,?,?,?,?,?)''',usuario)
    con.commit()

def main():
    micon=Conexion_BD()
    usuario=leer_info_usuario()
    #cancion=leer_info_cancion()
    insertar_tabla_usuario(micon,usuario)
    #insertar_tabla_cancion(micon,cancion)

main()