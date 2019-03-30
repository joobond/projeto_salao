from django.db import models
from django.contrib.auth.models import User

class Cliente (models.Model):
    nome_cliente = models.CharField(max_length=200, null=False)
    telefone_cliente = models.CharField(max_length=12)
    pontos_cliente = models.IntegerField(max_length=10, null=False)
    instagram_cliente = models.CharField(max_length=50)
    bairro_cliente = models.CharField(max_length=200, null=False)
    #ultima_alteracao = models.ForeignKey(User, on_delete=models.CASCADE) #Campo de quem fez a ultima alteração

class Produto(models.Model):
    desc_produto = models.CharField(max_length=200, null=False)
    pontos_produto = models.IntegerField(max_length=12, null=False)
    valor_produto = models.FloatField(max_length=12, null=False)
    marca_produto = models.CharField(max_length=100, null=False)

class Servico(models.Model):
    desc_servico = models.CharField(max_length=200, null=False)
    pontos_servico = models.IntegerField(max_length=12, null=False)
    valor_servico = models.FloatField(max_length=12, null=False)
    
    
