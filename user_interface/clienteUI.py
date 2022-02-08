from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
# from QTable import *
# from multiprocessing.spawn import prepare
# import sys
"""Importa las librerías de PyQT5 para su correcto funcionamiento"""


class Cliente(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto Cliente"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_menu.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from cliente")

        self.ConsultaTable_4.setSelectionBehavior(QTableView.SelectRows)
        self.ConsultaTable_4.setModel(self.consultaModel)
        self.ConsultaTable_4.verticalHeader().setVisible(False)
        """Métodos para la consulta de clientes en la base de datos"""

        self.filtrarModel = QSqlTableModel(self)
        self.filtrarModel.setTable("cliente")
        self.filtrarModel.select()

        self.SortTable_4.setEditTriggers(QTableView.NoEditTriggers)
        self.SortTable_4.setSelectionBehavior(QTableView.SelectRows)
        self.SortTable_4.setModel(self.filtrarModel)
        self.SortTable_4.verticalHeader().setVisible(False)
        self.SortTable_4.setSortingEnabled(True)
        """Métodos para ordenar los clientes de la base de datos."""

        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("cliente")
        self.borrarModel.select()

        self.BorrarTable_4.setEditTriggers(QTableView.NoEditTriggers)
        self.BorrarTable_4.setSelectionBehavior(QTableView.SelectRows)
        self.BorrarTable_4.setModel(self.borrarModel)
        self.BorrarTable_4.verticalHeader().setVisible(False)
        """Métodos para borrar clientes en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("cliente")
        self.actualizarModel.select()

        self.ActualizarTable_4.setModel(self.actualizarModel)
        self.ActualizarTable_4.verticalHeader().setVisible(False)
        """Métodos para actualizar los clientes en la base de datos."""

        self.ConsultaIntput_4.textEdited.connect(
            self.onConsultaIntput_textEdited)
        """Ejecuta el line edit que consulta específicamente un cliente"""

        self.BorrarTable_4.clicked.connect(self.onDeleteInfo_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""
        self.ConsultaRefresh_4.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.BorrarRefresh_4.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.ActualizarRefresh_4.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de update.
        self.Registrar_4.clicked.connect(self.onRegister_clicked)
        # Botón que al clickarse ingresa un nuevo cliente a la bd.

    def onDeleteInfo_clicked(self, index):
        """Función para borrar registros de la db"""
        if (QMessageBox.question(self, "Borrar datos.", "¿Desea borrar este cliente?", QMessageBox.Yes | QMessageBox.No)
                == QMessageBox.Yes):
            row = index.row()
            if self.borrarModel.removeRow(row):
                self.borrarModel.select()

    def onConsultaIntput_textEdited(self, txt):
        """Función para que un lineedit enseñe info específica en la db"""
        self.consultaModel.setQuery("select * from cliente where cedula like '%" + txt + "%'")

    def onRefresh_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from cliente")
        self.borrarModel.select()
        self.actualizarModel.select()

    def onRegister_clicked(self):
        """Función para registrar cliente en la bd."""
        cedula = self.Reg_CedulaInput_4.text()
        nombre = self.Reg_NombreInput_4.text()
        apellido = self.Reg_ApellidoInput_4.text()
        correo = self.Reg_CorreoInput_4.text()        
        pais = self.Reg_PaisInput_4.text()
        ciudad = self.Reg_CiudadInput_4.text()
        telefono = self.Reg_TelefonoInput_4.text()
        tarjeta_credito = self.Reg_TarjetaInput_4.text()
        fecha_pago = self.Reg_FechaInput_4.text()
        pago = self.Reg_PagoInput_4.text()
        """Datos que lee la bd"""

        if (cedula == "" or nombre == "" or apellido == "" or correo == "" or pais == "" or ciudad == "" or telefono == "" or tarjeta_credito == "" or fecha_pago == "" or pago == ""):
            QMessageBox.critical(self, "Error", "Rellene todos los espacios.")
            return
        """Mensajes de error si falta algún dato por ingresar."""

        cedula = int(cedula)
        telefono = int(telefono)
        tarjeta_credito = int(tarjeta_credito)
        pago = int(pago)

        q = QSqlQuery()
        if (q.prepare("INSERT OR IGNORE INTO cliente VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")):
            """Se ingresan los registros a la bd"""
            q.addBindValue(cedula)
            q.addBindValue(nombre)
            q.addBindValue(apellido)
            q.addBindValue(correo)
            q.addBindValue(pais)
            q.addBindValue(ciudad)
            q.addBindValue(telefono)
            q.addBindValue(tarjeta_credito)
            q.addBindValue(fecha_pago)
            q.addBindValue(pago)
            if (q.exec()):
                if (QMessageBox.question(self, "Listo.", "Listo. ¿Desea limpiar campos?", QMessageBox.Yes | QMessageBox.No)
                        == QMessageBox.Yes):
                    self.Reg_CedulaInput_4.clear()
                    self.Reg_NombreInput_4.clear()
                    self.Reg_ApellidoInput_4.clear()
                    self.Reg_CorreoInput_4.clear()
                    self.Reg_PaisInput_4.clear()
                    self.Reg_CiudadInput_4.clear()
                    self.Reg_TelefonoInput_4.clear()
                    self.Reg_TarjetaInput_4.clear()
                    self.Reg_FechaInput_4.clear()
                    self.Reg_PagoInput_4.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""

