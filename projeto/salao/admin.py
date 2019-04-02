from django.contrib import admin
from .models import  Produto, Cliente, Servico, Reserva

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Reserva)
