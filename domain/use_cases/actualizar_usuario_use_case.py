from domain.validators.usuario_validator import (
    UsuarioValidator
)


class ActualizarUsuarioUseCase:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository


    def execute(self, usuario):

        UsuarioValidator.validar_dni(usuario.dni)

        UsuarioValidator.validar_email(usuario.email)

        self.usuario_repository.actualizar(usuario)