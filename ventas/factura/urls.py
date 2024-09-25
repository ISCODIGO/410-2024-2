from django.urls import path, include

from rest_framework.routers import DefaultRouter

from factura.api import (
    ClienteViewSet,
    OrdenViewSet,
    ProductoViewSet,
    TipoProductoViewSet,
    TiendaViewSet,
    VendedorViewSet,
)

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"ordenes", OrdenViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"producto-tipos", TipoProductoViewSet)
router.register(r"tiendas", TiendaViewSet)
router.register(r"vendedores", VendedorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
