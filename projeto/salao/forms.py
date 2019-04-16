from django import forms
from salao.models import Cliente, Venda, Reserva, Servico, Produto

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
        self.fields['data_hora_reserva'].widget.attrs = {'class': 'form-group form-control', 'type':'date', 'placeholder':'##/##/##'}
        self.fields['pontos_servico'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'666'}
        self.fields['valor_servico'].widget.attrs = {'class': 'form-group form-control', 'type':'number', 'placeholder':'R$ 55'}
    class Meta:
        model = Reserva
        fields = ('data_hora_reserva', 'cliente_reserva',)
        labels = {
            'data_hora_reserva': 'Data e Horário da Reserva',
            'cliente_reserva': 'Cliente',
        }
