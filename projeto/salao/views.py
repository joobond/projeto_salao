from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import DeleteView
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

class ListarProdutos(ListView):
    template_name = 'salao/produto/listar.html'
    model = Produto
    context_object_name = 'produtos'
    paginate_by=10

def IncluirCliente(request):
    template_name = 'salao/cliente/incluir.html'
    if request.method == "POST":
        form = ClienteForm(request.POST)
        cliente = form.save(commit=False)
        cliente.save()
        return HttpResponseRedirect(reverse('salao:detalhes_cliente',args=[cliente.pk]))
    else:
        form = ClienteForm()
        return render(request, template_name, {'form': form})

def DeletarCliente(request):
    template_name='salao/produto/listar.html'
    if request.method == "POST":
        cliente = Cliente.objects.get(pk=request.POST.get("id"))
        print(cliente)
        cliente.delete()
        return redirect("salao:listar_clientes")


def IncluirProduto(request):
    template_name = 'salao/produto/incluir.html'
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        produto = form.save(commit=False)
        produto.save()
        return redirect("salao:detalhes_produto", pk=produto.pk)
    else:
        form = ProdutoForm()
        return render(request, template_name, {'form': form})

def IncluirServico(request):
    template_name = 'salao/servico/incluir.html'
    if request.method == "POST":
        form = ServicoForm(request.POST)
        servico = form.save(commit=False)
        servico.save()
        return redirect("cliente:detalhes_servico", pk=servico.pk)
    else:
        form = ServicoForm()
        return render(request, template_name, {'form': form})