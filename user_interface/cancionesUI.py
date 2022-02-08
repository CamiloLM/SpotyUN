from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
# from QTable import *
# from multiprocessing.spawn import prepare
# import sys
"""Importa las librerías de PyQT5 para su correcto funcionamiento"""


class Cancion(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto Cancion"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_menu.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from cancion")

        self.ConsultaTable_3.setSelectionBehavior(QTableView.SelectRows)
        self.ConsultaTable_3.setModel(self.consultaModel)
        self.ConsultaTable_3.verticalHeader().setVisible(False)
        """Métodos para la consulta de canciones en la base de datos"""

        self.filtrarModel = QSqlTableModel(self)
        self.filtrarModel.setTable("cancion")
        self.filtrarModel.select()

        self.SortTable_3.setEditTriggers(QTableView.NoEditTriggers)
        self.SortTable_3.setSelectionBehavior(QTableView.SelectRows)
        self.SortTable_3.setModel(self.filtrarModel)
        self.SortTable_3.verticalHeader().setVisible(False)
        self.SortTable_3.setSortingEnabled(True)
        """Métodos para ordenar las canciones de la base de datos."""

        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("cancion")
        self.borrarModel.select()

        self.BorrarTable_3.setEditTriggers(QTableView.NoEditTriggers)
        self.BorrarTable_3.setSelectionBehavior(QTableView.SelectRows)
        self.BorrarTable_3.setModel(self.borrarModel)
        self.BorrarTable_3.verticalHeader().setVisible(False)
        """Métodos para borrar canciones en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("cancion")
        self.actualizarModel.select()

        self.ActualizarTable_3.setModel(self.actualizarModel)
        self.ActualizarTable_3.verticalHeader().setVisible(False)
        """Métodos para actualizar las canciones en la base de datos."""

        self.ConsultaIntput_3.textEdited.connect(
            self.onConsultaIntput_textEdited)
        """Ejecuta el line edit que consulta específicamente una cancion"""

        self.BorrarTable_3.clicked.connect(self.onDeleteInfo_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""
        self.ConsultaRefresh_3.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.BorrarRefresh_3.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.ActualizarRefresh_3.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de update.
        self.Registrar_3.clicked.connect(self.onRegister_clicked)
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
        self.consultaModel.setQuery("select * from cancion where codigo like '%" + txt + "%'")

    def onRefresh_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from cancion")
        self.borrarModel.select()
        self.actualizarModel.select()

    def onRegister_clicked(self):
        """Función para registrar cancion en la bd."""    
        codigo = self.Reg_CodigoInput_3.text()
        nombre = self.Reg_NombreInput_3.text()
        ubicacion = self.Reg_UbicacionInput_3.text()
        genero = self.Reg_GeneroInput_3.text()
        album = self.Reg_AlbumInput_3.text()
        interprete = self.Reg_InterpreteInput_3.text()
        fotografia = self.Reg_FotografiaInput_3.text()
        """Datos que lee la bd"""

        if (codigo == "" or nombre == "" or ubicacion == "" or genero == "" or album == "" or interprete == "" or fotografia == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        """Mensaje de error si falta algún dato por ingresar."""

        codigo = int(codigo)
        print(codigo, nombre, ubicacion, genero, album, interprete, fotografia)

        q = QSqlQuery()
        if (q.prepare("INSERT OR IGNORE INTO cancion (codigo, nombre, ubicacion, genero, album, interprete, fotografia) VALUES (?, ?, ?, ?, ?, ?, ?)")):
            """Se ingresan los registros a la bd"""
            q.addBindValue(codigo)
            q.addBindValue(nombre)
            q.addBindValue(ubicacion)
            q.addBindValue(genero)
            q.addBindValue(album)
            q.addBindValue(interprete)
            q.addBindValue(fotografia)
            if (q.exec()):
                print("Insercion realizada con exito")
                if (QMessageBox.question(self, "Listo.", "Listo. ¿Desea limpiar campos?", QMessageBox.Yes | QMessageBox.No)
                        == QMessageBox.Yes):
                    print("Limpiando los datos")
                    self.Reg_CodigoInput_3.clear()
                    self.Reg_NombreInput_3.clear()
                    self.Reg_UbicacionInput_3.clear()
                    self.Reg_GeneroInput_3.clear()
                    self.Reg_AlbumInput_3.clear()
                    self.Reg_InterpreteInput_3.clear()
                    self.Reg_FotografiaInput_3.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""

