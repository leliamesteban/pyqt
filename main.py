import os
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Image")

    label = QLabel(w)
    pixmap = QPixmap(os.getcwd() + '/logo.png')
    label.setPixmap(pixmap)
    w.resize(pixmap.width(), pixmap.height())

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
