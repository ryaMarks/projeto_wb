# Generated by Django 4.1.7 on 2023-03-05 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_produto_lucro_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='lucro',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, verbose_name='Margem de lucro (%)'),
        ),
    ]