from django.contrib import admin
from aplicaciones.compras.models import Proveedor, Pedido, RegistroCompra

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','ruc','telefono','email',)
    ordering = ('nombre',)
    search_fields = ('nombre', 'ruc',)
admin.site.register(Proveedor,ProveedorAdmin)


class PedidoAdmin(admin.ModelAdmin):

    list_display = ('referencia','producto','fecha','total')
    list_per_page = 10
    ordering = ('-fecha',)
    search_fields = ('fecha','referencia')
    list_filter = ('fecha',)


admin.site.register(Pedido,PedidoAdmin)

class RegistroAdmin (admin.ModelAdmin):
    list_display = ('id','referencia','cantidad','producto','total','hora')
    ordering = ('-fecha_registro',)
    search_fields = ('producto', 'referencia')

admin.site.register(RegistroCompra,RegistroAdmin)