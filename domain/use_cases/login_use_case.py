from infrastructure.security.password_hasher import PasswordHasher
from application.session import Session

class LoginUseCase:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository


    def execute(self, email: str, password: str):

        usuario = self.usuario_repository.login(email)

        if not usuario:
            raise ValueError(
                "Credenciales incorrectas"
            )

        password_correcto = PasswordHasher.verify_password(
            password,
            usuario.password_hash
        )

        if not password_correcto:
            raise ValueError(
                "Credenciales incorrectas"
            )
        
        Session.usuario_actual = usuario

        return usuario