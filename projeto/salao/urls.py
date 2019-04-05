from django.urls import path
from . import views

from . import views

app_name = "cliente"

urlpatterns =[
    #path('', views.index, name='index'),
    path('cliente/<int:pk>/', views.DetailViewCliente.as_view(), name='detalhes_cliente'),
    path('cliente/incluir/', views.IncluirCliente, name='incluir_cliente'),
    #path('cliente/listar', views.ListarClientes, name='listar_cliente'),
]