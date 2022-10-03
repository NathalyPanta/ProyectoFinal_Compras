from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
from aplicaciones.core.models import Base


class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    ruc = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=50, null=True,unique=True)
    ciudad = models.CharField(max_length=50,verbose_name='Ciudad')
    direccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = "Proveedores"
        ordering = ('nombre',)

class Pedido(models.Model):
    referencia = models.CharField(primary_key=True,unique=True, max_length=10)
    proveedor = models.ForeignKey(Proveedor,null=True,blank=False, on_delete=models.CASCADE,)
    fecha = models.DateField(default= now)
    producto = models.CharField(verbose_name='Nombre del Producto',null=True, max_length=100, unique=True,blank=False)
    precio = models.FloatField(blank=False, verbose_name='Precio del Producto')
    cantidad = models.IntegerField(blank=False)
    subtotal = models.FloatField(blank=False)
    iva = models.FloatField(blank=False)
    total = models.FloatField(blank=False)



    def __str__(self):
        return "{}".format(self.referencia,)
    class Meta:
        verbose_name ="Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ('proveedor',)

# class PedidosDetalle(models.Model):
#     pedidoref = models.ForeignKey(Pedido,null=True,on_delete=models.CASCADE)
#     producto = models.CharField(verbose_name='Nombre del Producto', max_length=100, unique=True)
#     cantidad = models.IntegerField(default=0)
#     precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio del Producto')
#     subtotal = models.DecimalField(default=0, max_digits=16, decimal_places=2)
#     tasa_iva = models.FloatField(default=0, null=True, blank=True)
#     iva = models.DecimalField(default=0, max_digits=16, decimal_places=2)
#     total = models.DecimalField(default=0, max_digits=16, decimal_places=2)
#
#     def __str__(self):
#         return "{} - {}".format(self.producto, self.cantidad)

class RegistroCompra(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    hora = models.DateTimeField(auto_now_add=False, auto_now=True)
    fecha_registro = models.DateField(verbose_name='Fecha de Registro', default=now)
    referencia = models.ForeignKey(Pedido, blank=False, on_delete=models.CASCADE, null=True)
    producto = models.CharField(verbose_name='Nombre del Producto',max_length=100,null=True,unique=True,blank=False)
    cantidad = models.IntegerField(blank=False)
    precio = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Precio del Producto',blank=False)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2,blank=False)
    iva = models.DecimalField(max_digits=16, decimal_places=2,blank=False)
    total = models.DecimalField(max_digits=16, decimal_places=2,blank=False)

    def __str__(self):
        return "{} - {}".format(self.usuario,self.referencia)

    class Meta:
        verbose_name = "Registro de Compra"
        verbose_name_plural = "Registros de Compras"
        ordering = ('referencia',)