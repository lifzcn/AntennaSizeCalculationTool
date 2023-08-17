# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        Form.setMaximumSize(QSize(640, 480))
        self.groupBox_1 = QGroupBox(Form)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(20, 10, 351, 451))
        self.groupBox_3 = QGroupBox(self.groupBox_1)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(19, 29, 311, 111))
        self.widget = QWidget(self.groupBox_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 151, 74))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(self.widget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.widget1 = QWidget(self.groupBox_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(200, 20, 77, 71))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1 = QPushButton(self.widget1)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_1)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(19, 159, 311, 281))
        self.widget2 = QWidget(self.groupBox_4)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 20, 271, 251))
        self.gridLayout_3 = QGridLayout(self.widget2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.widget2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.widget2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.widget2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.label_7 = QLabel(self.widget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.widget2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_7, 3, 1, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.widget2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_8, 4, 1, 1, 1)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_9, 5, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.widget2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_9, 5, 1, 1, 1)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.widget2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_10, 6, 1, 1, 1)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_11, 7, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.widget2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_11, 7, 1, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(389, 10, 241, 451))
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(9, 19, 221, 131))
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 50, 31, 51))
        self.widget3 = QWidget(self.groupBox_5)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(20, 23, 151, 104))
        self.gridLayout_4 = QGridLayout(self.widget3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_13 = QLineEdit(self.widget3)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_4.addWidget(self.lineEdit_13, 1, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.widget3)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_4.addWidget(self.lineEdit_12, 0, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.widget3)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_14, 2, 1, 1, 1)

        self.label_14 = QLabel(self.widget3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_12 = QLabel(self.widget3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_13 = QLabel(self.widget3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(9, 159, 221, 141))
        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(180, 50, 31, 51))
        self.widget4 = QWidget(self.groupBox_6)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(20, 20, 151, 101))
        self.gridLayout_5 = QGridLayout(self.widget4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget4)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.widget4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_5.addWidget(self.lineEdit_15, 0, 1, 1, 1)

        self.label_16 = QLabel(self.widget4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.widget4)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_5.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.label_17 = QLabel(self.widget4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 2, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.widget4)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setReadOnly(True)

        self.gridLayout_5.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(9, 310, 221, 131))
        self.pushButton_5 = QPushButton(self.groupBox_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(180, 40, 31, 51))
        self.widget5 = QWidget(self.groupBox_7)
        self.widget5.setObjectName(u"widget5")
        self.widget5.setGeometry(QRect(20, 20, 151, 91))
        self.gridLayout_6 = QGridLayout(self.widget5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget5)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_6.addWidget(self.label_19, 1, 0, 1, 2)

        self.lineEdit_19 = QLineEdit(self.widget5)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_6.addWidget(self.lineEdit_19, 1, 2, 1, 1)

        self.label_20 = QLabel(self.widget5)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 2, 0, 1, 2)

        self.lineEdit_20 = QLineEdit(self.widget5)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setReadOnly(True)

        self.gridLayout_6.addWidget(self.lineEdit_20, 2, 2, 1, 1)

        self.lineEdit_18 = QLineEdit(self.widget5)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_6.addWidget(self.lineEdit_18, 0, 2, 1, 1)

        self.label_18 = QLabel(self.widget5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u7ebf\u5c3a\u5bf8\u8ba1\u7b97\u5de5\u5177 V2.0 By LiFazheng", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"\u77e9\u5f62\u5fae\u5e26\u5929\u7ebf\u53c2\u6570\u8ba1\u7b97", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Form", u"epsilon_r", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"H", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"lambda", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"W", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"L", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"lambda_e", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"epsilon_e", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Delta L", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"L1", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"xi_re", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u540c\u8f74\u7ebf\u8ba1\u7b97", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u60c5\u5f621\uff1ar, R -> Zo", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"->", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Zo", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"r", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"R", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u60c5\u5f622\uff1ar, Zo -> R", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"->", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"r", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Zo", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"R", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u60c5\u5f623\uff1aR, Zo -> r", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"->", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Zo", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"r", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"R", None))
    # retranslateUi

