# Generated by Django 4.1.7 on 2023-03-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0005_alter_estoque_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='nf',
            field=models.PositiveIntegerField(null=True, verbose_name='nota fiscal'),
        ),
    ]
