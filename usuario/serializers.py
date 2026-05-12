#transformar los datos a json y viceversa
from rest_framework import serializers
from .models import UsuarioPyme

class UsuarioPymeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPyme
        fields = '__all__' # llama todos los campos del modelo
        # Ocultamos la contraseña al hacer GET por seguridad
        extra_kwargs = {'password': {'write_only': True}}