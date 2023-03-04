from django.db import models
from django.urls import reverse_lazy


# variaveis de lista
PESSOA_TIPO = (
    ('---', '---'),
    ('Pessoa Física', 'Pessoa Física'),
    ('Pessoa Juridica', 'Pessoa Jurídica'),
)

ESTADOS_BR = (
    ('---', '---'),
    ('Acre (AC)', 'Acre (AC)'),
    ('Alagoas (AL)','Alagoas (AL)'),
    ('Amapá (AP)','Amapá (AP)'),
    ('Amazonas (AM)','Amazonas (AM)'),
    ('Bahia (BA)','Bahia (BA)'),
    ('Ceará (CE)','Ceará (CE)'),
    ('Distrito Federal (DF)','Distrito Federal (DF)'),
    ('Espírito Santo (ES)','Espírito Santo (ES)'),
    ('Goiás (GO)','Goiás (GO)'),
    ('Maranhão (MA)','Maranhão (MA)'),
    ('Mato Grosso (MT)', 'Mato Grosso (MT)'),
    ('Mato Grosso do Sul (MS)','Mato Grosso do Sul (MS)'),
    ('Minas Gerais (MG)','Minas Gerais (MG)'),
    ('Pará (PA)','Pará (PA)'),
    ('Paraíba (PB)','Paraíba (PB)'),
    ('Paraná (PR)','Paraná (PR)'),
    ('Pernambuco (PE)','Pernambuco (PE)'),
    ('Piauí (PI)','Piauí (PI)'),
    ('Rio de Janeiro (RJ)', 'Rio de Janeiro (RJ)'),
    ('Rio Grande do Norte (RN)', 'Rio Grande do Norte (RN)'),
    ('Rio Grande do Sul (RS)', 'Rio Grande do Sul (RS)'),
    ('Rondônia (RO)', 'Rondônia (RO)'),
    ('Roraima (RR)','Roraima (RR)'),
    ('Santa Catarina (SC)','Santa Catarina (SC)'),
    ('São Paulo (SP)','São Paulo (SP)'),
    ('Sergipe (SE)', 'Sergipe (SE)'),
    ('Tocantins (TO)', 'Tocantins (TO)'),
)

IE_TIPO = (
    ('---', '---'),
    ('1', 'Contribuinte de ICMS'),
    ('9', 'Não contribuinte de ICMS'),
    ('---', 'Contribuinte isento'),
)


# Create your models here.
class Cliente(models.Model):
    tipo = models.CharField(max_length=50, choices=PESSOA_TIPO, default='---')
    cliente = models.CharField('Nome / Razão Social', max_length=50, unique=True)
    cpf_cnpj = models.CharField('CPF / CNPJ', max_length=50, unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.CharField('E-Mail', max_length=50)
    Tipo_de_inscrição_estadual = models.CharField(max_length=50, choices=IE_TIPO, default='---')  # 9=Não contribuinte

    # dados de endereco
    rua = models.CharField('Endereço - Rua', max_length=100, blank=False, null=True)
    numero = models.CharField('Nª da casa', max_length=10, null=True)
    complemento = models.CharField('Endereço - Complemento', max_length=100, null=True)
    bairro = models.CharField('Endereço - Bairro', max_length=100)
    cidade = models.CharField('Endereço - Cidade', max_length=100, blank=False)
    estado = models.CharField('Endereço - Estado', max_length=50, choices=ESTADOS_BR, default='---')
    cep = models.CharField('Endereço - CEP', max_length=50)


    class Meta:
        ordering = ('cliente', )

    def __str__(self):
        return self.cliente

    def get_absolute_url(self):
        return reverse_lazy('clientes:cliente_detail', kwargs={'pk': self.pk})

