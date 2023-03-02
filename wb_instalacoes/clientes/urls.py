from django.urls import path
from ..clientes import views as v
from django.contrib.auth.decorators import login_required

app_name = 'clientes'
urlpatterns = [
    path('', login_required(v.ClientesList.as_view()), name='clientes_list'),
    path('add/', login_required(v.add_client.as_view()), name='clientes_add'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('<int:pk>/edit/', login_required(v.ClienteUpdate.as_view()), name='cliente_edit'),
    path('delete/<int:pk>', v.cliente_delete, name='cliente_delete'),
]
