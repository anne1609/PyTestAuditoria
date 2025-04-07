from unittest import mock
from django.urls import reverse
from django.test import Client
from rest_framework import status
from faker import Faker
import pytest

@pytest.mark.django_db
@mock.patch('usuarios.utils.enviar_datos_a_api')
def test_registro_usuario_y_envio_api(mock_enviar):
    fake = Faker()
    client = Client()

    data = {
        'nombre': fake.first_name(),
        'apellidos': fake.last_name(),
        'email': fake.unique.email(),
        'contrasena': 'Test1234!',
        'contrasena_confirmar': 'Test1234!',
    }

    response = client.post(reverse('registro'), data)

    assert response.status_code == status.HTTP_302_FOUND

    # Asegurar que la función mockeada se haya llamado
    assert mock_enviar.called
    mock_enviar.assert_called_once()
