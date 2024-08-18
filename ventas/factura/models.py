from django.db import models
from django.conf import settings


class Cliente(models.Model):
    identidad = models.CharField("Cédula", max_length=15, unique=True)
    primer_nombre = models.CharField("Primer nombre", max_length=30)
    primer_apellido = models.CharField("Primer apellido", max_length=30)
    direccion = models.TextField("Dirección")
    telefono = models.CharField("Telefono", max_length=20)
    email = models.EmailField("Email", unique=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.identidad}"

    @property
    def nombre_completo(self):
        return f"{self.primer_nombre} {self.primer_apellido}"

    class Meta:
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"


class Tienda(models.Model):
    nombre = models.CharField("Nombre de la Tienda", max_length=150)
    direccion = models.TextField("Dirección", max_length=200)
    telefono = models.CharField("Telefono", max_length=15)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tiendas"
        verbose_name = "Tienda"


class Vendedor(models.Model):
    nombre = models.CharField("Nombre del Vendedor", max_length=100)
    tienda = models.ForeignKey(
        Tienda, on_delete=models.CASCADE
    )  # Relación uno a muchos (muchos vendedores a una tienda)
    email = models.EmailField("Email", unique=True)
    activo = models.BooleanField("Activo", default=True)

    def __str__(self):
        return self.nombre


class TipoProducto(models.Model):
    codigo = models.CharField("Código del Tipo", max_length=10, unique=True)
    nombre = models.CharField("Nombre del Tipo", max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField("Nombre del producto", max_length=100)
    descripcion = models.TextField("Descripción del Producto")
    precio = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField("Existencia")
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    gravable = models.BooleanField("Se grava ISV", default=True)
    activo = models.BooleanField("Activo", default=True)
    tipo = models.ForeignKey(TipoProducto, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} - {self.tienda.nombre}"

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"


class Orden(models.Model):
    PENDIENTE = 1
    PAGADO = 2
    ENTREGADO = 3
    CANCELADO = 4
    REVERSADO = 5
    ESTADO_CHOICES = (
        (PENDIENTE, "Pendiente"),
        (PAGADO, "Pagado"),
        (ENTREGADO, "Entregado"),
        (CANCELADO, "Cancelado"),
        (REVERSADO, "Reversado"),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.PROTECT)
    fecha_creacion = models.DateTimeField(
        "Fecha creacion de la orden", auto_now_add=True
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, editable=False
    )
    estado = models.PositiveSmallIntegerField(
        "Estado",
        choices=ESTADO_CHOICES,
        default=PENDIENTE,
    )

    def __str__(self):
        return f"Orden {self.id} - {self.cliente.nombre_completo}"

    def save(self, *args, **kwargs):
        if not self.id:  # Si no existe la orden
            self.total = sum([detalle.subtotal for detalle in self.detalles.all()])
        super().save(*args, **kwargs)


class OrdenDetalle(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField("Cantidad")
    precio_unitario = models.DecimalField(
        "Precio Unitario", max_digits=10, decimal_places=2
    )

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    @property
    def subtotal_isv(self):
        return self.subtotal * (1 + settings.ISV / 100.0)
