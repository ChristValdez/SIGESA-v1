from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Usuario:
    #id: Optional[int]
    id: int
    rol_id: int
    sede_id: int
    dni: str
    nombres: str
    apellidos: str
    email: str
    password_hash: str
    numero_colegiatura: Optional[str] = None
    especialidad: Optional[str] = None
    is_active: bool = True
    ultimo_acceso: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None