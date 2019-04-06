from django.urls import path, include
from . import views

from . import views

# URL para Clientes

app_name = "cliente"
cliente_patterns =[
    #path('', views.index, name='index'),
    path('cliente/<int:pk>/', views.DetailViewCliente.as_view(), name='detalhes_cliente'),
    path('cliente/incluir/', views.IncluirCliente, name='incluir_cliente'),
    path('cliente/listar', views.ListarClientes.as_view(), name='listar_cliente'),
]

# URL para Serviço

app_name = "servico"
servico_patterns =[
    path('servico/<int:pk>/', views.DetailViewServico.as_view(), name='detalhes_servico'),
    path('servico/incluir/', views.IncluirServico, name='incluir_Servico'),
]

# URL para Produto

app_name = "produto"
produto_patterns =[
    path('produto/<int:pk>/', views.DetailViewProduto.as_view(), name='detalhes_produto'),
    path('produto/incluir/', views.IncluirProduto, name='incluir_produto'),
]

urlpatterns = [
    path('', include(cliente_patterns)),
    path('', include(produto_patterns)),
    path('', include(servico_patterns)),
]