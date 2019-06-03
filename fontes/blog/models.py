import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    produto_nome = models.CharField(max_length=20)
    produto_descricao = models.TextField(default = "Insira aqui  a descricao do produto",max_length=300)
    data_cadastro = models.DateTimeField('Data de entrada no estoque:')

    def __str__(self):
        return self.produto_nome