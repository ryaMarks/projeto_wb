from django.urls import path
from ..fornecedores import views as v
from django.contrib.auth.decorators import login_required

app_name = 'fornecedores'
urlpatterns = [
    path('', login_required(v.FornecedoresList.as_view()), name='fornecedores_list'),
    path('add/', login_required(v.add_fornecedor.as_view()), name='fornecedor_add'),
    path('<int:pk>/', v.fornecedor_detail, name='fornecedor_detail'),
    path('<int:pk>/edit/', login_required(v.FornecedorUpdate.as_view()), name='fornecedor_edit'),
    path('delete/<int:pk>', v.fornecedor_delete, name='fornecedores_delete'),
]
