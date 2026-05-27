# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuarios.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.btn_refrescar = QPushButton(Form)
        self.btn_refrescar.setObjectName(u"btn_refrescar")
        self.btn_refrescar.setGeometry(QRect(10, 50, 81, 26))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 90, 781, 501))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_nuevo = QPushButton(self.frame)
        self.btn_nuevo.setObjectName(u"btn_nuevo")
        self.btn_nuevo.setGeometry(QRect(670, 460, 100, 40))
        self.table_usuarios = QTableWidget(self.frame)
        if (self.table_usuarios.columnCount() < 6):
            self.table_usuarios.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_usuarios.setObjectName(u"table_usuarios")
        self.table_usuarios.setGeometry(QRect(0, 20, 771, 431))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_refrescar.setText(QCoreApplication.translate("Form", u"A", None))
        self.btn_nuevo.setText(QCoreApplication.translate("Form", u"Nuevo", None))
        ___qtablewidgetitem = self.table_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem1 = self.table_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DNI", None))
        ___qtablewidgetitem2 = self.table_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Apellidos", None))
        ___qtablewidgetitem3 = self.table_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Nombres", None))
        ___qtablewidgetitem4 = self.table_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Correo", None))
        ___qtablewidgetitem5 = self.table_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Rol", None))
    # retranslateUi

