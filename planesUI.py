from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from multiprocessing.spawn import prepare
import sys
"""Importa las librerías de PyQT5 para su correcto funcionamiento"""

def ConBD():
    """Conexión con la bd de SQLite por medio de PyQT"""
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("SpotyUN.db")
    if (db.open()):
        q = QSqlQuery()
        if (q.prepare("create table if no exists planes(codigo integer primary key autoincrement not null, nombre text not null, valor float not null, cantidad integer not null) ")):
            if (q.exec()):
                print ("Tabla planes creada.")

def planes_app():
    "Función para iniciar el programa."
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = plan()
    w.show()
    sys.exit(app.exec_())

class plan(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto 'Plan'"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_planes.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from planes")
        self.tableView.setModel(self.consultaModel)
        """Métodos para la consulta de planes en la base de datos"""
        
        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("planes")
        self.borrarModel.select()
        self.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_2.setSelectionBehavior(QTableView.SelectRows)
        self.tableView_2.setModel(self.borrarModel)
        """Métodos para borrar planes en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("planes")
        self.actualizarModel.select()
        self.tableView_3.setModel(self.actualizarModel)
        """Métodos para actualizar los planes en la base de datos."""

        self.lineEdit_6.textEdited.connect(self.onLineEdit_6_textEdited)
        """Ejecuta el line edit que consulta específicamente un plan"""

        self.tableView_2.clicked.connect(self.onBorrartableView_2_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""
        
        self.pushButton.clicked.connect(self.onPushButton_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.pushButton_2.clicked.connect(self.onPushButton_2_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.pushButton_3.clicked.connect(self.onPushButton_3_clicked)
        # Botón que al clickarse ingresa un nuevo plan a la bd.
        self.pushButton_4.clicked.connect(self.onPushButton_4_clicked)
        # Botón que al clickarse cierra el programa (Provisional)
        
    
    def onPushButton_4_clicked(self):
        """Función para cerrar la app (provisional."""
        self.close()


    def onBorrartableView_2_clicked(self, index):
        """Función para borrar registros de la db"""
        if (QMessageBox.question(self, "Borrar datos.", "¿Desea borrar este plan?", QMessageBox.Yes | QMessageBox.No)
        == QMessageBox.Yes):
            row = index.row()
            if self.borrarModel.removeRow(row):
                self.borrarModel.select()

    def onLineEdit_6_textEdited(self, txt):
        """Función para que un lineedit enseñe info específica en la db"""
        self.consultaModel.setQuery("select * from planes where codigo like '%" + txt + "%'")

    def onPushButton_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from planes")
    
    def onPushButton_2_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.borrarModel.select()

    def onPushButton_3_clicked(self):
        """Función para registrar planes en la bd."""

        codigo = self.lineEdit_2.text()
        nombre = self.lineEdit_3.text()
        valor = self.lineEdit_4.text()
        cantidad = self.lineEdit_5.text()
        """Datos que lee la bd"""

        if (codigo == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        if (nombre == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        if (valor == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        if (cantidad == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        """Mensajes de error si falta algún dato por ingresar."""
        
        codigo = int(codigo)
        valor = float(valor)
        cantidad = int(cantidad)

        q = QSqlQuery()
        if (q.prepare("insert or ignore into planes (codigo, nombre, valor, cantidad) values (?, ?, ?, ?)")):
            """Se ingresan los registros a la bd"""
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(valor)
            q.addBindValue(cantidad)
            if (q.exec()):
                if (QMessageBox.question(self, "Listo.", "Listo. ¿Desea limpiar campos?", QMessageBox.Yes | QMessageBox.No) 
                == QMessageBox.Yes):
                    self.lineEdit_2.clear()
                    self.lineEdit_3.clear()
                    self.lineEdit_4.clear()
                    self.lineEdit_5.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""


# if __name__ == "__main__":
#    ConBD()
#    planes_app()