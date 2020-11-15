from django.contrib import admin

from .models import RegisterType, PostGraduation, DivisionSession, Branch

admin.site.register([
    RegisterType,
    PostGraduation,
    DivisionSession,
    Branch,
    ])
