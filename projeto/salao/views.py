from django.shortcuts import render, get_object_or_404, redirect
from django.http import  HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.list import ListView
from django.views.generic import DeleteView, TemplateView
from .forms import ClienteForm, ProdutoForm, ServicoForm, ReservaForm, VendaForm
from salao.models import Cliente, Servico, Produto, Reserva, Venda
from datetime import date

class Index(TemplateView):
  template_name = "salao/index.html"

# Produto
class DetailViewProduto(generic.DetailView):
    model = Produto
    template_name = 'salao/produto/reservas_de_hoje.html'


class ListarProdutos(ListView):
    template_name = 'salao/produto/listar.html'
    model = Produto
    context_object_name = 'produtos'
    paginate_by=10


def IncluirProduto(request):
    template_name = 'salao/produto/incluir.html'
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        produto = form.save(commit=False)
        produto.save()
        return HttpResponseRedirect(reverse('salao:listar_produtos'))
    else:
        form = ProdutoForm()
        return render(request, template_name, {'form': form})


def DeletarProduto(request):
    template_name='salao/produto/listar.html'
    if request.method == "POST":
        produto = Produto.objects.get(pk=request.POST.get("id"))
        produto.delete()
        return redirect("salao:listar_produtos")


def EditarProduto(request, pk):
    template_name = 'salao/produto/incluir.html'
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        produto = form.save(commit=False)
        produto.pk = pk
        produto.save()
        return HttpResponseRedirect(reverse('salao:listar_produtos'))
    else:
        form = ProdutoForm(instance=produto)
        return render(request, template_name, {'form': form, 'editar':True, 'produto':produto})


# Cliente
class DetailViewCliente(generic.DetailView):
    model = Cliente
    template_name = 'salao/cliente/reservas_de_hoje.html'


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
        return HttpResponseRedirect(reverse('salao:listar_clientes'))
    else:
        form = ClienteForm()
        return render(request, template_name, {'form': form})


def EditarCliente(request, pk):
    template_name = 'salao/cliente/incluir.html'
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        form = ClienteForm(request.POST)
        cliente = form.save(commit=False)
        cliente.pk = pk
        cliente.save()
        return HttpResponseRedirect(reverse('salao:listar_clientes'))
    else:
        form = ClienteForm(instance=cliente)
        return render(request, template_name, {'form': form, 'editar':True, 'cliente':cliente})


def DeletarCliente(request):
    template_name='salao/cliente/listar.html'
    if request.method == "POST":
        cliente = Cliente.objects.get(pk=request.POST.get("id"))
        cliente.delete()
        return redirect("salao:listar_clientes")

def MelhoresClientes(request):
    template_name='salao/cliente/melhores.html'
    clientes = sorted(Cliente.objects.all(), key=lambda t: t.pontos_cliente, reverse=True)[:5]
    return render(request, template_name, {'clientes': clientes})


# Serviço
class DetailViewServico(generic.DetailView):
    model = Servico
    template_name = 'salao/servico/reservas_de_hoje.html'


def IncluirServico(request):
    template_name = 'salao/servico/incluir.html'
    if request.method == "POST":
        form = ServicoForm(request.POST)
        servico = form.save(commit=False)
        servico.save()
        return redirect("salao:detalhes_servico", pk=servico.pk)
    else:
        form = ServicoForm()
        return render(request, template_name, {'form': form})


def EditarServico(request, pk):
    template_name = 'salao/servico/incluir.html'
    servico = get_object_or_404(Servico, pk=pk)

    if request.method == "POST":
        form = ServicoForm(request.POST)
        servico = form.save(commit=False)
        servico.pk = pk
        servico.save()
        return HttpResponseRedirect(reverse('salao:listar_servicos'))
    else:
        form = ServicoForm(instance=servico)
        return render(request, template_name, {'form': form, 'editar':True, 'servico':servico})


class ListarServicos(ListView):
    template_name = 'salao/servico/listar.html'
    model = Servico
    context_object_name = 'servicos'
    paginate_by=10


def DeletarServico(request):
    template_name='salao/servico/listar.html'
    if request.method == "POST":
        servico = Servico.objects.get(pk=request.POST.get("id"))
        servico.delete()
        return redirect("salao:listar_servicos")


# Reserva

def IncluirReserva(request):
    template_name = 'salao/reserva/incluir.html'
    if request.method == "POST":
        form = ReservaForm(request.POST)
        reserva = form.save(commit=False)
        reserva.save()
        return redirect("salao:reservas_hoje")
    else:
        form = ReservaForm()
        return render(request, template_name, {'form': form})


def ReservasHoje(request):
    template_name='salao/reserva/reservas_de_hoje.html'
    reservas = []
    for reserva in Reserva.objects.all():
        if reserva.data_reserva == date.today():
            reservas.append(reserva)
    return render(request,template_name, {'reservas':reservas, 'hoje':date.today()})


#Venda

def FazerVenda(request):
    template_name = 'salao/venda/incluir.html'
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("salao:index")
    else:
        form = VendaForm()
        return render(request, template_name, {'form': form})



