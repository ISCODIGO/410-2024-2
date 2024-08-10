import sqlite3

cuenta = input("Cuenta:")
primer_nombre = input("Primer nombre:")
primer_apellido = input("Primer apellido:")
carrera = input("carrera:")

conn = sqlite3.connect("asignatura.db")
cursor = conn.cursor()

cursor.execute("""
    insert into alumno(cuenta, primer_nombre, primer_apellido, carrera)
    values(?, ?, ?, ?)
    """, (cuenta, primer_nombre, primer_apellido, carrera))

conn.commit()

cursor.close()
