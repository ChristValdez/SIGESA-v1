from domain.entities.sede import Sede

from domain.ports.sede_repository import (
    SedeRepository
)

from infrastructure.database.connection import (
    MySQLConnection
)


class MySQLSedeRepository(SedeRepository):

    def listar(self):

        connection = MySQLConnection.get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                nombre,
                direccion,
                telefono
            FROM sedes
            WHERE is_active = 1
            ORDER BY nombre
        """

        cursor.execute(query)

        results = cursor.fetchall()

        cursor.close()
        connection.close()

        sedes = []

        for row in results:
            sedes.append(Sede(**row))

        return sedes