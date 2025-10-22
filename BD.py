import sqlite3 as sql

def crear_BD():
        conexion = sql.connect("CalzaIsoft.db")
        conexion.commit()
        conexion.close()


def Conex():
        conexion = sql.connect("CalzaIsoft.db")
        conexion.execute("PRAGMA foreign_keys = ON;")
        return conexion


def Iniciar_Cursor():
        conexion = Conex()
        cursor = conexion.cursor()
        return conexion,cursor

def crear_Tabla():
        conexion,cursor = Iniciar_Cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS Empleados (
        ID TEXT PRIMARY KEY,
        Nombre TEXT,
        ap_Paterno TEXT,
        ap_Materno TEXT,
        Telefono Text,
        Direccion TEXT,
        Antigüedad TEXT,
        Rol TEXT,
        Contra text
        )  
        """)
        conexion.commit()
        conexion.close()

def Eliminar_tabla(Tabla):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"DROP TABLE {Tabla}")
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


def Agregar_Administrador(usuario,contra,id):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"SELECT Id FROM Empleados WHERE Id = '{id}'")
        fila = cursor.fetchone()
        if fila is None:
                print("El empleado no existe")
        else:
                cursor.execute(f"INSERT INTO Administradores VALUES ('{usuario}','{contra}','{id}')")
                cursor.execute(f"UPDATE Empleados SET Rol = 'Administrador' WHERE id = '{id}'")
        conexion.commit()
        conexion.close()

def Eliminar_Administrador(usuario,rol):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"SELECT Id_Empleado FROM Administradores WHERE Usuario = '{usuario}'")
        fila = cursor.fetchone()
        id = fila[0]
        cursor.execute(f"UPDATE Empleados SET Rol = '{rol}' WHERE Id = '{id}'")
        cursor.execute(f"DELETE FROM Administradores WHERE Usuario = '{usuario}' ")
        conexion.commit()
        conexion.close()

def Actualizar_contra(Usuario,contra):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"""
        UPDATE Administradores
        SET Contra = '{contra}'
        WHERE Usuario = '{Usuario}'""")
        conexion.commit()
        conexion.close()

def Agregar_Empleado(id,nombre,ap_paterno,ap_materno,telefono,direccion,anti,rol,contra):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"INSERT INTO Empleados VALUES('{id}','{nombre}','{ap_paterno}','{ap_materno}','{telefono}','{direccion}','{anti}','{rol}','{contra}')")
        conexion.commit()
        conexion.close()

def Eliminar_Empleado(id):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"SELECT Rol FROM Empleados WHERE Id = '{id}'")
        fila = cursor.fetchone()
        rol = fila[0]
        cursor.execute(f"DELETE FROM Empleados WHERE Id = '{id}'")
        conexion.commit()
        if rol == "Administrador":
                cursor.execute(f"DELETE FROM Administradores WHERE Id_Empleado = '{id}'")
                conexion.commit()
        conexion.close()

def comparar_contra(usuario,contra):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"SELECT contra from Empleados WHERE Nombre = '{usuario}'")
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
                return False
        return contra == fila[0]

def comparar_Admin(usuario,contra):
        conexion,cursor = Iniciar_Cursor()
        cursor.execute(f"SELECT contra from Administradores WHERE Usuario = '{usuario}'")
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
                return False
        return contra == fila[0]