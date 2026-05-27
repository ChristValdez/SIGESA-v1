from PySide6.QtWidgets import QMainWindow
from presentation.ui.ui_main_window import Ui_MainWindow
from presentation.views.usuarios_window import (UsuariosPage)
from application.session import Session
from PySide6.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.configurar_usuario()

        self.configurar_paginas()

        self.configurar_botones()
        self.configurar_iconos()

    def configurar_usuario(self):

        usuario = Session.usuario_actual

        self.ui.lbl_usuario.setText(
            f"{usuario.nombres}"
        )


    def configurar_paginas(self):

        self.page_usuarios = UsuariosPage()

        self.ui.stackedWidget.addWidget(
            self.page_usuarios
        )


    def configurar_botones(self):

        self.ui.btn_usuarios.clicked.connect(
            self.abrir_usuarios
        )


    def abrir_usuarios(self):

        self.ui.stackedWidget.setCurrentWidget(
            self.page_usuarios
        )

    def configurar_iconos(self):

        self.ui.btn_dashboard.setIcon(
            QIcon(":/icons/chart-column-big.svg")
        )

        self.ui.btn_usuarios.setIcon(
            QIcon(":/icons/users.svg")
        )

        self.ui.btn_logout.setIcon(
            QIcon(":/icons/log-out.svg")
        )