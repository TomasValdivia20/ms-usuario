from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UsuarioService
from .serializers import UsuarioPymeSerializer

class UsuarioListCreateView(APIView):
    # GET /api/usuario/ -> Lista todos
    def get(self, request):
        usuarios = UsuarioService.listar_usuarios()
        return Response(UsuarioPymeSerializer(usuarios, many=True).data)

    # POST /api/usuario/ -> Crea uno nuevo
    def post(self, request):
        try:
            usuario = UsuarioService.crear_usuario(request.data)
            return Response(UsuarioPymeSerializer(usuario).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 🛡️ Esto evita que Django escupa HTML cuando hay un error grave
            return Response(
                {"error": f"Error interno en MS-Usuario: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UsuarioDetailView(APIView):
    # GET /api/usuario/<rut>/ -> Trae un usuario específico
    def get(self, request, rut):
        try:
            usuario = UsuarioService.obtener_usuario(rut)
            return Response(UsuarioPymeSerializer(usuario).data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    # PATCH /api/usuario/<rut>/ -> Actualiza datos
    def patch(self, request, rut):
        try:
            usuario = UsuarioService.actualizar_usuario(rut, request.data)
            return Response(UsuarioPymeSerializer(usuario).data)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /api/usuario/<rut>/ -> Desactiva al usuario
    def delete(self, request, rut):
        try:
            UsuarioService.eliminar_usuario(rut)
            return Response({"mensaje": "Usuario desactivado correctamente."})
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)