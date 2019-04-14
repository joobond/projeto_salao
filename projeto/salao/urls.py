from django.urls import path, include
from . import views

from . import views

app_name = 'salao'
# URL para Clientes
cliente_patterns =[
    path('cliente/<int:pk>/', views.DetailViewCliente.as_view(), name='detalhes_cliente'),
    path('cliente/incluir/', views.IncluirCliente, name='incluir_cliente'),
    path('cliente/editar/<int:pk>/', views.EditarCliente, name='editar_cliente'),
    path('cliente/listar/', views.ListarClientes.as_view(), name='listar_clientes'),
    path('cliente/deletar', views.DeletarCliente, name='deletar_cliente'),
]

# URL para Serviço
servico_patterns =[
    path('servico/<int:pk>/', views.DetailViewServico.as_view(), name='detalhes_servico'),
    path('servico/incluir/', views.IncluirServico, name='incluir_Servico'),
]

# URL para Produto
produto_patterns =[
    path('produto/listar/', views.ListarProdutos.as_view(), name='listar_produtos'),
    path('produto/<int:pk>/', views.DetailViewProduto.as_view(), name='detalhes_produto'),
    path('produto/incluir/', views.IncluirProduto, name='incluir_produto'),
    path('produto/editar/<int:pk>/', views.EditarProduto, name='editar_produto'),
    path('produto/deletar', views.DeletarProduto, name='deletar_produto'),
]

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('', include(cliente_patterns)),
    path('', include(produto_patterns)),
    path('', include(servico_patterns)),
]
