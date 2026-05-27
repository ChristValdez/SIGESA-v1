#-----------------------------------------------------------------------------
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)
#-----------------------------------------------------------------------------

from domain.entities.usuario import Usuario
from domain.use_cases.crear_usuario_use_case import CrearUsuarioUseCase
from infrastructure.database.mysql_usuario_repository import (
    MySQLUsuarioRepository
)

usuario = Usuario(
    id=None,
    rol_id=1,
    sede_id=1,
    dni="12345678",
    nombres="Juan",
    apellidos="Pérez",
    email="juan@example.com",
    password_hash=""
)

repository = MySQLUsuarioRepository()

use_case = CrearUsuarioUseCase(repository)

use_case.execute(usuario, "12345678")

print("Usuario creado correctamente")