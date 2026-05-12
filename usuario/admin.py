from django.contrib import admin
from .models import UsuarioPyme

@admin.register(UsuarioPyme)
class UsuarioPymeAdmin(admin.ModelAdmin):
    list_display = ('rut_empresa', 'nombre_empresa', 'email', 'codigo_sii')
    search_fields = ('rut_empresa', 'nombre_empresa')