ISV = 0.15


class Producto:
    def __init__(self, codigo: str, precio: float, descripcion: str, es_gravado: bool):
        self.__precio = precio
        self.codigo = codigo
        self.descripcion = descripcion
        self.es_gravado = es_gravado

    def get_precio(self):
        return round(self.__precio, 2)

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("No es posible un precio negativo")
        self.__precio = precio

    @property
    def precio(self):
        return round(self.__precio, 2)

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("No es posible un precio negativo")
        self.__precio = precio

    def calcular_precio(self):
        return self.__precio * (1 + ISV)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"


product = Producto("0001", 130, "Mouse", True)

print(product.get_precio())
print(product.__dict__)

product2 = Producto("0002", 700.565464, "Teclado", True)
print(product2.__dict__)
print(product2.precio)
