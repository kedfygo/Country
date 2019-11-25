# Generated by Django 2.2.7 on 2019-11-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='fecha')),
                ('folio', models.CharField(max_length=50, verbose_name='folio')),
                ('provider', models.CharField(max_length=200, verbose_name='proveedor')),
                ('description', models.CharField(max_length=200, verbose_name='descripción')),
                ('notes', models.CharField(max_length=300, verbose_name='observaciones adicionales')),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
                'ordering': ['-date'],
            },
        ),
    ]