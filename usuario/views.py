from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UsuarioService
from .serializers import UsuarioPymeSerializer

class RegistroPymeView(APIView):
    def post(self, request):
        try:
            # Enviamos los datos al servicio
            nuevo_usuario = UsuarioService.registrar_pyme(request.data)
            
            # Serializamos la respuesta para devolverla como JSON
            serializer = UsuarioPymeSerializer(nuevo_usuario)
            
            return Response({
                "message": "Empresa registrada con éxito",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)