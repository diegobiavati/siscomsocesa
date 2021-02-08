from django.db import models

# Create your models here.
class Beneficiario(models.Model):
    nome = models.CharField(max_length=250)
    nascimento = models.DateField()
    preccp = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    slug = models.SlugField()
    status = models.BooleanField()