from sqlite3 import connect
from colorama import Cursor
import pyodbc

try:
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP_DELL;DATABASE=Tienda;UID=sa;PWD=123')
    print("Conexion exitosa")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Usuario")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row) 

except Exception as ex:
    print(ex)