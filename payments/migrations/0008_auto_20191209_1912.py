# Generated by Django 2.2.7 on 2019-12-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20191209_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='proof_of_payment',
            field=models.ImageField(upload_to='payments', verbose_name='Comprobante de Pago'),
        ),
    ]