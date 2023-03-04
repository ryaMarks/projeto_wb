from django.urls import include, path
from django.contrib.auth.decorators import login_required
from ..estoque import views as v

app_name = 'estoque'


entrada_patterns = [
    path('', login_required(v.EstoqueEntradaList.as_view()), name='estoque_entrada_list'),
    path('add/', login_required(v.estoque_entrada_add), name='estoque_entrada_add'),
]

saida_patterns = [
    path('', login_required(v.EstoqueSaidaList.as_view()), name='estoque_saida_list'),
    path('add/', login_required(v.estoque_saida_add), name='estoque_saida_add'),
]


urlpatterns = [
    path('<int:pk>/', login_required(v.EstoqueDetail.as_view()), name='estoque_detail'),
    path('<int:pk>/geraPDF/', login_required(v.pdf_generate), name='gerarPDF'),
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),
]
