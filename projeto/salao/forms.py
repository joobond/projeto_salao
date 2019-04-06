from django import forms
from salao.models import Cliente, Venda, Reserva, Servico, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'telefone_cliente', 'instagram_cliente', 'bairro_cliente',)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('desc_produto', 'pontos_produto', 'valor_produto', 'marca_produto',)

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ('desc_servico', 'pontos_servico', 'valor_servico',)
