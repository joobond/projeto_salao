from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from salao.models import Cliente, Servico, Produto
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import ClienteForm

class DetailViewCliente(generic.DetailView):
    model = Cliente
    template_name = 'salao/cliente/detalhes.html'

def IncluirCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
    else:
        form = ClienteForm()
        return render(request, 'cliente/incluir.html', {'form': form})




