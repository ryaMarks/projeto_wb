# Generated by Django 4.1.7 on 2023-03-05 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Tipo_de_inscrição_estadual',
        ),
    ]
