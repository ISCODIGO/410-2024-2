import sqlite3


conn = sqlite3.connect("asignatura.db")
cursor = conn.cursor()

# create
cursor.execute(
    """
    insert into alumno(cuenta, primer_nombre, primer_apellido, carrera)
    values('1244', 'Jose', 'Valladares', 'Medicina')
    """)

# cursor.execute("select * from alumno")
# dato = cursor.fetchone()
# print(dato)

conn.commit()

cursor.close()
