from enum import Enum


class MetodoPago(Enum):
    EFECTIVO = 1
    TARJETA_CREDITO = 2
    TARJETA_DEBITO = 3
    CHEQUE = 4
    OTRO = 5


class TipoCliente(Enum):
    RTN = 1
    CONTADO = 2


class Factura:
    def __init__(self, tipo_cliente, vendedor, metodo_pago):
        self.identificador = None
        self.tipo_cliente = tipo_cliente
        self.vendedor = vendedor
        self.metodo_pago = metodo_pago
        self.productos = []
        self.total = 0
        self.cliente = None

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        if total < 0:
            raise ValueError("El total no puede ser negativo")
        self._total = total

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.calcular_precio()

    def remover_producto(self, producto):
        self.productos.remove(producto)
        self.total -= producto.calcular_precio()

    def imprimir_factura(self):
        return f"""
        Factura: {self.identificador}
        Vendedor: {self.vendedor}
        Cliente: {self.cliente}
        Metodo de Pago: {self.metodo_pago}
        Total: {self.total}
        -------------------------------------
        Productos:
        {self.productos}
        -------------------------------------
        """

    def __str__(self) -> str:
        return f"{self.identificador}"
