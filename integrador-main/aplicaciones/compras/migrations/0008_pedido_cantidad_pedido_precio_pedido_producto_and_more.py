# Generated by Django 4.1.1 on 2022-10-02 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0007_remove_pedido_cantidad_remove_pedido_precio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio del Producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Nombre del Producto'),
        ),
        migrations.DeleteModel(
            name='PedidosDetalle',
        ),
    ]
