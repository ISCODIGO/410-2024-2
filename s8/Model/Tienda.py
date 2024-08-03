class Tienda:
    def __init__(self, direccion: str, nombre: str, telefonos: list):
        self.direccion = direccion
        self.nombre = nombre
        self.telefonos = "/".join(telefonos)

    def __str__(self):
        return f"{self.nombre}"