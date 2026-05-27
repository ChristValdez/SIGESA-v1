from abc import ABC, abstractmethod


class RolRepository(ABC):

    @abstractmethod
    def listar(self):
        pass