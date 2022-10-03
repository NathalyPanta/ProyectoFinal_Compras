from django.urls import path

from aplicaciones.compras.views.menuc.views import ComprasMTemplateView
from aplicaciones.compras.views.proveedor.views import ProveedorListView,CrearProveedor,ActualizarProveedor, EliminarProveedor
from aplicaciones.compras.views.pedido.view import PedidosListView, CrearPedido, ActualizarPedido, EliminarPedido
from aplicaciones.compras.views.registro.views import RegistroCompraListView, CrearRegistro, ActualizarRegistro, \
    EliminarRegistro

app_name= "compras"


urlpatterns = [
    path('menu', ComprasMTemplateView.as_view(),name='menu'),
    # Proveedor
    path('proveedor/', ProveedorListView.as_view(),name='proveedor'),
    path('crearprov/', CrearProveedor.as_view(),name='crearprov'),
    path('actualizarprov/<int:pk>/', ActualizarProveedor.as_view(),name='actualizarprov'),
    path('eliminarprov/<int:pk>/',EliminarProveedor.as_view(),name='eliminarprov'),
    # PEDIDO
    path('pedidos/', PedidosListView.as_view(),name='pedido'),
    path('crearpedido/', CrearPedido.as_view(),name='crearpedido'),
    path('actualizapedido/<int:pk>/', ActualizarPedido.as_view(),name='actualizapedido'),
    path('eliminapedido/<int:pk>/', EliminarPedido.as_view(),name='eliminapedido'),



    # REGISTRO
    path('registroc/', RegistroCompraListView.as_view(),name='registroc'),
    path('crearRegistro/', CrearRegistro.as_view(),name='crearRegistro'),
    path('actualizaRegistro/<int:pk>/', ActualizarRegistro.as_view(),name='actualizaRegistro'),
    path('eliminaRegistro/<int:pk>/', EliminarRegistro.as_view(),name='eliminaRegistro'),



]