import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()

    w.resize(320, 240)
    w.setWindowTitle("Calendar Widget")

    cal = QCalendarWidget(w)
    cal.setGridVisible(True)
    cal.move(0, 0)
    cal.resize(320, 240)

    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
