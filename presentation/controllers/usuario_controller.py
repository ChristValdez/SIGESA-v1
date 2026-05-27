from PySide6.QtWidgets import QTableWidgetItem
from domain.use_cases.listar_usuarios_use_case import (ListarUsuariosUseCase)
from infrastructure.database.mysql_usuario_repository import (MySQLUsuarioRepository)
from domain.entities.usuario import Usuario
from domain.use_cases.crear_usuario_use_case import (CrearUsuarioUseCase)
from domain.use_cases.actualizar_usuario_use_case import (ActualizarUsuarioUseCase)
from domain.use_cases.eliminar_usuario_use_case import (EliminarUsuarioUseCase)
from domain.use_cases.listar_roles_use_case import (ListarRolesUseCase)
from domain.use_cases.listar_sedes_use_case import (ListarSedesUseCase)
from infrastructure.database.mysql_rol_repository import (MySQLRolRepository)
from infrastructure.database.mysql_sede_repository import (MySQLSedeRepository)

class UsuarioController:

    def __init__(self, view):

        self.view = view

        repository = MySQLUsuarioRepository()
        self.repository = repository
        self.listar_usuarios_use_case = (ListarUsuariosUseCase(repository))
        self.crear_usuario_use_case = (CrearUsuarioUseCase(repository))
        self.actualizar_usuario_use_case = (ActualizarUsuarioUseCase(repository))
        self.eliminar_usuario_use_case = (EliminarUsuarioUseCase(repository))
        rol_repository = MySQLRolRepository()
        sede_repository = MySQLSedeRepository()
        self.listar_roles_use_case = (ListarRolesUseCase(rol_repository))
        self.listar_sedes_use_case = ( ListarSedesUseCase(sede_repository))
        
    def cargar_usuarios(self):

        usuarios = self.listar_usuarios_use_case.execute()

        tabla = self.view.ui.table_usuarios

        tabla.setRowCount(len(usuarios))

        for row, usuario in enumerate(usuarios):

            tabla.setItem(
                row,
                0,
                QTableWidgetItem(str(usuario.id))
            )

            tabla.setItem(
                row,
                1,
                QTableWidgetItem(usuario.dni)
            )

            tabla.setItem(
                row,
                2,
                QTableWidgetItem(usuario.nombres)
            )

            tabla.setItem(
                row,
                3,
                QTableWidgetItem(usuario.apellidos)
            )

            tabla.setItem(
                row,
                4,
                QTableWidgetItem(usuario.email)
            )

            tabla.setItem(
                row,
                5,
                QTableWidgetItem(str(usuario.rol_id))
            )


    def crear_usuario(self):

        try:

            usuario = Usuario(
                id=None,
                rol_id=self.view.ui.combo_rol.currentData(),
                sede_id=self.view.ui.combo_sede.currentData(),
                dni=self.view.ui.input_dni.text(),
                nombres=self.view.ui.input_nombres.text(),
                apellidos=self.view.ui.input_apellidos.text(),
                email=self.view.ui.input_email.text(),
                password_hash=""
            )

            password = self.view.ui.input_password.text()

            self.crear_usuario_use_case.execute(
                usuario,
                password
            )

            self.view.accept()

        except Exception as e:

            self.view.ui.lbl_error.setText(str(e))
    
    def guardar_usuario(self):

        try:

            if hasattr(self.view, 'usuario') and self.view.usuario:

                self.editar_usuario()

            else:

                self.crear_usuario()

        except Exception as e:

            self.view.ui.lbl_error.setText(str(e))

    def editar_usuario(self):

        usuario = self.view.usuario

        usuario.rol_id = self.view.ui.combo_rol.currentData()

        usuario.sede_id = self.view.ui.combo_sede.currentData()

        usuario.dni = self.view.ui.input_dni.text()

        usuario.nombres = self.view.ui.input_nombres.text()

        usuario.apellidos = self.view.ui.input_apellidos.text()

        usuario.email = self.view.ui.input_email.text()

        self.actualizar_usuario_use_case.execute(
            usuario
        )

        self.view.accept()

    def obtener_usuario(self, usuario_id):

        return self.repository.buscar_por_id(
            usuario_id)
    
    def eliminar_usuario(self, usuario_id):

        self.eliminar_usuario_use_case.execute(
            usuario_id)
    
    def cargar_combos(self):

        self.view.ui.combo_rol.clear()

        roles = self.listar_roles_use_case.execute()

        for rol in roles:

            self.view.ui.combo_rol.addItem(
                rol.nombre,
                rol.id
            )

        self.view.ui.combo_sede.clear()

        sedes = self.listar_sedes_use_case.execute()

        for sede in sedes:

            self.view.ui.combo_sede.addItem(
                sede.nombre,
                sede.id
            )

        def cargar_combos(self):

            self.view.ui.combo_rol.clear()

            roles = self.listar_roles_use_case.execute()

            for rol in roles:

                self.view.ui.combo_rol.addItem(
                    rol.nombre,
                    rol.id
                )

            self.view.ui.combo_sede.clear()

            sedes = self.listar_sedes_use_case.execute()

            for sede in sedes:

                self.view.ui.combo_sede.addItem(
                    sede.nombre,
                    sede.id
                )