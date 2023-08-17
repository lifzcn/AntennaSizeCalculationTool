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
        self.createSignalSlot()

    def createSignalSlot(self):
        self.pushButton_1.clicked.connect(self.function1)
        self.pushButton_2.clicked.connect(self.function2)
        self.pushButton_3.clicked.connect(self.function3)
        self.pushButton_4.clicked.connect(self.function4)
        self.pushButton_5.clicked.connect(self.function5)

    def function1(self):
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()

        # 光速
        c = 3.0 * np.power(10.0, 8)

        # 介质的介电常数
        epsilon_r = float(self.lineEdit_1.text())

        # 天线的中心工作频率
        f = float(self.lineEdit_2.text()) * np.power(10.0, 9)

        # 波长
        lambda_c = c / f

        # 介质基片的厚度
        H = float(self.lineEdit_3.text()) * np.power(10.0, -3)

        # 高效率辐射贴片的宽度
        W = c / 2.0 / f * np.power((epsilon_r + 1.0) / 2.0, -1 / 2)

        # 有效介电常数
        epsilon_e = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 * np.power(1.0 + 12.0 * H / W, -1 / 2)

        # 等效辐射缝隙长度
        Delta_L = 0.412 * H * (epsilon_e + 0.3) * (W / H + 0.264) / (epsilon_e - 0.258) / (W / H + 0.8)

        # 介质内的导波波长
        lambda_e = c / f / np.sqrt(epsilon_e)

        # 实际辐射单元长度
        L = c / 2.0 / f / np.sqrt(epsilon_e) - 2.0 * Delta_L

        xi_re = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 * np.power(1.0 + 12.0 * H / L, -1 / 2)

        # 馈电点位置類
        L1 = L / 2.0 * 1.0 / np.sqrt(xi_re)

        self.lineEdit_4.setText(str(round(lambda_c * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_5.setText(str(round(W * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_6.setText(str(round(L * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_7.setText(str(round(lambda_e * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_8.setText(str(round(epsilon_e, 3)))
        self.lineEdit_9.setText(str(round(Delta_L * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_10.setText(str(round(L1 * np.power(10.0, 3), 3)) + " mm")
        self.lineEdit_11.setText(str(round(xi_re, 3)))

    def function2(self):
        sys.exit(app.exec())

    def function3(self):
        self.lineEdit_14.clear()
        epsilon_r = float(self.lineEdit_1.text())
        r = float(self.lineEdit_12.text()) * np.power(10.0, -3)
        R = float(self.lineEdit_13.text()) * np.power(10.0, -3)
        Zo = 60.0 / np.sqrt(epsilon_r) * np.log(R / r)
        self.lineEdit_14.setText(str(round(Zo, 3)) + " ohm")

    def function4(self):
        self.lineEdit_17.clear()
        epsilon_r = float(self.lineEdit_1.text())
        r = float(self.lineEdit_15.text()) * np.power(10.0, -3)
        Zo = float(self.lineEdit_16.text())
        R = r * np.exp(Zo * np.sqrt(epsilon_r) / 60.0)
        self.lineEdit_17.setText(str(round(R * np.power(10.0, 3), 3)) + " mm")

    def function5(self):
        self.lineEdit_20.clear()
        epsilon_r = float(self.lineEdit_1.text())
        R = float(self.lineEdit_18.text()) * np.power(10.0, -3)
        Zo = float(self.lineEdit_19.text())
        r = R / np.exp(Zo * np.sqrt(epsilon_r) / 60.0)
        self.lineEdit_20.setText(str(round(r * np.power(10.0, 3), 3)) + " mm")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())
