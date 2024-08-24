from rest_framework import serializers
from factura.models import (
    Cliente,
    Producto,
    TipoProducto,
    Tienda,
    Orden,
    OrdenDetalle,
    Vendedor,
)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    tipo = TipoProductoSerializer()

    class Meta:
        model = Producto
        fields = "__all__"


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = "__all__"


class VendedorSerializer(serializers.ModelSerializer):
    tienda = TiendaSerializer()

    class Meta:
        model = Vendedor
        fields = "__all__"


class OrdenDetalleSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = OrdenDetalle
        fields = "__all__"


class OrdenSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    tienda = TiendaSerializer()
    detalle = OrdenDetalleSerializer(
        many=True
    )  # many=True para indicar que es una relación de muchos a uno

    class Meta:
        model = Orden
        fields = "__all__"
