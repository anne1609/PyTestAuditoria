import pytest
from django.urls import reverse
from usuarios.models import Usuario  
from rest_framework import status
from django.test import Client

@pytest.mark.django_db
def test_usuario_registro():
    # Crear cliente de pruebas
    client = Client()
    
   
    data = {
        'nombre': 'Test',
        'apellidos': 'User',
        'email': 'testuser@example.com',
        'contrasena': 'TestPassword123',
        'contrasena_confirmar': 'TestPassword123',  
    }
    
    # Hacer una solicitud POST a la vista de registro
    response = client.post(reverse('registro'), data)
    
    # Verificar que la respuesta fue exitosa (redirección a la página de éxito)
    assert response.status_code == status.HTTP_302_FOUND  # Redirección a la página de éxito
    
    # Verificar que el usuario se haya creado en la base de datos
    user = Usuario.objects.get(email='testuser@example.com')  # Usar Usuario en lugar de get_user_model()
    assert user.nombre == 'Test'
    assert user.apellidos == 'User'
    assert user.email == 'testuser@example.com'
    assert user.check_contrasena('TestPassword123')  # Verificar que la contraseña es válida
