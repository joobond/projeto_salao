from django import forms
from salao.models import Cliente, Venda, Reserva, Servico, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone_cliente', 'instagram_cliente', 'bairro_cliente',)
