
#-----------------------------------------------------------------------------
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)
#-----------------------------------------------------------
from domain.use_cases.login_use_case import LoginUseCase
from infrastructure.database.mysql_usuario_repository import (
    MySQLUsuarioRepository
)

repository = MySQLUsuarioRepository()

login_use_case = LoginUseCase(repository)

try:

    usuario = login_use_case.execute(
        "juan@example.com",
        "12345678"
    )

    print("Login exitoso")
    print(usuario)

except Exception as e:
    print(e)