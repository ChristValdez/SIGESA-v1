import mysql.connector
from config.database import DatabaseConfig


class MySQLConnection:

    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=DatabaseConfig.HOST,
            port=DatabaseConfig.PORT,
            user=DatabaseConfig.USER,
            password=DatabaseConfig.PASSWORD,
            database=DatabaseConfig.DATABASE
        )