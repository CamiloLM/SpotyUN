from PyQt5.QtWidgets import QTableWidgetItem
from QTable import *
from sqlite3 import connect
from cliente import Cliente
from cancion import Cancion
import sys

# pyuic5 QTable.ui -o QTable.py
headers = ("Cedula", "Nombre", "Apellido", "Correo", "Pais", "Ciudad", "Telefono", "Tarjeta credito", "Fecha Pago", "Pago")

con = connect('SpotyUN.db')
cur = con.cursor()

data = Cliente().consulta_usuario_general(cur)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(2)
        self.ui.tableWidget.setColumnCount(10)
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)  # set header text

        row=0
        for cliente in data:
            col=0
            print("")
            for elem in cliente:
                print(row, col, elem)
                cellinfo = QTableWidgetItem(elem)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) # Haciendo que no se pueda editar
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

        self.ui.pushButton.setText("Cambiar a cancion")
        self.ui.pushButton.clicked.connect(self.cancion)
        self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.sortItems(0)
        # self.ui.tableWidget.sortByColumn(0, QtCore.Qt.AscendingOrder)  # sort by the first column


    def cancion(self):
        self.ui.tableWidget.clear()
        data = Cancion().consulta_canciones(cur)
        headers = ("Codigo", "Nombre", "Ubicación", "Género", "Album", "Interprete", "Fotografía")
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)  # set header text

        row=0
        for cliente in data:
            col=0
            print("")
            for elem in cliente:
                print(row, col, elem)
                cellinfo = QTableWidgetItem(elem)
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled) # Haciendo que no se pueda editar
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1


app = QtWidgets.QApplication([])
win = mywindow()
win.show()
sys.exit(app.exec())
