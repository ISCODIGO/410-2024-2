from django.contrib import admin

# Register your models here.
from factura.models import Cliente, Producto, Tienda, TipoProducto, Vendedor


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ["primer_nombre", "primer_apellido"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ["tipo"]


@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    pass


@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "direccion")
