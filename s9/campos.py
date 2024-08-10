def obtener_campos(cursor):
    cursor.execute("select * from alumno")
    return [description[0] for description in cursor.description]
