import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()

    w.resize(320, 100)
    w.setWindowTitle("Textbox Widget")

    textbox = QLineEdit(w)
    textbox.move(20, 20)
    textbox.resize(280, 40)
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
