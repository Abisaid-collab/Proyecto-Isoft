import sqlite3 as sql

def crear_BD():
        conexion = sql.Connection("CalzaIsoft.db")
        conexion.commit()
        conexion.close()

def crear_Tabla():
        conexion = sql.Connection("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(
        """ CREATE TABLE Administradores  (
                Usuario text PRIMARY KEY,
                Contra text
                    )""")
        conexion.commit()
        conexion.close()

def alterar():
        conexion = sql.Connection("CalzaIsoft.db")
        cursor = conexion.cursor()
        conexion.commit()
        conexion.close()

crear_Tabla()
