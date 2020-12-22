from django.contrib import admin

from .models import RegisterType, PostGraduation, DivisionSession, Branch, Qualification

'''Model Branch'''
@admin.register(Branch)
class Branch(admin.ModelAdmin):
    list_display = (
        'name',
        'abbreviation',
        'telephone',
        'activate'
        )
    list_filter = (
        'activate',
        )
    search_fields = (
        'name',
        'abbreviation',
        'telephone',
        )

'''Model DivisionSession'''
@admin.register(DivisionSession)
class DivisionSession(admin.ModelAdmin):
    list_display = (
        'name',
        'abbreviation',
        'subunit',
        'echelon',
        'activate'
    )
    list_filter = (
        'subunit',
        'echelon',
        'activate',
    )
    search_fields = (
        'name',
        'abbreviation',
        )

@admin.register(PostGraduation)
class PostGraduation(admin.ModelAdmin):
    list_display = (
        'name',
        'abbreviation',
        'activate',
        )
    list_filter = (
        'activate',
        'seniority',
    )
    search_fields = (
        'name',
        'abbreviation',
        )

@admin.register(Qualification)
class Qualification(admin.ModelAdmin):
    list_display = (
        'name',
        'abbreviation',
        'activate',
        )
    list_filter = (
        'activate',
    )
    search_fields = (
        'name',
        'abbreviation'
        )

@admin.register(RegisterType)
class RegisterType(admin.ModelAdmin):
    list_display = (
        'name',
        'abbreviation',
        'activate',
        )
    list_filter = (
        'activate',
    )
    prepopulated_fields = {"slug": ("name",)}
    search_fields = (
        'name',
        'abbreviation',
        )