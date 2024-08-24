# Vistas de la Rest API

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from factura.models import (
    Cliente,
    Producto,
    TipoProducto,
    Tienda,
    Orden,
    Vendedor,
)
from factura.serializers import (
    ClienteSerializer,
    ProductoSerializer,
    TipoProductoSerializer,
    TiendaSerializer,
    OrdenSerializer,
    OrdenDetalleSerializer,
    VendedorSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()  # seleccionar todos los registros de la BD
    serializer_class = ClienteSerializer


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class TiendaViewSet(viewsets.ModelViewSet):
    queryset = Tienda.objects.all()
    serializer_class = TiendaSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request):
        """
        Obtener los datos del request:
        JSON
        {
            "cliente": 1,
            "vendedor": 1,
            "detalle": [
                {
                    "producto": 1,
                    "cantidad": 1
                },
                {
                    "producto": 2,
                    "cantidad": 1
                },
            ]
        }
        """

        # recibir los datos del cliente por medio de POST
        order_detalles = request.POST.pop("detalle")
        # obtiene el serializer_class
        serializer = self.get_serializer(request.POST)
        # valida los datos del request
        if serializer.is_valid(raise_exception=True):
            order = serializer.save()

        # si viene el detalle lo agregamos a la orden
        for order_detalle in order_detalles:
            order_detalle["orden"] = order.id
            serializer_detalle = OrdenDetalleSerializer(data=order_detalle)
            if serializer_detalle.is_valid(raise_exception=True):
                serializer_detalle.save

        # retorna el objeto creado
        return Response(serializer.data, status=status.HTTP_201_CREATED)
