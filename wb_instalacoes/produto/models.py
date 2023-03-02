from django.db import models
from django.urls import reverse_lazy
from datetime import datetime
from ..fornecedores.models import Fornecedor
# Create your models here.

MEDIDAS = (
    ('M', 'Metros (m)'),
    ('KG', 'Kilos (Kg)'),
    ('UN', 'Unidades'),
)


class Produto(models.Model):
    codigo = models.CharField('Codigo de Registro', max_length=8, unique=True)
    produto = models.CharField('Produto', max_length=100, unique=True)
    medida = models.CharField('Unidade de Medida', max_length=50, choices=MEDIDAS)
    preco = models.DecimalField('Preço da unidade (R$)', max_digits=7, decimal_places=2)
    fabricante = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    estoque = models.IntegerField('estoque atual', null=True)
    data = datetime.now()


#    codigo,  # id do produto
#    descricao,
#    ncm,
#    cfop,
#    unidade_comercial,
#    ean = 'SEM GTIN',
#    ean_tributavel = 'SEM GTIN',
#    quantidade_comercial = Decimal('12'),  # 12 unidades
#    valor_unitario_comercial = Decimal('9.75'),  # preço unitário
#    valor_total_bruto = Decimal('117.00'),  # preço total
#    unidade_tributavel = 'UN',
#    quantidade_tributavel = Decimal('12'),
#    valor_unitario_tributavel = Decimal('9.75'),
#    ind_total = 1,
#    icms_modalidade = '102',
#    icms_origem = 0,
#    icms_csosn = '400',
#    pis_modalidade = '07',
#    cofins_modalidade = '07',
#    valor_tributos_aprox = '21.06'


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

