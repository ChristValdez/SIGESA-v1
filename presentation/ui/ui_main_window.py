# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 800)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar = QFrame(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setGeometry(QRect(9, 20, 220, 711))
        self.sidebar.setStyleSheet(u"Qwidget{\n"
"	background-color:  rgb(31,149,239);\n"
"}")
        self.sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.line = QFrame(self.sidebar)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 80, 118, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_usuario = QLabel(self.sidebar)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(10, 650, 200, 40))
        self.btn_logout = QPushButton(self.sidebar)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(10, 600, 200, 40))
        font = QFont()
        font.setPointSize(9)
        self.btn_logout.setFont(font)
        self.btn_usuarios = QPushButton(self.sidebar)
        self.btn_usuarios.setObjectName(u"btn_usuarios")
        self.btn_usuarios.setGeometry(QRect(10, 150, 200, 40))
        self.btn_usuarios.setFont(font)
        self.btn_pacientes = QPushButton(self.sidebar)
        self.btn_pacientes.setObjectName(u"btn_pacientes")
        self.btn_pacientes.setGeometry(QRect(10, 200, 200, 40))
        self.btn_pacientes.setFont(font)
        self.btn_dashboard = QPushButton(self.sidebar)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setGeometry(QRect(10, 100, 200, 40))
        self.btn_dashboard.setFont(font)
        self.btn_citas = QPushButton(self.sidebar)
        self.btn_citas.setObjectName(u"btn_citas")
        self.btn_citas.setGeometry(QRect(10, 250, 200, 40))
        self.btn_citas.setFont(font)
        self.lbl_logo = QLabel(self.sidebar)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setGeometry(QRect(70, 30, 65, 26))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lbl_logo.setFont(font1)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 20, 800, 600))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.btn_usuarios.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.btn_pacientes.setText(QCoreApplication.translate("MainWindow", u"Pacientes", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btn_citas.setText(QCoreApplication.translate("MainWindow", u"Citas", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"SIGESA", None))
    # retranslateUi

