import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)
    w = QWidget()

    tab1 = QtGui.QWidget()
    tab2 = QtGui.QWidget()
    tab3 = QtGui.QWidget()
    tab4 = QtGui.QWidget()

    w.resize(320, 240)
    w.setWindowTitle("Files")

    filename = QFileDialog.getOpenFileName(w, 'Open File', '/')
    print(filename)

    with open(filename, 'r') as f:
        print(f.read())

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
