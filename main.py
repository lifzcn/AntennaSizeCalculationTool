"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/8/15
# Author     ：LiFZ
# Email      ：lifzcn@gmail.com
# Version    ：python 3.10
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
        self.createSignalSlot()

    def createSignalSlot(self):
        self.pushButton_1.clicked.connect(self.calculate)

    def calculate(self):
        c = 3.0 * np.power(10, 8)

        # H = 0.762 * np.power(10, -3)

        epsilon_r = float(self.lineEdit_1.text())

        f = float(self.lineEdit_2.text())

        H = float(self.lineEdit_9.text())

        W = (c / 2 * f) * np.power((epsilon_r + 1) / 2, -1 / 2)

        epsilon_e = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * np.power(1 + 12 * H / W, -1 / 2)

        Delta_L = 0.412 * H * (epsilon_e + 0.3) * (W / H + 0.264) / (epsilon_e - 0.258) / (W / H + 0.8)

        lambda_e = c / f / np.sqrt(epsilon_e)

        L = c / f * np.sqrt(epsilon_r) - 2 * Delta_L

        xi_re = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * np.power(1 + 12 * H / L, -1 / 2)

        L1 = L / 2 * (1 - 1 / np.sqrt(xi_re))

        self.lineEdit_3.insert(str(W))

        self.lineEdit_4.setText(str(L))

        self.lineEdit_5.setText(str(lambda_e))

        self.lineEdit_6.setText(str(epsilon_e))

        self.lineEdit_7.setText(str(Delta_L))

        self.lineEdit_8.setText(str(L1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())
