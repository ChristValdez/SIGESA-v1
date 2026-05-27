from abc import ABC, abstractmethod


class SedeRepository(ABC):

    @abstractmethod
    def listar(self):
        pass