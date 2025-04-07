from django import forms
from .models import Usuario

class RegistroFormulario(forms.ModelForm):
    # Confirmar la contraseña
    contrasena_confirmar = forms.CharField(widget=forms.PasswordInput(), label="Confirmar contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellidos', 'email', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        if len(contrasena) < 6:
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return contrasena

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        contrasena_confirmar = cleaned_data.get('contrasena_confirmar')

        # Comprobar si las contraseñas coinciden
        if contrasena and contrasena_confirmar:
            if contrasena != contrasena_confirmar:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data
