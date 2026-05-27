from dataclasses import dataclass


@dataclass
class Sede:
    id: int
    nombre: str
    direccion: str = None
    telefono: str = None