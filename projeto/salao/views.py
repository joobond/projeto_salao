from django.shortcuts import render, get_object_or_404
from salao.models import Cliente, Servico, Produto
from django.template import loader
from django.urls import reverse
from django.views import generic
from .forms import ClienteForm


class DetailViewCliente(generic.DetailView):
    model = Cliente
    template_name = 'salao/cliente/detalhes.html'

def IncluirCliente(request):
    template_name = 'salao/cliente/incluir.html'
    if request.method == "POST":
        form = ClienteForm(request.POST)
        cliente = form.save(commit=False)
        cliente.save()
        #return redirect('detalhes_cliente', pk=cliente.pk)
    else:
        form = ClienteForm()

    return render(request, template_name, {'form': form})




