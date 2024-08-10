import sqlite3


conn = sqlite3.connect("asignatura.db")
cursor = conn.cursor()

id = input("ID a eliminar: ")

cursor.execute("delete from alumno where id = ?", (id,))
conn.commit()
cursor.close()
