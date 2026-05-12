from django.urls import path
from .views import UsuarioListCreateView, UsuarioDetailView

urlpatterns = [
    # Si entran a /api/usuario/
    path('', UsuarioListCreateView.as_view(), name='usuario-list'),
    
    # Si entran a /api/usuario/76123456-K/
    path('<str:rut>/', UsuarioDetailView.as_view(), name='usuario-detail'),
]