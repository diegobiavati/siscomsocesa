from django.contrib import admin

from .models import RegisterType, PostGraduation, DivisionSession, Branch, Qualification

admin.site.register([
    RegisterType,
    PostGraduation,
    DivisionSession,
    Branch,
    Qualification
    ])
