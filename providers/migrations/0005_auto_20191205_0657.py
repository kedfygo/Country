# Generated by Django 2.2.7 on 2019-12-05 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0004_auto_20191125_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='providers',
            options={'ordering': ['description'], 'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
    ]