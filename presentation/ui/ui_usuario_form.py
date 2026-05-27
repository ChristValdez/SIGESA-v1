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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 485)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(110, 80, 181, 220))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.input_dni = QLineEdit(self.formLayoutWidget)
        self.input_dni.setObjectName(u"input_dni")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_dni)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.input_nombres = QLineEdit(self.formLayoutWidget)
        self.input_nombres.setObjectName(u"input_nombres")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_nombres)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.input_apellidos = QLineEdit(self.formLayoutWidget)
        self.input_apellidos.setObjectName(u"input_apellidos")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_apellidos)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.input_email = QLineEdit(self.formLayoutWidget)
        self.input_email.setObjectName(u"input_email")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.input_email)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.input_password = QLineEdit(self.formLayoutWidget)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.input_password)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.combo_rol = QComboBox(self.formLayoutWidget)
        self.combo_rol.setObjectName(u"combo_rol")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.combo_rol)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.combo_sede = QComboBox(self.formLayoutWidget)
        self.combo_sede.setObjectName(u"combo_sede")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.combo_sede)

        self.btn_guardar = QPushButton(Dialog)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(110, 330, 81, 26))
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(200, 330, 81, 26))
        self.lbl_error = QLabel(Dialog)
        self.lbl_error.setObjectName(u"lbl_error")
        self.lbl_error.setGeometry(QRect(8, 400, 391, 20))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"DNI:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombres:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Apellidos:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Correo:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Rol:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Sede:", None))
        self.btn_guardar.setText(QCoreApplication.translate("Dialog", u"Guardar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.lbl_error.setText(QCoreApplication.translate("Dialog", u"e", None))
    # retranslateUi

