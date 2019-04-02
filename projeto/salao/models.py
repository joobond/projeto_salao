from django.db import models
from django.contrib.auth.models import User

class Cliente (models.Model):
    nome_cliente = models.CharField(max_length=200, null=False)
    telefone_cliente = models.CharField(max_length=12)
    pontos_cliente = models.IntegerField(null=False)
    instagram_cliente = models.CharField(max_length=50)
    bairro_cliente = models.CharField(max_length=200, null=False)
    #ultima_alteracao = models.ForeignKey(User, on_delete=models.CASCADE) #Campo de quem fez a ultima alteração

    def __str__(self):
        return self.nome_cliente

class Produto(models.Model):
    desc_produto = models.CharField(max_length=200, null=False)
    pontos_produto = models.IntegerField(null=False)
    valor_produto = models.FloatField(max_length=12, null=False)
    marca_produto = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.desc_produto

class Servico(models.Model):
    desc_servico = models.CharField(max_length=200, null=False)
    pontos_servico = models.IntegerField(null=False)
    valor_servico = models.FloatField(null=False)

    def __str__(self):
        return self.desc_servico

class Reserva(models.Model):
    data_hora_reserva = models.DateTimeField(null = False)
    cliente_reserva = models.ForeignKey(Cliente,on_delete=models.CASCADE, null = False)

    def __str__(self):
        return self.data_hora_reserva, self.cliente_reserva
