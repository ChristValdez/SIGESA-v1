from dataclasses import dataclass


@dataclass
class Rol:
    id: int
    nombre: str
    descripcion: str = None