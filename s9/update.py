import sqlite3
from campos import obtener_campos


conn = sqlite3.connect("asignatura.db")
cursor = conn.cursor()

id = input("ID a editar: ")
campos_disponibles = obtener_campos(cursor)[:-1]
print("Campos:")
for pos, valor in enumerate(campos_disponibles):
    print(f"[{pos}]", valor)
campo_pos = int(input("Seleccione el numero del campo: "))
valor = input("Que valor desea proveer: ")

cursor.execute(f"""
               update alumno set {campos_disponibles[campo_pos]} = ?
               where id = ?
               """, (valor, id,))
conn.commit()
cursor.close()
