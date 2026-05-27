import sys
import presentation.resources.resources_rc
from PySide6.QtWidgets import QApplication

from presentation.views.login_window import LoginWindow


app = QApplication(sys.argv)

with open(
    "presentation/styles/style.qss",
    "r"
) as file:

    app.setStyleSheet(file.read())

window = LoginWindow()
window = LoginWindow()

window.show()

sys.exit(app.exec())

#EJECUTAR AQUI