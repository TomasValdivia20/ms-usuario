from django.db import models
import re
from .validators import validar_rut_chileno

class RolUsuario(models.TextChoices):
    ADMIN = 'Admin', 'Administrador'
    PYME = 'Pyme', 'Empresa Cliente'
    BODEGUERO = 'Bodeguero', 'Bodeguero'


class UsuarioPyme(models.Model):
    # Identificadores únicos
    rut_empresa = models.CharField(max_length=12, unique=True, validators=[validar_rut_chileno], verbose_name="RUT de la Empresa")
    razon_social = models.CharField(max_length=200, verbose_name="Razón Social")
    nombre_empresa = models.CharField(max_length=200, verbose_name="Nombre Fantasía")
    
    # Datos de contacto
    email = models.EmailField(unique=True, verbose_name="Correo Principal")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono de Contacto")
    direccion = models.CharField(max_length=255, verbose_name="Dirección Principal")
    
    # Datos de negocio
    codigo_sii = models.CharField(max_length=10, verbose_name="Código Actividad SII")
    
    # Seguridad (Se guarda el hash enviado por ms-login o texto plano según tu flujo)
    password = models.CharField(max_length=128)
    
    # Roles y permisos
    rol = models.CharField(max_length=20, choices=RolUsuario.choices, default=RolUsuario.PYME)
    # Auditoría
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_empresa} ({self.rut_empresa})"

    class Meta:
        verbose_name = "Usuario PYME"
        verbose_name_plural = "Usuarios PYME"
        
