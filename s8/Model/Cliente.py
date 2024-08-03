
class Cliente:
    def __init__(self, nombre, direccion, telefonos, identidad):
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = telefonos
        self.identidad = identidad

    def __str__(self):
        return f"{self.nombre}"
