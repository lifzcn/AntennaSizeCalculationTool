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
        Form.resize(380, 420)
        Form.setMaximumSize(QSize(380, 480))
        Form.setSizeIncrement(QSize(380, 480))
        self.groupBox_1 = QGroupBox(Form)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setGeometry(QRect(10, 10, 361, 141))
        self.pushButton_1 = QPushButton(self.groupBox_1)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(260, 60, 75, 31))
        self.layoutWidget = QWidget(self.groupBox_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 32, 221, 91))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 160, 361, 251))
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 341, 221))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_7, 4, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_8, 5, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5929\u7ebf\u5c3a\u5bf8\u8ba1\u7b97\u5de5\u5177 V1.0 By LiFazheng", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u4ecb\u8d28\u7684\u4ecb\u7535\u5e38\u6570\uff1aepsilon_r", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5de5\u4f5c\u9891\u7387\uff1af", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u4ecb\u8d28\u57fa\u7247\u539a\u5ea6\uff1aH", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f90\u5c04\u8d34\u7247\u7684\u5bbd\u5ea6\uff1aW", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f90\u5c04\u5355\u5143\u957f\u5ea6\uff1aL", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4ecb\u8d28\u5185\u7684\u5bfc\u6ce2\u6ce2\u957f\uff1alambda_e", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6709\u6548\u4ecb\u7535\u5e38\u6570\uff1aepsilon_e", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u7b49\u6548\u8f90\u5c04\u7f1d\u9699\u5bbd\u5ea6\uff1aDelta_L", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u963b\u6297\u4e3a50\u03a9\u65f6\u7684\u9988\u7535\u70b9\u4f4d\u7f6e\uff1aL1", None))
    # retranslateUi

