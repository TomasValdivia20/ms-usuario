from django.urls import path
from .views import RegistroPymeView

urlpatterns = [
    # URL final: http://localhost:PORT/api/usuario/registro/
    path('registro/', RegistroPymeView.as_view(), name='registro-pyme'),
]