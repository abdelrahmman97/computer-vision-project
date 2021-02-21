from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI.EdgeDetection import Ui_MainWindow
from UI.About import Ui_Dialog
from PyQt5 import QtGui
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Icons//001-code.png'))

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

app = QApplication(sys.argv)
application = MainWindow()
application.show()
app.exec_()
