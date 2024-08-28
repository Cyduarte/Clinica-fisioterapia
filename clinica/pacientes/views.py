from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def cadastro_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/cadastro.html', {'form': form})

def listagem_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listagem.html', {'pacientes': pacientes})

def index(request):
    return render(request, 'pacientes/index.html')
