from domain.use_cases.login_use_case import LoginUseCase
from presentation.views.main_window import MainWindow
from infrastructure.database.mysql_usuario_repository import (
    MySQLUsuarioRepository
)
from presentation.views.main_window import (
    MainWindow
)

class AuthController:

    def __init__(self, view):

        self.view = view

        repository = MySQLUsuarioRepository()

        self.login_use_case = LoginUseCase(repository)


    def login(self):

        email = self.view.ui.input_email.text()

        password = self.view.ui.input_password.text()

        try:

            usuario = self.login_use_case.execute(
                email,
                password
            )

            self.main = MainWindow()
            self.main.show()
            self.view.close()

            self.view.ui.lbl_error.setText(
                f"Bienvenido {usuario.nombres}"
            )

        except Exception as e:

            self.view.ui.lbl_error.setText(str(e))