from django.contrib.auth.models import User
from django.db import models
from ..core.models import TimeStampedModel
from ..produto.models import Produto
from ..clientes.models import Cliente
from ..fornecedores.models import Fornecedor
from .managers import EstoqueEntradaManager, EstoqueSaidaManager

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=False)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}'.format(self.pk, self.created.strftime('%d-%m-%Y'))


    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


class EstoqueEntrada(Estoque):

    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'


class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)


