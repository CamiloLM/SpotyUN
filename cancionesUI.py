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
        if (q.prepare("CREATE TABLE IF NOT EXISTS cancion (codigo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, ubicacion TEXT NOT NULL, genero TEXT, album TEXT, interprete TEXT, fotografia TEXT)")):
            if (q.exec()):
                print("Tabla cancion creada.")


def cancion_app():
    "Función para iniciar el programa."
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    cancion = Cancion()
    cancion.show()
    sys.exit(app.exec_())


class Cancion(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto Cancion"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_cancion.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from cancion")

        self.ConsultaTable.setSelectionBehavior(QTableView.SelectRows)
        self.ConsultaTable.setModel(self.consultaModel)
        self.ConsultaTable.verticalHeader().setVisible(False)
        """Métodos para la consulta de canciones en la base de datos"""

        self.filtrarModel = QSqlTableModel(self)
        self.filtrarModel.setTable("cancion")
        self.filtrarModel.select()


        self.SortTable.setEditTriggers(QTableView.NoEditTriggers)
        self.SortTable.setSelectionBehavior(QTableView.SelectRows)
        self.SortTable.setModel(self.filtrarModel)
        self.SortTable.verticalHeader().setVisible(False)
        self.SortTable.setSortingEnabled(True)
        """Métodos para ordenar las canciones de la base de datos."""

        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("cancion")
        self.borrarModel.select()
        self.BorrarTable.setEditTriggers(QTableView.NoEditTriggers)
        self.BorrarTable.setSelectionBehavior(QTableView.SelectRows)
        self.BorrarTable.setModel(self.borrarModel)
        self.BorrarTable.verticalHeader().setVisible(False)
        """Métodos para borrar canciones en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("cancion")
        self.actualizarModel.select()
        self.ActualizarTable.setModel(self.actualizarModel)
        self.ActualizarTable.verticalHeader().setVisible(False)
        """Métodos para actualizar las canciones en la base de datos."""

        self.ConsultaIntput.textEdited.connect(
            self.onConsultaIntput_textEdited)
        """Ejecuta el line edit que consulta específicamente una cancion"""

        self.BorrarTable.clicked.connect(self.onDeleteInfo_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""

        self.ConsultaRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.BorrarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.ActualizarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de update.
        self.Registrar.clicked.connect(self.onRegister_clicked)
        # Botón que al clickarse ingresa una nueva cancion a la bd.

    def onDeleteInfo_clicked(self, index):
        """Función para borrar registros de la db"""
        if (QMessageBox.question(self, "Borrar datos.", "¿Desea borrar esta cancion?", QMessageBox.Yes | QMessageBox.No)
                == QMessageBox.Yes):
            row = index.row()
            if self.borrarModel.removeRow(row):
                self.borrarModel.select()

    def onConsultaIntput_textEdited(self, txt):
        """Función para que un lineedit enseñe info específica en la db"""
        self.consultaModel.setQuery(
            "select * from cancion where codigo like '%" + txt + "%'")

    def onRefresh_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from cancion")
        self.borrarModel.select()
        self.actualizarModel.select()

    def onRegister_clicked(self):
        """Función para registrar cancion en la bd."""

        codigo = self.Reg_CodigoInput.text()
        nombre = self.Reg_NombreInput.text()
        ubicacion = self.Reg_UbicacionInput.text()
        genero = self.Reg_GeneroInput.text()
        interprete = self.Reg_InterpreteInput.text()
        fotografia = self.Reg_FotografiaInput.text()
        """Datos que lee la bd"""

        if (codigo == "" or nombre == "" or ubicacion == "" or genero == "" or interprete == "" or fotografia == ""):
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

        q = QSqlQuery()
        if (q.prepare("INSERT OR IGNORE INTO cancion (codigo, nombre, ubicacion, genero, interprete, fotografia) VALUES (?, ?, ?, ?, ?, ?, ?)")):
            """Se ingresan los registros a la bd"""
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(ubicacion)
            q.addBindValue(genero)
            q.addBindValue(interprete)
            q.addBindValue(fotografia)
            if (q.exec()):
                if (QMessageBox.question(self, "Listo.", "Listo. ¿Desea limpiar campos?", QMessageBox.Yes | QMessageBox.No)
                        == QMessageBox.Yes):
                    self.Reg_CodigoInput.clear()
                    self.Reg_NombreInput.clear()
                    self.Reg_UbicacionInput.clear()
                    self.Reg_GeneroInput.clear()
                    self.Reg_InterpreteInput.clear()
                    self.Reg_FotografiaInput.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""

