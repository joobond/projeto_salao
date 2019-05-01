from django.urls import path, include
from . import views

from . import views

app_name = 'salao'
# URL para Clientes
cliente_patterns =[
    path('cliente/<int:pk>/', views.DetailViewCliente.as_view(), name='detalhes_cliente'),
    path('cliente/incluir/', views.IncluirCliente, name='incluir_cliente'),
    path('cliente/melhores/', views.MelhoresClientes, name='melhores_clientes'),
    path('cliente/editar/<int:pk>/', views.EditarCliente, name='editar_cliente'),
    path('cliente/listar/', views.ListarClientes.as_view(), name='listar_clientes'),
    path('cliente/deletar', views.DeletarCliente, name='deletar_cliente'),
]

# URL para Serviço
servico_patterns =[
    path('servico/<int:pk>/', views.DetailViewServico.as_view(), name='detalhes_servico'),
    path('servico/incluir/', views.IncluirServico, name='incluir_servico'),
    path('servico/listar/', views.ListarServicos.as_view(), name='listar_servicos'),
    path('servico/editar/<int:pk>/', views.EditarServico, name='editar_servico'),
    path('servico/deletar', views.DeletarServico, name='deletar_servico'),
]

# URL para Produto
produto_patterns =[
    path('produto/listar/', views.ListarProdutos.as_view(), name='listar_produtos'),
    path('produto/<int:pk>/', views.DetailViewProduto.as_view(), name='detalhes_produto'),
    path('produto/incluir/', views.IncluirProduto, name='incluir_produto'),
    path('produto/editar/<int:pk>/', views.EditarProduto, name='editar_produto'),
    path('produto/deletar', views.DeletarProduto, name='deletar_produto'),
]

# URL para Reserva
reserva_patterns =[
    path('reserva/incluir/', views.IncluirReserva, name='incluir_reserva'),
    path('reserva/hoje/', views.ReservasHoje, name='reservas_hoje'),
]

# URL para Venda
venda_patterns =[
    path('venda/', views.FazerVenda, name='fazer_venda'),
]

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login', views.Login, name='login'),
    path('', include(cliente_patterns)),
    path('', include(produto_patterns)),
    path('', include(servico_patterns)),
    path('', include(reserva_patterns)),
    path('', include(venda_patterns)),
]
