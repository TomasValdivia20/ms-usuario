from .models import UsuarioPyme

class UsuarioRepository:
    @staticmethod
    def crear(datos: dict) -> UsuarioPyme:
        return UsuarioPyme.objects.create(**datos)

    @staticmethod
    def obtener_por_rut(rut: str):
        # Buscamos por RUT y que no esté eliminado
        return UsuarioPyme.objects.filter(rut_empresa=rut, activo=True).first()

    @staticmethod
    def listar_activos():
        return UsuarioPyme.objects.filter(activo=True)

    @staticmethod
    def actualizar(usuario, datos: dict):
        for campo, valor in datos.items():
            setattr(usuario, campo, valor)
        usuario.save()
        return usuario

    @staticmethod
    def eliminar(usuario):
        # Eliminación lógica (Soft Delete)
        usuario.activo = False
        usuario.save()