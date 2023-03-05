# Generated by Django 4.1.7 on 2023-03-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='lucro',
            field=models.CharField(max_length=50, null=True, verbose_name='Margem de lucro (%)'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço de compra da unidade (R$)'),
        ),
    ]
