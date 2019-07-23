from django.shortcuts import render

from .forms import DiagnosticoForm1


def home(request):
    template_name = 'home.html'
    form = DiagnosticoForm1()
    return render(request, template_name, {'form': form})


def resultado(request):
    template_name = 'resultado.html'
    return render(request, template_name)
