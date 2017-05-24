import sys
from PyQt4 import QtGui
from PyQt4.QtGui import *

def window():

    # Create a PyQt4 application object
    app = QtGui.QApplication(sys.argv)
    tabs = QtGui.QTabWidget()

    tab1 = QtGui.QWidget()
    tab2 = QtGui.QWidget()
    tab3 = QtGui.QWidget()
    tab4 = QtGui.QWidget()

    tabs.resize(250, 150)

    vBoxLayout = QtGui.QVBoxLayout()
    pushButton1 = QtGui.QPushButton("Start")
    pushButton2 = QtGui.QPushButton("Settings")
    pushButton3 = QtGui.QPushButton("Stop")
    vBoxLayout.addWidget(pushButton1)
    vBoxLayout.addWidget(pushButton2)
    vBoxLayout.addWidget(pushButton3)
    tab1.setLayout(vBoxLayout)

    tabs.addTab(tab1, "Tab 1")
    tabs.addTab(tab2, "Tab 2")
    tabs.addTab(tab3, "Tab 3")
    tabs.addTab(tab4, "Tab 4")

    tabs.setWindowTitle("Tabs")
    tabs.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
