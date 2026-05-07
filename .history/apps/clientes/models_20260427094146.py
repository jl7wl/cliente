from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(verbose_name ="Nome completo", max_length=100)
    cpf = models.CharField(verbose_name="CPF", max_length=14)
    telefone = models.Charfield(verbose_name="Telefone", max_length=14)
    nascimento = models.DateField(verbose_name=""