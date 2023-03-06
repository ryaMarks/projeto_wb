from django.db import models
from django.urls import reverse_lazy
from datetime import datetime
from ..fornecedores.models import Fornecedor
from decimal import Decimal
# Create your models here.

MEDIDAS = (
    ('M- Metros', 'Metros (m)'),
    ('KG - Kilos', 'Kilos (Kg)'),
    ('UN- Unidades', 'Unidades'),
)


class Produto(models.Model):
    codigo = models.CharField('Codigo de Registro', max_length=8, unique=True)
    produto = models.CharField('Produto', max_length=100, unique=True)
    medida = models.CharField('Unidade de Medida', max_length=50, choices=MEDIDAS)
    preco_compra = models.DecimalField('Preço de compra da unidade (R$)', max_digits=7, decimal_places=2)
    lucro = models.IntegerField('Margem de lucro (%)', null=True)
    preco_venda = 0
    fabricante = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    estoque = models.IntegerField('estoque atual', null=True)
    data = datetime.now()


    class Meta:
        ordering = ('produto', )

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }

