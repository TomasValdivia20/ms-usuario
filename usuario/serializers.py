#transformar los datos a json y viceversa
from rest_framework import serializers
from .models import UsuarioPyme

class UsuarioPymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPyme
        fields = [
            'id', 'rut_empresa', 'razon_social', 'nombre_empresa', 
            'email', 'telefono', 'direccion', 'codigo_sii', 'activo'
        ]
        # La contraseña nunca se envía de vuelta en un GET por seguridad
        extra_kwargs = {'password': {'write_only': True}}