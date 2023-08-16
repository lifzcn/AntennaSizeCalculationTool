"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/8/15
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
        self.createSignalSlot()

    def createSignalSlot(self):
        self.pushButton_1.clicked.connect(self.calculate)

    def calculate(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()

        c = 3.0 * np.power(10.0, 8)

        # 介质的介电常数
        epsilon_r = float(self.lineEdit_1.text())

        # 天线的中心工作频率
        f = float(self.lineEdit_2.text()) * np.power(10.0, 9)

        # 介质基片的厚度
        H = float(self.lineEdit_9.text()) * np.power(10.0, -3)

        # 高效率辐射贴片的宽度
        W = c / 2 / f * np.power((epsilon_r + 1) / 2, -1 / 2)

        # 有效介电常数
        epsilon_e = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * np.power(1 + 12 * H / W, -1 / 2)

        # 等效辐射缝隙长度
        Delta_L = 0.412 * H * (epsilon_e + 0.3) * (W / H + 0.264) / (epsilon_e - 0.258) / (W / H + 0.8)

        # 介质内的导波波长
        lambda_e = c / f / np.sqrt(epsilon_e)

        # 实际辐射单元长度
        L = c / f * np.sqrt(epsilon_r) - 2 * Delta_L

        xi_re = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * np.power(1 + 12 * H / L, -1 / 2)

        # 馈电点位置
        L1 = L / 2 * (1 - 1 / np.sqrt(xi_re))

        self.lineEdit_3.insert(str(round(W * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_4.setText(str(round(L * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_5.setText(str(round(lambda_e, 3)) + " m")
        self.lineEdit_6.setText(str(round(epsilon_e, 3)))
        self.lineEdit_7.setText(str(round(Delta_L * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_8.setText(str(round(L1 * np.power(10.0, 3), 3)) + " mm")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())
