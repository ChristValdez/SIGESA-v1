from PySide6.QtWidgets import QMainWindow
from presentation.ui.ui_login import Ui_MainWindow
from presentation.controllers.auth_controller import AuthController
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QLineEdit

class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configurar_password_toggle()

        self.auth_controller = AuthController(self)

        self.ui.btn_login.clicked.connect(
            self.auth_controller.login
        )

    def configurar_password_toggle(self):

        self.password_visible = False

        self.toggle_password_action = QAction(self)

        self.toggle_password_action.setIcon(
            QIcon(":/icons/eye.svg")
        )

        self.ui.input_password.addAction(
            self.toggle_password_action,
            QLineEdit.TrailingPosition
        )

        self.toggle_password_action.triggered.connect(
            self.toggle_password_visibility
        )

    def toggle_password_visibility(self):

        if self.password_visible:

            self.ui.input_password.setEchoMode(
                QLineEdit.Password
            )

            self.toggle_password_action.setIcon(
                QIcon(":/icons/eye.svg")
            )

            self.password_visible = False

        else:

            self.ui.input_password.setEchoMode(
                QLineEdit.Normal
            )

            self.toggle_password_action.setIcon(
                QIcon(":/icons/eye-off.svg")
            )

            self.password_visible = True