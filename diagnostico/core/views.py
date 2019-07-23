from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DiagnosticoForm1


def home(request):
    template_name = 'home.html'
    form = DiagnosticoForm1()

    if request.method == 'POST':
        return redirect(reverse('resultado', args=[0]))

    return render(request, template_name, {'form': form})


def resultado(request, id_etapa):
    template_name = 'resultado.html'
    return render(request, template_name)
