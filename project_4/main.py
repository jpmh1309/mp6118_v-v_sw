# Costa Rica Institute of Technology
# MP-6118 Validation and Verification in Software Engineering
# Students: 
#           - David Martínez
#           - Jose Martínez
# Project:  Smart Embedded Systems Security Alarm  
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from registers import Registers
import display
import logging
import sys

logger = logging.getLogger(__name__) 

class ExampleApp(QtWidgets.QMainWindow, display.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] - %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("alarm.log", mode='w'),
            logging.StreamHandler()
        ]
    )
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()