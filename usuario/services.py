#Logica de negocios
from django.contrib.auth.hashers import make_password
from .repositories import UsuarioRepository

class UsuarioService:
    @staticmethod
    def registrar_pyme(datos: dict):
        # 1. Validar si el RUT ya existe
        rut = datos.get('rut_empresa')
        if UsuarioRepository.obtener_por_rut(rut):
            raise ValueError(f"La empresa con RUT {rut} ya está registrada.")
        
        #SEGURIDAD: HASHEO DE CONTRASEÑA 
        raw_password = datos.get('password')
        if raw_password:
            datos['password'] = make_password(raw_password)
            
        # 3. Guardar a través del repositorio
        return UsuarioRepository.crear_usuario(datos)