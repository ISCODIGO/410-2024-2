ISV = 0.15


class Producto:
    def __init__(self, codigo: str, precio: float, descripcion: str, es_gravado: bool):
        self.precio = precio
        self.codigo = codigo
        self.descripcion = descripcion
        self.es_gravado = es_gravado

    def calcular_precio(self):
        return self.precio * (1 + ISV)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"
