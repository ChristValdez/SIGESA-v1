from PySide6.QtWidgets import QDialog
from presentation.ui.ui_usuario_form import Ui_Dialog
from presentation.controllers.usuario_controller import (UsuarioController)


class UsuarioFormDialog(QDialog):
    def __init__(self, usuario=None, parent=None):
        super().__init__(parent)

        self.usuario = usuario
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.controller = UsuarioController(self)
        self.ui.btn_guardar.clicked.connect(self.controller.guardar_usuario)
        self.ui.btn_cancelar.clicked.connect(self.close)
        self.controller.cargar_combos()
        if self.usuario:
            self.cargar_datos()


 
    def cargar_datos(self):

        self.ui.input_dni.setText(
            self.usuario.dni
        )

        self.ui.input_nombres.setText(
            self.usuario.nombres
        )

        self.ui.input_apellidos.setText(
            self.usuario.apellidos
        )

        self.ui.input_email.setText(
            self.usuario.email
        )

        self.ui.combo_rol.setCurrentIndex(0)

        self.ui.combo_sede.setCurrentIndex(0)
    
