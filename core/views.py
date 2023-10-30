from django.shortcuts import render, redirect
from .forms import RegistroPacienteForm, InicioSesionPacienteForm, RegistroMedicoForm, InicioSesionMedicoForm
import requests

# INDEX
def pagina_bienvenida(request):
    return render(request, 'bienvenida.html')

def seleccionar_perfil(request):
    return render(request,'seleccionar_perfil.html')

# PACIENTE
def registro_paciente(request):
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            data = {
                "rut": form.cleaned_data['rut'],
                "nombre": form.cleaned_data['nombre'],
                "apellido": form.cleaned_data['apellido'],
                "edad": form.cleaned_data['edad'],
                "email": form.cleaned_data['email'],
                "contrasena": form.cleaned_data['contrasena']
            }
            
            api_url = 'https://arquitectura.sabravo.repl.co/api/paciente'  # Reemplaza con la URL de tu API de Flask
            response = requests.post(api_url, json=data)
            
            if response.status_code == 201:
                return redirect('inicio_sesion_paciente')  # Redirige a la página de inicio de sesión
            else:
                form.add_error(None, "Error en el registro. Por favor, inténtalo de nuevo.")
    else:
        form = RegistroPacienteForm()

    return render(request, 'registro_paciente.html', {'form': form})

def inicio_sesion_paciente(request):
    if request.method == 'POST':
        form = InicioSesionPacienteForm(request.POST)
        if form.is_valid():
            data = {
                "email": form.cleaned_data['email'],
                "contrasena": form.cleaned_data['contrasena']
            }
            
            api_url = 'https://arquitectura.sabravo.repl.co/api/login/paciente'  # Reemplaza con la URL de tu API de Flask
            response = requests.post(api_url, json=data)
            
            if response.status_code == 200:
                return redirect('inicio_paciente')  # Redirige a la página de inicio de sesión
            else:
                form.add_error(None, "Credenciales inválidas. Por favor, inténtalo de nuevo.")
    else:
        form = InicioSesionPacienteForm()
        
    return render(request, 'inicio_sesion_paciente.html', {'form': form})

def inicio_paciente(request):
    return render(request, 'inicio_paciente.html')


# MEDICO
def registro_medico(request):
    if request.method == 'POST':
        form = RegistroMedicoForm(request.POST)
        if form.is_valid():
            data = {
                "rut": form.cleaned_data['rut'],
                "nombre": form.cleaned_data['nombre'],
                "apellido": form.cleaned_data['apellido'],
                "edad": form.cleaned_data['edad'],
                "especialidad": form.cleaned_data['especialidad'],
                "email": form.cleaned_data['email'],
                "contrasena": form.cleaned_data['contrasena']
            }
            
            api_url = 'https://arquitectura.sabravo.repl.co/api/medico'  # Reemplaza con la URL de tu API de Flask
            response = requests.post(api_url, json=data)
            
            if response.status_code == 201:
                return redirect('inicio_sesion_medico')  # Redirige a la página de inicio de médico
            else:
                form.add_error(None, "Error en el registro. Por favor, inténtalo de nuevo.")
    else:
        form = RegistroMedicoForm()

    return render(request, 'registro_medico.html', {'form': form})

def inicio_sesion_medico(request):
    if request.method == 'POST':
        form = InicioSesionMedicoForm(request.POST)
        if form.is_valid():
            data = {
                "email": form.cleaned_data['email'],
                "contrasena": form.cleaned_data['contrasena']
            }
            
            api_url = 'https://arquitectura.sabravo.repl.co/api/login/medico'  # Reemplaza con la URL de tu API de Flask
            response = requests.post(api_url, json=data)
            
            if response.status_code == 200:
                return redirect('inicio_medico')  # Redirige a la página de inicio de médico
            else:
                form.add_error(None, "Credenciales inválidas. Por favor, inténtalo de nuevo.")
    else:
        form = InicioSesionMedicoForm()

    return render(request, 'inicio_sesion_medico.html', {'form': form})

def inicio_medico(request):
    return render(request, 'inicio_medico.html')