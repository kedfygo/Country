# Generated by Django 2.2.7 on 2019-12-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20191209_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='proof_of_payment',
            field=models.ImageField(upload_to='payments/%(name)s', verbose_name='Comprobante de Pago'),
        ),
    ]