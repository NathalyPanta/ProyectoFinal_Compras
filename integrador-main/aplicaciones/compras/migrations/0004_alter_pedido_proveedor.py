# Generated by Django 4.1.1 on 2022-09-26 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_alter_registrocompra_options_registrocompra_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor'),
        ),
    ]