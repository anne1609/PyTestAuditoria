from django.shortcuts import render, redirect
from .forms import RegistroFormulario
from .models import Usuario  # Asegúrate de importar tu modelo personalizado

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
