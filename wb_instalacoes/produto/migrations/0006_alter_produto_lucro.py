# Generated by Django 4.1.7 on 2023-03-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_rename_preco_produto_preco_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='lucro',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True, verbose_name='Margem de lucro (%)'),
        ),
    ]
