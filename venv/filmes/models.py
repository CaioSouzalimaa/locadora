from django.db import models

# Create your models here.

from uuid import uuid4

# Create your models here.

class Filmes(models.Model):
    id_filme = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_filme = models.CharField(max_length=255)
    nome_cliente = models.CharField(max_length=255)
    dia_alugado = models.DateField(auto_now_add=True)
    dia_devolver = models.DateField()
    valor = models.FloatField()
