from django import forms
from salao.models import Cliente, Venda, Reserva, Servico, Produto
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

'''class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control'}
        self.fields['password'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': None,
            'password': None,
        }
        help_texts = {
            'username': None,
            'password': None,
        }
        widgets = {
            'password': forms.PasswordInput,
        }'''


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'form-control'}
        self.fields['password'].widget.attrs = {'class': 'form-control'}

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nome_cliente'].widget.attrs = {'class': 'form-group form-control', 'type':'text', 'placeholder':'Joãzinho'}
        self.fields['telefone_cliente'].widget.attrs = {'class': 'form-group form-control', 'type':'phone', 'placeholder':'(##) # ####-####'}
        self.fields['instagram_cliente'].widget.attrs = {'class': 'form-group form-control', 'type':'text', 'placeholder':'@usuario'}
        self.fields['bairro_cliente'].widget.attrs = {'class': 'form-group form-control', 'type':'address', 'placeholder':'Centro'}


    class Meta:
        model= Cliente
        fields = ['nome_cliente', 'telefone_cliente', 'instagram_cliente', 'bairro_cliente']
        labels = {
            'nome_cliente':'Nome do Cliente',
            'telefone_cliente':'Telefone do Cliente',
            'instagram_cliente':'Instagram do Cliete',
            'bairro_cliente':'Bairro do Cliente',
        }

class ProdutoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['desc_produto'].widget.attrs = {'class': 'form-group form-control', 'type':'text', 'placeholder':'Xampuzin'}
        self.fields['pontos_produto'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'666'}
        self.fields['valor_produto'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'R$ 55'}
        self.fields['marca_produto'].widget.attrs = {'class': 'form-group form-control', 'type':'text', 'placeholder':'Nestre'}

    class Meta:
        model = Produto
        fields = ('desc_produto', 'pontos_produto', 'valor_produto', 'marca_produto',)
        labels = {
            'desc_produto':'Descrição do Produto',
            'pontos_produto': 'Pontos do Produto',
            'valor_produto':'Valor do Produto',
            'marca_produto':'Marca do Produto',
        }

class ServicoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['desc_servico'].widget.attrs = {'class': 'form-group form-control', 'type':'text', 'placeholder':'Corte Padrão'}
        self.fields['pontos_servico'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'666'}
        self.fields['valor_servico'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'R$ 55'}
    class Meta:
        model = Servico
        fields = ('desc_servico', 'pontos_servico', 'valor_servico',)
        labels = {
            'desc_servico': 'Descrição do Serviço',
            'pontos_servico': 'Pontos do Serviço',
            'valor_servico': 'Valor do Serviço',
        }


class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        self.fields['data_reserva'].widget.attrs = {'type':'date', 'class': 'form-group form-control', 'placeholder':'##/##/####'}
        self.fields['hora_reserva'].widget.attrs = {'type':'hour', 'class': 'form-group form-control', 'placeholder':'-:-'}
        self.fields['cliente_reserva'].widget.attrs = {'class': 'form-group form-control'}

    class Meta:
        model = Reserva
        fields = ('data_reserva', 'hora_reserva','cliente_reserva',)
        labels = {
            'data_reserva': 'Data da Reserva',
            'hora_reserva': 'Hora da Reserva',
            'cliente_reserva': 'Cliente',
        }
        widgets = {
            'cliente_reserva': forms.Select(attrs={'class': 'select'}),
            'data_reserva': forms.DateTimeInput(attrs={'type': 'date'}),
        }


class VendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)
        self.fields['cliente_venda'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['servico_venda'].widget.attrs = {'class': 'form-group form-control'}
        self.fields['servico_venda'].queryset=Servico.objects.all()
        self.fields['produto_venda'].queryset=Produto.objects.all()
        self.fields['produto_venda'].widget.attrs = {'class': 'form-group form-control'}

    class Meta:
        model = Venda
        fields = ('cliente_venda', 'servico_venda','produto_venda',)
        labels = {
            'cliente_venda': 'Cliente',
            'servico_venda': 'Serviços',
            'produto_venda': 'Produtos',
        }
        widgets = {
            'cliente_venda': forms.Select(attrs={'class': 'select'}),
        }
