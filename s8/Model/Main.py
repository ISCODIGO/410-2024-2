from Cliente import Cliente
from Producto import Producto
from Tienda import Tienda
from Vendedor import Vendedor
from Loader import Loader

VENDEDOR_JSON = "vendedor.json"
CLIENTES_JSON = "clientes.json"
PRODUCTOS_JSON = "productos.json"
TIENDAS_JSON = "tienda.json"

vendedor = Loader.cargar(Vendedor, VENDEDOR_JSON)
clientes = Loader.cargar(Cliente, CLIENTES_JSON)
productos = Loader.cargar(Producto, PRODUCTOS_JSON)
tienda = Loader.cargar(Tienda, TIENDAS_JSON)

print(vendedor.__dict__)
for cliente in clientes:
    print(cliente.__dict__)
for producto in productos:
    print(producto.__dict__)
print(tienda.__dict__)
