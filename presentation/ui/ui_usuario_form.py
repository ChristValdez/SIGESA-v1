# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuario_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(358, 587)
        self.btn_guardar = QPushButton(Dialog)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(20, 530, 100, 40))
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(240, 530, 100, 40))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 50, 341, 433))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.input_dni = QLineEdit(self.widget)
        self.input_dni.setObjectName(u"input_dni")
        font = QFont()
        font.setPointSize(12)
        self.input_dni.setFont(font)

        self.verticalLayout.addWidget(self.input_dni)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.input_nombres = QLineEdit(self.widget)
        self.input_nombres.setObjectName(u"input_nombres")
        self.input_nombres.setFont(font)

        self.verticalLayout.addWidget(self.input_nombres)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.input_apellidos = QLineEdit(self.widget)
        self.input_apellidos.setObjectName(u"input_apellidos")
        self.input_apellidos.setFont(font)

        self.verticalLayout.addWidget(self.input_apellidos)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.input_email = QLineEdit(self.widget)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setFont(font)

        self.verticalLayout.addWidget(self.input_email)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.input_password = QLineEdit(self.widget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setFont(font)
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.input_password)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.combo_rol = QComboBox(self.widget)
        self.combo_rol.setObjectName(u"combo_rol")
        self.combo_rol.setFont(font)

        self.verticalLayout.addWidget(self.combo_rol)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.lbl_error = QLabel(self.widget)
        self.lbl_error.setObjectName(u"lbl_error")

        self.verticalLayout.addWidget(self.lbl_error)

        self.combo_sede = QComboBox(self.widget)
        self.combo_sede.setObjectName(u"combo_sede")
        self.combo_sede.setFont(font)

        self.verticalLayout.addWidget(self.combo_sede)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"DNI:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombres:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Apellidos:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Correo:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Rol:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Sede:", None))
        self.lbl_error.setText("")
    # retranslateUi

