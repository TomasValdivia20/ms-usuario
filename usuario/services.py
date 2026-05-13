from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from .repositories import UsuarioRepository
from .models import UsuarioPyme
from .validators import validar_rut_chileno

class UsuarioService:
    @staticmethod
    def crear_usuario(datos: dict):
        rut_entrante = datos.get('rut_empresa', '')

        # 1. ¡NUEVO! Pasamos el RUT por el escáner chileno antes de hacer nada
        try:
            validar_rut_chileno(rut_entrante)
        except ValidationError as e:
            # Si el RUT es falso, lanzamos un ValueError para que la vista devuelva un Error 400 al Front
            raise ValueError(e.messages[0])

        # 2. Verificamos si ya existe en la base de datos
        if UsuarioRepository.obtener_por_rut(rut_entrante):
            raise ValueError("Ya existe una empresa con este RUT.")
        
        # 3. Encriptamos la clave
        if 'password' in datos:
            datos['password'] = make_password(datos['password'])
            
        return UsuarioRepository.crear(datos)

    @staticmethod
    def obtener_usuario(rut: str):
        usuario = UsuarioRepository.obtener_por_rut(rut)
        if not usuario:
            raise ValueError("Usuario no encontrado.")
        return usuario

    @staticmethod
    def listar_usuarios():
        return UsuarioRepository.listar_activos()

    @staticmethod
    def actualizar_usuario(rut: str, datos: dict):
        usuario = UsuarioService.obtener_usuario(rut)
        
        # Protegemos campos que NO se deben cambiar por actualización
        datos.pop('rut_empresa', None)
        datos.pop('password', None) 
        
        return UsuarioRepository.actualizar(usuario, datos)

    @staticmethod
    def eliminar_usuario(rut: str):
        usuario = UsuarioService.obtener_usuario(rut)
        UsuarioRepository.eliminar(usuario)
    
    @staticmethod
    def validar_credenciales(email: str, password_plana: str):
        # 1. Buscamos al usuario por correo
        usuario = UsuarioPyme.objects.filter(email=email, activo=True).first()
        if not usuario:
            raise ValueError("Credenciales inválidas")
        
        # 2. check_password compara el texto plano con el hash guardado en SQLite
        if not check_password(password_plana, usuario.password):
            raise ValueError("Credenciales inválidas")
            
        return usuario