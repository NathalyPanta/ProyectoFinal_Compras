# Generated by Django 4.1.1 on 2022-09-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
                ('ciudad', models.CharField(max_length=50, unique=True, verbose_name='Ciudad')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]