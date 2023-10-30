from django import forms

# PACIENTE
class RegistroPacienteForm(forms.Form):
    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput())
    
class InicioSesionPacienteForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput())
    
    
# MEDICO
class RegistroMedicoForm(forms.Form):
    rut = forms.CharField(max_length=12)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    especialidad = forms.CharField(max_length=100)
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput())

class InicioSesionMedicoForm(forms.Form):
    email = forms.EmailField()
    contrasena = forms.CharField(widget=forms.PasswordInput())
