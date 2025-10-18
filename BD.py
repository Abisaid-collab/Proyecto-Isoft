import sqlite3 as sql

def crear_BD():
        conexion = sql.connect("CalzaIsoft.db")
        conexion.commit()
        conexion.close()

def crear_Tabla():
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(
        """ CREATE TABLE Administradores  (
                Usuario text PRIMARY KEY,
                Contra text
                    )""")
        conexion.commit()
        conexion.close()

def alterar():
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        conexion.commit()
        conexion.close()

def agregar_nuevo_zapato(tabla,id,sexo,talla,color,material,tipo,precio,stock):
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO {tabla} VALUES ('{id}','{sexo}',{talla},'{color}','{material}','{tipo}',{precio},{stock})")
        conexion.commit()
        conexion.close()

def mostrar_datos(Tabla):
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(f"Select * from {Tabla}")
        filas = cursor.fetchall()

        for filas in filas:
                print(filas)
        
        conexion.close()

def Eliminar_Zapato(Tabla,Id):
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM {Tabla} WHERE Id_Producto = '{Id}'")
        conexion.commit()
        conexion.close()

def Agregar_Stock(Tabla,agregado,id):
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(f"""
        UPDATE {Tabla}
        SET Stock = Stock + {agregado}
        WHERE Id_Producto = '{id}'
        """)
        conexion.commit()
        conexion.close()

def Eliminar_Stock(Tabla,eliminado,id):
        conexion = sql.connect("CalzaIsoft.db")
        cursor = conexion.cursor()
        cursor.execute(f"""
        UPDATE {Tabla}
        SET Stock = Stock - {eliminado}
        WHERE Id_Producto = '{id}'
        """)
        conexion.commit()
        conexion.close()





