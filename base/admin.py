from django.contrib import admin

from .models import RegisterType, PostGraduation, DivisionSession, Branch, Qualification

admin.site.register([
    DivisionSession,
    Branch,
    Qualification
    ])

@admin.register(RegisterType)
@admin.register(PostGraduation)

class RegisterType(admin.ModelAdmin):
    list_display = ('name','abbreviation','activate')
    search_fields = ('name','abbreviation',)

class PostGraduation(admin.ModelAdmin):
    list_display = ('name','abbreviation','activate')
