# Generated by Django 2.2.7 on 2019-11-24 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='residents',
            options={'ordering': ['-lastname'], 'verbose_name': 'Residente', 'verbose_name_plural': 'Residentes'},
        ),
    ]