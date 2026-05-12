from django.urls import path
from .views import UsuarioListCreateView, UsuarioDetailView,ValidarCredencialesView

urlpatterns = [
    path('', UsuarioListCreateView.as_view(), name='usuario-list'),
    #Vamos a agregar esta nueva ruta para validar credenciales
    path('validar-credenciales/', ValidarCredencialesView.as_view(), name='validar-credenciales'), 
    # Esta ruta es para operaciones sobre un usuario específico, usando su RUT como identificador
    path('<str:rut>/', UsuarioDetailView.as_view(), name='usuario-detail'),
]