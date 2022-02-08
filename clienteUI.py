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
        if (q.prepare("CREATE TABLE IF NOT EXISTS cliente (cedula INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL, correo TEXT NOT NULL, pais TEXT, ciudad TEXT, telefono INTEGER, tarjetaCredito INTEGER, fechaPago TEXT, pago INTEGER)")):
            if (q.exec()):
                print("Tabla cliente creada.")


def cliente_app():
    "Función para iniciar el programa."
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    cliente = Cliente()
    cliente.show()
    sys.exit(app.exec_())


class Cliente(QMainWindow):
    def __init__(self):
        """Método constructor, inicializa los argumentos del objeto Cliente"""
        QMainWindow.__init__(self)
        uic.loadUi("ui_cliente.ui", self)

        self.consultaModel = QSqlQueryModel(self)
        self.consultaModel.setQuery("select * from cliente")

        self.ConsultaTable.setSelectionBehavior(QTableView.SelectRows)
        self.ConsultaTable.setModel(self.consultaModel)
        self.ConsultaTable.verticalHeader().setVisible(False)
        """Métodos para la consulta de clientes en la base de datos"""

        self.filtrarModel = QSqlTableModel(self)
        self.filtrarModel.setTable("cliente")
        self.filtrarModel.select()


        self.SortTable.setEditTriggers(QTableView.NoEditTriggers)
        self.SortTable.setSelectionBehavior(QTableView.SelectRows)
        self.SortTable.setModel(self.filtrarModel)
        self.SortTable.verticalHeader().setVisible(False)
        self.SortTable.setSortingEnabled(True)
        """Métodos para ordenar los clientes de la base de datos."""

        self.borrarModel = QSqlTableModel(self)
        self.borrarModel.setTable("cliente")
        self.borrarModel.select()
        self.BorrarTable.setEditTriggers(QTableView.NoEditTriggers)
        self.BorrarTable.setSelectionBehavior(QTableView.SelectRows)
        self.BorrarTable.setModel(self.borrarModel)
        self.BorrarTable.verticalHeader().setVisible(False)
        """Métodos para borrar clientes en la base de datos."""

        self.actualizarModel = QSqlTableModel(self)
        self.actualizarModel.setTable("cliente")
        self.actualizarModel.select()
        self.ActualizarTable.setModel(self.actualizarModel)
        self.ActualizarTable.verticalHeader().setVisible(False)
        """Métodos para actualizar los clientes en la base de datos."""

        self.ConsultaIntput.textEdited.connect(
            self.onConsultaIntput_textEdited)
        """Ejecuta el line edit que consulta específicamente un cliente"""

        self.BorrarTable.clicked.connect(self.onDeleteInfo_clicked)
        """Ejecuta la tabla que borrará info de la base de datos"""

        self.ConsultaRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de consultas.
        self.BorrarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de borrado.
        self.ActualizarRefresh.clicked.connect(self.onRefresh_clicked)
        # Botón que al clickarse actualiza la información de la tabla de update.
        self.Registrar.clicked.connect(self.onRegister_clicked)
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
        self.consultaModel.setQuery(
            "select * from cliente where cedula like '%" + txt + "%'")

    def onRefresh_clicked(self):
        """Función que le da un botón la capacidad de actualizar la info mostrada en la app"""
        self.consultaModel.setQuery("select * from cliente")
        self.borrarModel.select()
        self.actualizarModel.select()

    def onRegister_clicked(self):
        """Función para registrar cliente en la bd."""

        cedula = self.Reg_CedulaInput.text()
        nombre = self.Reg_NombreInput.text()
        apellido = self.Reg_ApellidoInput.text()
        correo = self.Reg_CorreoInput.text()        
        pais = self.Reg_PaisInput.text()
        ciudad = self.Reg_CiudadInput.text()
        telefono = self.Reg_TelefonoInput.text()
        tarjeta_credito = self.Reg_TarjetaInput.text()
        fecha_pago = self.Reg_FechaInput.text()
        pago = self.Reg_PagoInput.text()
        """Datos que lee la bd"""

        if (cedula == "" or nombre == "" or apellido == "" or correo == "" or pais == "" or ciudad == "" or telefono == "" or tarjeta_credito == "" or fecha_pago == "" or pago == ""):
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
                    self.Reg_CedulaInput.clear()
                    self.Reg_NombreInput.clear()
                    self.Reg_ApellidoInput.clear()
                    self.Reg_CorreoInput.clear()
                    self.Reg_PaisInput.clear()
                    self.Reg_CiudadInput.clear()
                    self.Reg_TelefonoInput.clear()
                    self.Reg_TarjetaInput.clear()
                    self.Reg_FechaInput.clear()
                    self.Reg_PagoInput.clear()
                    """Funciones para limpiar el tablero de ingresar datos."""

