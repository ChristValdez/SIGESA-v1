class EliminarUsuarioUseCase:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository


    def execute(self, usuario_id):

        self.usuario_repository.eliminar(
            usuario_id
        )