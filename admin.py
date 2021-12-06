import sqlite3

def conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    except sqlite3.Error:
        print(sqlite3.Error)


def admin_logueado(data):
    pass