
from django.contrib import admin
from .models import Fornecedor


# Register your models here.
@admin.register(Fornecedor)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'fornecedor',
        'cnpj',
        'telefone',
    )
    search_fields = ('fornecedor',)
