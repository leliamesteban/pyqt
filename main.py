import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    table = QTableWidget()
    tableItem = QTableWidgetItem()

    table.setRowCount(4)
    table.setColumnCount(2)

    table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
    table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
    table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
    table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
    table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
    table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
    table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
    table.setItem(3,1, QTableWidgetItem("Item (4,2)"))

    table.show()

    table.cellClicked.connect(cellClick)

    sys.exit(app.exec_())

def cellClick(row, col):
    print("Click on %s" % str(row+1), str(col+1))

if __name__ == '__main__':
    window()
