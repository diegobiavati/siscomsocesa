from django.contrib import admin
from .models import Beneficiario,Procedimento,OcsPsa,Atendimento

# Register your models here.
@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nome','preccp','status')
    search_fields = ('nome','preccp','cpf')
    list_filter = ('status',)

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome','codigo','status')
    search_fields = ('nome','codigo')
    list_filter = ('status',)

@admin.register(OcsPsa)
class OcsPsaAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','email','status')
    search_fields = ('nome','telefone','email')
    list_filter = ('status',)

@admin.register(Atendimento)
class Atendimento(admin.ModelAdmin):
    list_display = ('id','data','status')
    search_fields = ('data','id')
    list_filter = ('status',)