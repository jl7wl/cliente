from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(verbose_name ="Nome completo", max_length)
    cpf = models.CharField(verbose_name="CPF", max_length=14)