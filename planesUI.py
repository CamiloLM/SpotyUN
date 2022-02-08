from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
# from QTable import *
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
                print("Tabla planes creada.")


def planes_app():
    "Función para iniciar el programa."
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    planes = plan()
    planes.show()
    sys.exit(app.exec_())


class plan(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto 'Plan'"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_menu.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from planes")
        self.ConsultaTable.setSelectionBehavior(QTableView.SelectRows)
        self.ConsultaTable.setModel(self.consultaModel)
        self.ConsultaTable.verticalHeader().setVisible(False)
        """Métodos para la consulta de planes en la base de datos"""

        self.filtrarModel = QSqlTableModel(self)
        self.filtrarModel.setTable("planes")
        self.filtrarModel.select()
        self.SortTable.setEditTriggers(QTableView.NoEditTriggers)
        self.SortTable.setSelectionBehavior(QTableView.SelectRows)
        self.SortTable.setModel(self.filtrarModel)
        self.SortTable.verticalHeader().setVisible(False)
        self.SortTable.setSortingEnabled(True)
        """Métodos para ordenar los planes de la base de datos."""

        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("planes")
        self.borrarModel.select()
        self.BorrarTable.setEditTriggers(QTableView.NoEditTriggers)
        self.BorrarTable.setSelectionBehavior(QTableView.SelectRows)
        self.BorrarTable.setModel(self.borrarModel)
        self.BorrarTable.verticalHeader().setVisible(False)
        """Métodos para borrar planes en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("planes")
        self.actualizarModel.select()
        self.ActualizarTable.setModel(self.actualizarModel)
        self.ActualizarTable.verticalHeader().setVisible(False)
        """Métodos para actualizar los planes en la base de datos."""

        self.ConsultaIntput.textEdited.connect(
            self.onConsultaIntput_textEdited)
        """Ejecuta el line edit que consulta específicamente un plan"""

        self.BorrarTable.clicked.connect(self.onDeleteInfo_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""

        self.ConsultaRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.BorrarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.ActualizarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de update.
        self.SortRefresh.clicked.connect(self.onRefresh_clicked)
        self.Registrar.clicked.connect(self.onRegister_clicked)
        # Botón que al clickarse ingresa un nuevo plan a la bd.

    def onDeleteInfo_clicked(self, index):
        """Función para borrar registros de la db"""
        if (QMessageBox.question(self, "Borrar datos.", "¿Desea borrar este plan?", QMessageBox.Yes | QMessageBox.No)
                == QMessageBox.Yes):
            row = index.row()
            if self.borrarModel.removeRow(row):
                self.borrarModel.select()

    def onConsultaIntput_textEdited(self, txt):
        """Función para que un lineedit enseñe info específica en la db"""
        self.consultaModel.setQuery(
            "select * from planes where codigo like '%" + txt + "%'")

    def onRefresh_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from planes")
        self.borrarModel.select()
        self.actualizarModel.select()
        self.filtrarModel.select()

    def onRegister_clicked(self):
        """Función para registrar planes en la bd."""

        codigo = self.Reg_CodigoInput.text()
        nombre = self.Reg_NombreInput.text()
        valor = self.Reg_ValorInput.text()
        cantidad = self.Reg_CantidadInput.text()
        """Datos que lee la bd"""

        if (codigo == "" or nombre == "" or valor == "" or cantidad == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        """
        if (nombre == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        if (valor == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        if (cantidad == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
            """
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
                    self.Reg_CodigoInput.clear()
                    self.Reg_NombreInput.clear()
                    self.Reg_ValorInput.clear()
                    self.Reg_CantidadInput.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""


if __name__ == "__main__":
    ConBD()
    planes_app()
