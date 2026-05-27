from domain.entities.usuario import Usuario
from domain.ports.usuario_repository import UsuarioRepository
from infrastructure.database.connection import MySQLConnection


class MySQLUsuarioRepository(UsuarioRepository):

    def crear(self, usuario: Usuario):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor()

        query = """
            INSERT INTO usuarios (
                rol_id,
                sede_id,
                dni,
                nombres,
                apellidos,
                email,
                password_hash,
                numero_colegiatura,
                especialidad
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            usuario.rol_id,
            usuario.sede_id,
            usuario.dni,
            usuario.nombres,
            usuario.apellidos,
            usuario.email,
            usuario.password_hash,
            usuario.numero_colegiatura,
            usuario.especialidad
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()


    def buscar_por_email(self, email: str):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM usuarios
            WHERE email = %s
            AND deleted_at IS NULL
        """

        cursor.execute(query, (email,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if not result:
            return None

        return Usuario(**result)


    def buscar_por_dni(self, dni: str):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM usuarios
            WHERE dni = %s
            AND deleted_at IS NULL
        """

        cursor.execute(query, (dni,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if not result:
            return None

        return Usuario(**result)
    
    def login(self, email: str):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM usuarios
            WHERE email = %s
            AND is_active = TRUE
            AND deleted_at IS NULL
        """

        cursor.execute(query, (email,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if not result:
            return None

        return Usuario(**result)
        
    def listar(self):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM usuarios
            WHERE deleted_at IS NULL
            ORDER BY id DESC
        """

        cursor.execute(query)

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        usuarios = []

        for row in results:
            usuarios.append(Usuario(**row))

        return usuarios

    def actualizar(self, usuario: Usuario):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor()

        query = """
            UPDATE usuarios
            SET
                rol_id = %s,
                sede_id = %s,
                dni = %s,
                nombres = %s,
                apellidos = %s,
                email = %s,
                numero_colegiatura = %s,
                especialidad = %s,
                updated_at = NOW()
            WHERE id = %s
        """

        values = (
            usuario.rol_id,
            usuario.sede_id,
            usuario.dni,
            usuario.nombres,
            usuario.apellidos,
            usuario.email,
            usuario.numero_colegiatura,
            usuario.especialidad,
            usuario.id
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def buscar_por_id(self, usuario_id: int):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM usuarios
            WHERE id = %s
            AND deleted_at IS NULL
        """

        cursor.execute(query, (usuario_id,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if not result:
            return None

        return Usuario(**result)
    
    def eliminar(self, usuario_id: int):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor()

        query = """
            UPDATE usuarios
            SET deleted_at = NOW()
            WHERE id = %s
        """

        cursor.execute(query, (usuario_id,))

        connection.commit()

        cursor.close()
        connection.close()