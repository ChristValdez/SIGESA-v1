from domain.entities.rol import Rol
from domain.ports.rol_repository import (RolRepository)
from infrastructure.database.connection import (MySQLConnection)


class MySQLRolRepository(RolRepository):

    def listar(self):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                nombre,
                descripcion
            FROM roles
            ORDER BY nombre
        """

        cursor.execute(query)

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        roles = []

        for row in results:
            roles.append(Rol(**row))

        return roles