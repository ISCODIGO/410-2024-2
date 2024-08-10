import sqlite3
from pprint import pprint

conn = sqlite3.connect("asignatura.db")
cursor = conn.cursor()

cursor.execute("select * from alumno")
# fone = cursor.fetchone()
# print("Fetch one:", fone)

# fmany = cursor.fetchmany(3)
# print("Fetch many:", fmany)

campos = [description[0] for description in cursor.description]  # list
data = cursor.fetchall()  # list of tuples

tabla = []
for registro in data:
    d = dict(zip(campos, registro))
    tabla.append(d)

pprint(tabla)
