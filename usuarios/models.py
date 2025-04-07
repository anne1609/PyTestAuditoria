from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    def set_contrasena(self, contrasena):
        # Utiliza make_password para cifrar la contraseña
        self.contrasena = make_password(contrasena)

    def check_contrasena(self, contrasena):
        # Verifica si la contraseña introducida coincide con la almacenada
        from django.contrib.auth.hashers import check_password
        return check_password(contrasena, self.contrasena)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
