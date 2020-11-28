from django.db import models
from django.utils.translation import ugettext_lazy as _

class RegisterType(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Tipo de Identificação')
        verbose_name_plural = _('Tipos de Identificação')

class PostGraduation(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    seniority = models.ManyToManyField("self",blank=True)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Posto/Graduação')
        verbose_name_plural = _('Postos e Graduações')

class Branch(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    telephone = models.CharField(max_length=4)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Ramal')
        verbose_name_plural = _('Ramais')

class DivisionSession(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20)
    branch = models.ManyToManyField(Branch,blank=True)
    branch_main = models.ForeignKey(
        Branch,
        related_name='branch_main',
        blank=True,
        default = None,
        null=True,
        on_delete=models.CASCADE)
    subordination = models.ManyToManyField("self",blank=True)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Divisão ou Seção')
        verbose_name_plural = _('Divisões e Seções')

class Qualification(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    official_color = models.CharField(max_length=7)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _('Arma/Quadro/Serviço')
        verbose_name_plural = _('Armas/Quadros/Serviços')
