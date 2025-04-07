import pytest
from django.urls import reverse
from usuarios.models import Usuario
from rest_framework import status
from django.test import Client
from faker import Faker

@pytest.mark.django_db
def test_usuario_registro_con_faker():
    # Crear instancia de Faker
    fake = Faker()

    # Crear cliente de pruebas
    client = Client()
    
    # Crear 8 usuarios con datos aleatorios generados por Faker
    for _ in range(3):
        # Generar una contraseña y un email único
        contrasena = fake.unique.password(length=7)  # Contraseña aleatoria de 12 caracteres
        email = fake.unique.email()  # Asegura que el email sea único
        
        # Crear los datos del usuario
        data = {
            'nombre': fake.first_name(),
            'apellidos': fake.last_name(),
            'email': email,
            'contrasena': contrasena,
            'contrasena_confirmar': contrasena,
        }

        # Hacer una solicitud POST a la vista de registro
        response = client.post(reverse('registro'), data)
        
        # Verificar que la respuesta fue exitosa (redirección a la página de éxito)
        assert response.status_code == status.HTTP_302_FOUND  # Redirección a la página de éxito
        
        # Verificar que el usuario se haya creado en la base de datos
        user = Usuario.objects.get(email=email)  # Usar email del usuario creado
        assert user.nombre == data['nombre']
        assert user.apellidos == data['apellidos']
        assert user.email == data['email']
        assert user.check_contrasena(data['contrasena'])  # Verificar que la contraseña es válida
