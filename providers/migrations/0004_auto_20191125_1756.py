# Generated by Django 2.2.7 on 2019-11-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_auto_20191125_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='register_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id de registro'),
        ),
    ]