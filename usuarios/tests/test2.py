import pytest
from django.urls import reverse
from usuarios.models import Usuario
from rest_framework import status
from django.test import Client
from faker import Faker

@pytest.mark.django_db
def test_usuario_registro():
    
    fake = Faker()


    client = Client()


    nombre = fake.first_name()
    apellidos = fake.last_name()
    email = fake.email()
    contrasena = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

    data = {
        'nombre': nombre,
        'apellidos': apellidos,
        'email': email,
        'contrasena': contrasena,
        'contrasena_confirmar': contrasena,
    }

    # Hacer una solicitud POST a la vista de registro
    response = client.post(reverse('registro'), data)

    # Verificar que la respuesta fue exitosa (redirección a la página de éxito)
    assert response.status_code == status.HTTP_302_FOUND  # Redirección a la página de éxito

    # Verificar que el usuario se haya creado en la base de datos
    user = Usuario.objects.get(email=email)  # Usar el email generado para buscar el usuario
    assert user.nombre == nombre
    assert user.apellidos == apellidos
    assert user.email == email
    assert user.check_contrasena(contrasena)  # Verificar que la contraseña es válida
