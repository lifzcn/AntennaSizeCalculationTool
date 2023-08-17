"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/8/17
# Author     ：LiFZ
# Email      ：lifzcn@gmail.com
# Description：
"""

import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget
from AppUI import Ui_Form


class mainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())
