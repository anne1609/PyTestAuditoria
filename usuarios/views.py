from django.shortcuts import render, redirect
from .forms import RegistroFormulario
from .models import Usuario  # Asegúrate de importar tu modelo personalizado
from .utils import enviar_datos_a_api
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            # Crear usuario con la información proporcionada
            usuario = form.save(commit=False)
            # Usar el método set_contrasena para cifrar la contraseña antes de guardar
            usuario.set_contrasena(form.cleaned_data['contrasena'])
            usuario.save()
            return redirect('registro_exitoso')  # Redirección a la página de éxito
    else:
        form = RegistroFormulario()

    return render(request, 'usuarios/registro.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')


def vista_registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        contrasena_confirmar = request.POST.get('contrasena_confirmar')

        if contrasena == contrasena_confirmar:
            # Simula crear un usuario aquí (puedes usar create_user o guardar en DB)
            usuario_data = {
                'nombre': nombre,
                'apellidos': apellidos,
                'email': email
            }

            enviar_datos_a_api(usuario_data) 

            return redirect('home')  