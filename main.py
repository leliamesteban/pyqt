import sys
from PyQt4 import QtGui

def window():
    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)
    # QWidget is the base class of all user interface objects in PyQt4
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World")
    w.setGeometry(100, 100, 200, 50)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
