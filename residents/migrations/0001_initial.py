# Generated by Django 2.2.7 on 2019-11-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='residents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('lastname', models.CharField(max_length=50, verbose_name='apellido')),
                ('address', models.CharField(max_length=100, verbose_name='dirección')),
                ('email', models.EmailField(max_length=254, verbose_name='correo electrónico')),
                ('type_of_property', models.CharField(max_length=50, verbose_name='tipo de inmueble')),
                ('owner_name', models.CharField(max_length=100, verbose_name='nombre del propietario')),
            ],
        ),
    ]