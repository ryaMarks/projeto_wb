from django.urls import path
from ..produto import views as v
from django.contrib.auth.decorators import login_required

app_name = 'produto'
urlpatterns = [
    path('', login_required(v.ProdutoList.as_view()), name='produto_list'),
    path('<int:pk>/', login_required(v.produto_detail), name='produto_detail'),
    path('add/', login_required(v.ProdutoCreate.as_view()), name='produto_add'),
    path('<int:pk>/edit/', login_required(v.ProdutoUpdate.as_view()), name='produto_edit'),
    path('delete/<int:pk>', login_required(v.produto_delete), name='produto_delete'),
    path('<int:pk>/json/', login_required(v.produto_json), name='produto_json'),
    path('import/csv/', login_required(v.import_csv), name='import_csv'),
    path('export/xlsx/', login_required(v.exportar_produtos_xlsx), name='export_xlsx'),
]
