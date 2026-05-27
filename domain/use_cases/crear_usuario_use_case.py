from domain.entities.usuario import Usuario
from domain.validators.usuario_validator import UsuarioValidator
from infrastructure.security.password_hasher import PasswordHasher


class CrearUsuarioUseCase:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository


    def execute(self, usuario: Usuario, password_plano: str):

        UsuarioValidator.validar_dni(usuario.dni)
        UsuarioValidator.validar_email(usuario.email)
        UsuarioValidator.validar_password(password_plano)

        usuario_existente = self.usuario_repository.buscar_por_email(
            usuario.email
        )

        if usuario_existente:
            raise ValueError(
                "Ya existe un usuario con ese correo"
            )

        dni_existente = self.usuario_repository.buscar_por_dni(
            usuario.dni
        )

        if dni_existente:
            raise ValueError(
                "Ya existe un usuario con ese DNI"
            )

        password_hash = PasswordHasher.hash_password(password_plano)

        usuario.password_hash = password_hash

        self.usuario_repository.crear(usuario)