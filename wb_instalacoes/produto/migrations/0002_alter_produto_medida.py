# Generated by Django 4.1.7 on 2023-03-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='medida',
            field=models.CharField(choices=[('M- Metros', 'Metros (m)'), ('KG - Kilos', 'Kilos (Kg)'), ('UN- Unidades', 'Unidades')], max_length=50, verbose_name='Unidade de Medida'),
        ),
    ]
