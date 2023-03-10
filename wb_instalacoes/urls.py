from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('wb_instalacoes.accounts.urls')),
    path('clientes/', include('wb_instalacoes.clientes.urls')),
    path('', include('wb_instalacoes.core.urls')),
    path('fornecedores/', include('wb_instalacoes.fornecedores.urls')),
    path('produto/', include('wb_instalacoes.produto.urls')),
    path('estoque/', include('wb_instalacoes.estoque.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
