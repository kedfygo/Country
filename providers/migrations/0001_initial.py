# Generated by Django 2.2.7 on 2019-11-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('register_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='id de registro')),
                ('description', models.CharField(max_length=200, verbose_name='razón social')),
                ('rfc', models.CharField(max_length=30, verbose_name='Número de RFC')),
                ('address', models.CharField(max_length=200, verbose_name='dirección')),
                ('category', models.CharField(max_length=50, verbose_name='Categoría')),
                ('phone', models.CharField(max_length=50, verbose_name='número telefónico')),
                ('email', models.EmailField(max_length=254, verbose_name='correo electrónico')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['register_id'],
            },
        ),
    ]
