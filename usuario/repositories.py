from .models import UsuarioPyme

class UsuarioRepository:
    @staticmethod
    def crear_usuario(datos: dict) -> UsuarioPyme:
        return UsuarioPyme.objects.create(**datos)

    @staticmethod
    def obtener_por_rut(rut: str) -> UsuarioPyme:
        try:
            return UsuarioPyme.objects.get(rut_empresa=rut)
        except UsuarioPyme.DoesNotExist:
            return None

    @staticmethod
    def listar_todos():
        return UsuarioPyme.objects.filter(activo=True)