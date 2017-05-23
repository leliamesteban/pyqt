import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()

    w.setGeometry(100, 100, 200, 50)
    w.setWindowTitle("Hello World!")

    mainMenu = w.menuBar()
    mainMenu.setNativeMenuBar(False)
    fileMenu = mainMenu.addMenu('File')

    exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit Application')
    exitButton.triggered.connect(w.close)
    fileMenu.addAction(exitButton)
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
