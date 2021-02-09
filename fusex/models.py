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
    def __str__(self):
        return self.nome

class Procedimento(models.Model):
    nome = models.CharField(max_length=250)
    codigo = models.CharField(max_length=10)
    #ocs_psa = models.ManyToManyField(OcsPsa)
    valor = models.IntegerField()
    slug = models.SlugField()
    status = models.BooleanField()
    def __str__(self):
        return self.nome

class OcsPsa(models.Model):
    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    procedimentos = models.ManyToManyField(Procedimento)
    slug = models.SlugField()
    status = models.BooleanField()
    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    beneficiario = models.ForeignKey(Beneficiario,on_delete=models.CASCADE)
    data = models.DateField()
    procedimento = models.ManyToManyField(Procedimento)
    slug = models.SlugField()
    status = models.BooleanField()
    def __str__(self):
        return self.beneficiario.nome