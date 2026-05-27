from PySide6.QtWidgets import QWidget, QTableWidgetItem
#from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from presentation.ui.ui_usuarios import Ui_Form
from presentation.controllers.usuario_controller import (UsuarioController)
from presentation.views.usuario_form_dialog import (UsuarioFormDialog)
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMenu)
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QAbstractItemView,QHeaderView)

class UsuariosPage(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.configurar_tabla()

        self.controller = UsuarioController(self)

        self.controller.cargar_usuarios()
        #self.ui.btn_editar.clicked.connect(self.editar_usuario)
        self.ui.btn_refrescar.clicked.connect(self.controller.cargar_usuarios)
        self.ui.btn_nuevo.clicked.connect(self.abrir_formulario)
        #self.ui.btn_eliminar.clicked.connect(self.eliminar_usuario)


    def abrir_formulario(self):

        #dialog = UsuarioFormDialog(self)
        dialog = UsuarioFormDialog(parent=self)
        resultado = dialog.exec()

        if resultado:
            self.controller.cargar_usuarios()
    

    def editar_usuario(self):
        fila = self.ui.table_usuarios.currentRow()
        if fila < 0:
            return
        usuario_id = int(
            self.ui.table_usuarios.item(fila, 0).text()
        )
        usuario = self.controller.obtener_usuario(
            usuario_id
        )
        dialog = UsuarioFormDialog(
            usuario,
            self
        )
        resultado = dialog.exec()
        if resultado:
            self.controller.cargar_usuarios()

    def eliminar_usuario(self):

        fila = self.ui.table_usuarios.currentRow()

        if fila < 0:
            return

        usuario_id = int(
            self.ui.table_usuarios.item(fila, 0).text()
        )

        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea eliminar este usuario?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:

            self.controller.eliminar_usuario(
                usuario_id
            )

            self.controller.cargar_usuarios()
    
    def configurar_tabla(self):

        tabla = self.ui.table_usuarios
        tabla.setShowGrid(False)
        tabla.verticalHeader().setVisible(False)

        # Seleccionar fila completa
        tabla.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        # Solo una fila
        tabla.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        # No editable
        tabla.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )

        # Alternar colores
        tabla.setAlternatingRowColors(True)

        # Ocultar ID
        tabla.setColumnHidden(0, True)

        # Ajustar columnas
        tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # Menú contextual
        tabla.setContextMenuPolicy(
            Qt.CustomContextMenu
        )

        tabla.customContextMenuRequested.connect(
            self.mostrar_menu_contextual
        )

    def mostrar_menu_contextual(self, position):

        fila = self.ui.table_usuarios.currentRow()

        if fila < 0:
            return

        menu = QMenu()

        action_editar = QAction("Editar", self)

        action_eliminar = QAction("Eliminar", self)

        menu.addAction(action_editar)

        menu.addAction(action_eliminar)

        action_editar.triggered.connect(
            self.editar_usuario
        )

        action_eliminar.triggered.connect(
            self.eliminar_usuario
        )

        menu.exec(
            self.ui.table_usuarios.viewport().mapToGlobal(position)
        )