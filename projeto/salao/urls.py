from django.urls import path
from . import views

from . import views

urlpatterns =[
    #path('', views.index, name='index'),
    path('salao/cliente/<int:pk>/', views.DetailViewCliente.as_view(), name='detalhes_cliente'),
    path('salao/cliente/incluir/', views.IncluirCliente, name='incluir_cliente'),
    #path('cliente/listar', views.ListarClientes, name='listar_cliente'),
]