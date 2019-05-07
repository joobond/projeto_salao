from django.db import models
from django.contrib.auth.models import User
from datetime import date
import json

class Cliente (models.Model):
    nome_cliente = models.CharField(max_length=200, null=False)
    telefone_cliente = models.CharField(max_length=12)
    instagram_cliente = models.CharField(max_length=50)
    bairro_cliente = models.CharField(max_length=200, null=False)
    #ultima_alteracao = models.ForeignKey(User, on_delete=models.CASCADE) #Campo de quem fez a ultima alteração

    def __str__(self):
        return self.nome_cliente

    @property
    def pontos_cliente(self):
        pontos = 0
        vendas = self.venda_set.all()
        for x in vendas:
            pontos += x.soma_pontos_venda
        return pontos

    @property
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)


class Produto(models.Model):
    desc_produto = models.CharField(max_length=200, null=False)
    pontos_produto = models.IntegerField(null=False)
    valor_produto = models.FloatField(max_length=12, null=False)
    marca_produto = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.desc_produto

    @property
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)

class Servico(models.Model):
    desc_servico = models.CharField(max_length=200, null=False)
    pontos_servico = models.IntegerField(null=False)
    valor_servico = models.FloatField(null=False)

    def __str__(self):
        return self.desc_servico

    @property
    def toJSON(self):
        return json.dumps(self, default=lambda x: x.__dict__)

class Reserva(models.Model):
    data_reserva = models.DateField(null = False, default=date.today())
    hora_reserva = models.TimeField(null = False, default='00:00:00')
    cliente_reserva = models.ForeignKey(Cliente,on_delete=models.CASCADE, null = False)


    def __str__(self):
        return str(self.data_reserva) + ":" +str(self.cliente_reserva)

class Venda(models.Model):
    data_hora_venda = models.DateTimeField(auto_now_add=True)
    cliente_venda = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    servico_venda = models.ManyToManyField(Servico, blank=True)
    produto_venda = models.ManyToManyField(Produto, blank=True)


    def __str__(self):
        return str(self.cliente_venda) + ":" + str(self.data_hora_venda) + "- PontosG: " + str(self.soma_pontos_venda)


    @property
    def soma_pontos_venda(self):
        pontos = 0
        if self.servico_venda:
            for x in self.servico_venda.all():
                pontos = pontos + x.pontos_servico

        if self.produto_venda:
            for x in self.produto_venda.all():
                pontos = pontos + x.pontos_produto
        return pontos



    #Fazer Função de somatória de pontos