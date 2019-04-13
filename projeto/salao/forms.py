from django import forms
from salao.models import Cliente, Venda, Reserva, Servico, Produto

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        nome_cliente = forms.CharField(label='Nome do Cliente', max_length=255, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Joaquim Osório'}))
        telefone_cliente = forms.CharField(label='Telefone do Cliente', max_length=255, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '(##) # #### - ####', 'type':'phone'}))
        instagram_cliente = forms.CharField(label='Instagram do Cliente', max_length=255, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '@joazinho123'}))
        bairro_cliente = forms.CharField(label='Bairro do Cliente', max_length=255, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Industrial'}))
        fields = '__all__'
            # fields = ('nome_cliente', 'telefone_cliente', 'instagram_cliente', 'bairro_cliente',)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('desc_produto', 'pontos_produto', 'valor_produto', 'marca_produto',)

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ('desc_servico', 'pontos_servico', 'valor_servico',)
