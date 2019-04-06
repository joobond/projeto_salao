from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.list import ListView
from .forms import ClienteForm, ProdutoForm, ServicoForm
from salao.models import Cliente, Servico, Produto


class DetailViewCliente(generic.DetailView):
    model = Cliente
    template_name = 'salao/cliente/detalhes.html'

class DetailViewServico(generic.DetailView):
    model = Servico
    template_name = 'salao/servico/detalhes.html'

class DetailViewProduto(generic.DetailView):
    model = Produto
    template_name = 'salao/produto/detalhes.html'

class ListarClientes(ListView):
    template_name = 'salao/cliente/listar.html'
    model = Cliente
    context_object_name = 'clientes'
    paginate_by=10

def IncluirCliente(request):
    template_name = 'salao/cliente/incluir.html'
    if request.method == "POST":
        form = ClienteForm(request.POST)
        cliente = form.save(commit=False)
        cliente.save()
        return redirect("cliente:detalhes_cliente", pk=cliente.pk)
    else:
        form = ClienteForm()
        return render(request, template_name, {'form': form})

def IncluirProduto(request):
    template_name = 'salao/produto/incluir.html'
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        produto = form.save(commit=False)
        produto.save()
        return redirect("produto:detalhes_produto", pk=produto.pk)
    else:
        form = ProdutoForm()
        return render(request, template_name, {'form': form})

def IncluirServico(request):
    template_name = 'salao/servico/incluir.html'
    if request.method == "POST":
        form = ServicoForm(request.POST)
        servico = form.save(commit=False)
        servico.save()
        return redirect("servico:detalhes_servico", pk=servico.pk)
    else:
        form = ServicoForm()
        return render(request, template_name, {'form': form})