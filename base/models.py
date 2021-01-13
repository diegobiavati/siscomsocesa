from django.db import models
from django.utils.translation import ugettext_lazy as _

class RegisterType(models.Model):
    """
    Stores a single documentation type.
    """
    abbreviation = models.CharField(
        max_length=10,
        help_text="Abbreviation name of the RegisterType.",
        )
    activate = models.BooleanField(
        default=True,
        help_text="Activate and Deactivate RegisterType.",
        )
    name = models.CharField(
        max_length=100,
        help_text="Name of the RegisterType.",
        )
    slug = models.SlugField(
        unique=True,
        help_text="slug URL of the RegisterType.",
        )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Tipo de Identificação')
        verbose_name_plural = _('Tipos de Identificação')

class PostGraduation(models.Model):
    abbreviation = models.CharField(
        max_length=10,
        help_text="",
        )
    activate = models.BooleanField(
        default=True,
        help_text="",
        )
    name = models.CharField(
        max_length=100,
        help_text="Name of the Post & Graduation.",
        )
    seniority = models.ManyToManyField(
        "self",
        blank=True,
        )
    slug = models.SlugField(
        unique=True,
        help_text="slug URL of the Post & Graduation.",
        )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Posto/Graduação',)
        verbose_name_plural = _('Postos e Graduações',)

class Branch(models.Model):
    abbreviation = models.CharField(
        max_length=20,
        help_text=".",
        )
    activate = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        help_text=".",
        )
    telephone = models.CharField(
        max_length=4,
        help_text=".",
        )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Ramal',)
        verbose_name_plural = _('Ramais',)

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
    echelon = models.BooleanField(default=False)
    subunit = models.BooleanField(default=False)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Divisão ou Seção',)
        verbose_name_plural = _('Divisões e Seções',)

class Qualification(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    official_color = models.CharField(max_length=7)
    activate = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('activate',)
        verbose_name = _('Arma/Quadro/Serviço',)
        verbose_name_plural = _('Armas/Quadros/Serviços',)
