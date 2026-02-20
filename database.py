import sqlite3
from sqlite3 import Error
from notificaciones import mensaje_exito,mensaje_error

def conectar_db():
    try:
        #creo la conexion y la abse de datos 
        conexion=sqlite3.connect('agenda.db')
        #retorno la conexion
        return conexion
    except Error as e:
        print(f"error en la conexion de DB {e}")
        return None

def crear_tabla():
        sentencia_sql = """
    CREATE TABLE IF NOT EXISTS contactos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    cedula TEXT UNIQUE NOT NULL,
    direccion TEXT NOT NULL,
    pais TEXT NOT NULL,  -- <--- Agregamos este
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
        conexion= conectar_db()

        if conexion:
            try:
                cursor= conexion.cursor()
                cursor.execute(sentencia_sql)
                conexion.commit()
                print("Tabla creada con exito ")
            except Error as e:
                print(f"❌ Error al crear la tabla: {e}")
            finally:
                conexion.close()


#funcion para agg contactos a la tabla
def insertar_contacto(nombre, apellido, cedula, direccion, pais): # <--- Mira el nombre
    conexion = conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            query = "INSERT INTO contactos (nombre, apellido, cedula, direccion, pais) VALUES (?, ?, ?, ?, ?)"
            valores = (nombre, apellido, cedula, direccion, pais)
            cursor.execute(query, valores)
            conexion.commit()
            mensaje_exito("Operacion Realizada con Exito","Contacto Guardado Satisfactoriamente")
        except Exception as e:
            mensaje_error("Algo salio Mal","Error al Guardar el Contacto...")
        finally:
            conexion.close()

#obtenemos todos los contactos
def obtener_contactos():
    conexion = conectar_db()
    contactos = []
    if conexion:
        try:
            cursor = conexion.cursor()
            # Seleccionamos todo de la tabla
            cursor.execute("SELECT nombre, apellido, cedula, direccion, pais FROM contactos")
            contactos = cursor.fetchall() # Esto trae todos los registros en una lista
        except Exception as e:
            print(f"❌ Error al consultar: {e}")
        finally:
            conexion.close()
    return contactos




#borrar contacto por cedula
def borrar_Contacto_Por_Cedula(cedula):
    conexion= conectar_db()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM contactos WHERE cedula = ?", (cedula,))
            conexion.commit()

            if cursor.rowcount > 0:
                mensaje_exito("Operacion exitosa","Contacto borrado exitosamente") #notificaciones 
            else:
                print("No se encontró ningún contacto con esa cédula.")

        except Exception as e:
            print(f"Error al intentar borrar: {e}")
        finally:
            conexion.close()


if __name__ == '__main__':
    crear_tabla()