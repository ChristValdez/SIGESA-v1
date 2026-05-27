from abc import ABC, abstractmethod
from domain.entities.usuario import Usuario

#Para que nuestra lógica de negocio funcione, necesitamos que alguien se encargue de 
# crear, buscar y autenticar usuarios, pero no nos importa el cómo"
#estos se heredan en los repositorios una db especifica

class UsuarioRepository(ABC):

    @abstractmethod
    def crear(self, usuario: Usuario):
        pass

    @abstractmethod
    def buscar_por_email(self, email: str):
        pass

    @abstractmethod
    def buscar_por_dni(self, dni: str):
        pass

    @abstractmethod
    def login(self, email: str):
        pass

    @abstractmethod
    def listar(self):
        pass
    @abstractmethod
    def actualizar(self, usuario: Usuario):
        pass
        
    @abstractmethod
    def buscar_por_id(self, usuario_id: int):
        pass

    @abstractmethod
    def eliminar(self, usuario_id: int):
        pass