
class Cliente:
    def __init__(self, nombre, direccion, telefonos, identidad):
        self.nombre = nombre
        self.direccion = direccion
        self.telefonos = telefonos
        self.identidad = identidad

    def __str__(self):
        return f"{self.nombre}"

cliente = Cliente(direccion="Col. Buenos Aires", telefonos=["9900-1234"], nombre="Luis Ramirez", identidad="08329432")
print(cliente.__dict__)


datos = {
    "nombre": "Juan Perez",
    "direccion": "Col. San Miguel",
    "telefonos": "",
    "identidad": '2309248952',
}


cliente2 = Cliente(**datos)
print(cliente2.__dict__)


