import re


class UsuarioValidator:

    @staticmethod
    def validar_dni(dni: str):

        if not dni.isdigit():
            raise ValueError("El DNI solo debe contener números")

        if len(dni) != 8:
            raise ValueError("El DNI debe tener 8 dígitos")


    @staticmethod
    def validar_email(email: str):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, email):
            raise ValueError("Correo electrónico inválido")


    @staticmethod
    def validar_password(password: str):

        if len(password) < 8:
            raise ValueError(
                "La contraseña debe tener al menos 8 caracteres"
            )