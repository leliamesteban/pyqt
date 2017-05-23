import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    # QWidget is the base class of all user interface objects in PyQt4
    w = QtGui.QWidget()

    result = QMessageBox.question(w, 'Message', "Do you like python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if result == QMessageBox.Yes:
        print("Yes")
    else:
        print("No")
    w.setGeometry(100, 100, 200, 50)
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
