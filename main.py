import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()

    w.resize(320, 100)
    w.setWindowTitle("Combobox Widget")

    combo = QComboBox(w)
    combo.addItem("Python")
    combo.addItem("Perl")
    combo.addItem("Java")
    combo.addItem("C++")
    combo.move(20, 20)

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
