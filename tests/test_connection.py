
#-----------------------------------------------------------------------------
import os
import sys
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root_path not in sys.path:
    sys.path.append(root_path)
#-----------------------------------------------------------------------------

from infrastructure.database.connection import MySQLConnection

connection = MySQLConnection.get_connection()

if connection.is_connected():
    print("Conexión exitosa")
else:
    print("Error")