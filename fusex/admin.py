from django.contrib import admin
from .models import Beneficiario

# Register your models here.
@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    pass