from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from user_interface.planesUI import plan
import sys

def ConBD():
    """Conexión con la bd de SQLite por medio de PyQT"""
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("SpotyUN.db")
    if (db.open()):
        q = QSqlQuery()
        if (q.prepare("create table if no exists planes(codigo integer primary key autoincrement not null, nombre text not null, valor float not null, cantidad integer not null) ")):
            if (q.exec()):
                print("Tabla planes creada.")


def planes_app():
    "Función para iniciar el programa."
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    planes = plan()
    planes.show()
    sys.exit(app.exec_())

def mainui():
    ConBD()
    planes_app()

if __name__ == "__main__":
    mainui()