from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import UsuarioPyme
from .services import UsuarioService
from .validators import validar_rut_chileno


class ValidadorRUTTestCase(TestCase):
    def test_rut_valido_no_levanta_error(self):
        validar_rut_chileno('76402786-8')

    def test_rut_invalido_levanta_validation_error(self):
        with self.assertRaises(ValidationError):
            validar_rut_chileno('12345678-0')


class UsuarioServiceTestCase(TestCase):
    def setUp(self):
        self.usuario_data = {
            'rut_empresa': '76402786-8',
            'razon_social': 'Pyme Prueba S.A.',
            'nombre_empresa': 'Pyme Prueba',
            'email': 'contacto@pymeprueba.cl',
            'telefono': '+56912345678',
            'direccion': 'Av. Siempre Viva 123',
            'codigo_sii': '4711100',
            'password': 'MiClaveSegura123!',
        }
        self.usuario = UsuarioService.crear_usuario(self.usuario_data.copy())

    def test_crear_usuario_guarda_usuario_activo(self):
        usuario = UsuarioPyme.objects.get(rut_empresa='76402786-8')
        self.assertTrue(usuario.activo)
        self.assertEqual(usuario.email, self.usuario_data['email'])
        self.assertNotEqual(usuario.password, self.usuario_data['password'])

    def test_obtener_usuario_devuelve_usuario_existente(self):
        usuario = UsuarioService.obtener_usuario('76402786-8')
        self.assertEqual(usuario.razon_social, self.usuario_data['razon_social'])

    def test_actualizar_usuario_cambia_campos_permitidos(self):
        update_data = {
            'razon_social': 'Pyme Actualizada S.A.',
            'telefono': '+56987654321',
            'password': 'NuevaClave123!'
        }
        usuario = UsuarioService.actualizar_usuario('76402786-8', update_data)
        self.assertEqual(usuario.razon_social, update_data['razon_social'])
        self.assertEqual(usuario.telefono, update_data['telefono'])
        self.assertTrue(usuario.check_password(update_data['password']) if hasattr(usuario, 'check_password') else usuario.password != update_data['password'])

    def test_eliminar_usuario_desactiva_usuario(self):
        UsuarioService.eliminar_usuario('76402786-8')
        usuario = UsuarioPyme.objects.filter(rut_empresa='76402786-8').first()
        self.assertIsNotNone(usuario)
        self.assertFalse(usuario.activo)

    def test_validar_credenciales_contrasena_correcta(self):
        usuario = UsuarioService.validar_credenciales(self.usuario_data['email'], self.usuario_data['password'])
        self.assertEqual(usuario.rut_empresa, self.usuario_data['rut_empresa'])

    def test_validar_credenciales_contrasena_incorrecta_levanta_error(self):
        with self.assertRaises(ValueError):
            UsuarioService.validar_credenciales(self.usuario_data['email'], 'ClaveIncorrecta')

    def test_crear_usuario_con_rut_invalido_levanta_value_error(self):
        datos = self.usuario_data.copy()
        datos['rut_empresa'] = '12345678-0'
        with self.assertRaises(ValueError):
            UsuarioService.crear_usuario(datos)

    def test_listar_usuarios_devuelve_activos(self):
        usuarios = UsuarioService.listar_usuarios()
        self.assertEqual(len(usuarios), 1)
        UsuarioService.eliminar_usuario('76402786-8')
        usuarios_despues = UsuarioService.listar_usuarios()
        self.assertEqual(len(usuarios_despues), 0)
