from django.contrib.auth.hashers import make_password
from .repositories import UsuarioRepository

class UsuarioService:
    @staticmethod
    def crear_usuario(datos: dict):
        if UsuarioRepository.obtener_por_rut(datos.get('rut_empresa')):
            raise ValueError("Ya existe una empresa con este RUT.")
        
        # Encriptamos la clave
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