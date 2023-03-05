from django.db import models
from django.urls import reverse_lazy


# variaveis de lista

ESTADOS_BR = (
    ('---', '---'),
    ('Acre (AC)', 'Acre (AC)'),
    ('Alagoas (AL)', 'Alagoas (AL)'),
    ('Amapá (AP)', 'Amapá (AP)'),
    ('Amazonas (AM)', 'Amazonas (AM)'),
    ('Bahia (BA)', 'Bahia (BA)'),
    ('Ceará (CE)', 'Ceará (CE)'),
    ('Distrito Federal (DF)', 'Distrito Federal (DF)'),
    ('Espírito Santo (ES)', 'Espírito Santo (ES)'),
    ('Goiás (GO)', 'Goiás (GO)'),
    ('Maranhão (MA)', 'Maranhão (MA)'),
    ('Mato Grosso (MT)', 'Mato Grosso (MT)'),
    ('Mato Grosso do Sul (MS)', 'Mato Grosso do Sul (MS)'),
    ('Minas Gerais (MG)', 'Minas Gerais (MG)'),
    ('Pará (PA)', 'Pará (PA)'),
    ('Paraíba (PB)', 'Paraíba (PB)'),
    ('Paraná (PR)', 'Paraná (PR)'),
    ('Pernambuco (PE)', 'Pernambuco (PE)'),
    ('Piauí (PI)', 'Piauí (PI)'),
    ('Rio de Janeiro (RJ)', 'Rio de Janeiro (RJ)'),
    ('Rio Grande do Norte (RN)', 'Rio Grande do Norte (RN)'),
    ('Rio Grande do Sul (RS)', 'Rio Grande do Sul (RS)'),
    ('Rondônia (RO)', 'Rondônia (RO)'),
    ('Roraima (RR)', 'Roraima (RR)'),
    ('Santa Catarina (SC)', 'Santa Catarina (SC)'),
    ('São Paulo (SP)', 'São Paulo (SP)'),
    ('Sergipe (SE)', 'Sergipe (SE)'),
    ('Tocantins (TO)', 'Tocantins (TO)'),
)



# Create your models here.
class Fornecedor(models.Model):
    fornecedor = models.CharField('Razão Social', max_length=50, unique=True)
    cnpj = models.CharField('CNPJ', max_length=50, unique=True)
    inscricao = models.CharField('Inscrição Estadual', max_length=50, unique=True)
    telefone = models.CharField('Telefone', max_length=20)

    # dados de endereco (transformar em um campo so)
    endereco = models.CharField('Endereço completo', max_length=100, blank=True)

    class Meta:
        ordering = ('fornecedor', )

    def __str__(self):
        return self.fornecedor

    def get_absolute_url(self):
        return reverse_lazy('fornecedores:fornecedor_detail', kwargs={'pk': self.pk})
