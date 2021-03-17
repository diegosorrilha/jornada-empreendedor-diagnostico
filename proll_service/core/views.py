from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import DiagnosticoForm1


def home(request):
    template_name = 'home.html'
    form = DiagnosticoForm1()

    if request.method == 'POST':
        if request.POST['qtd_venda'] == '0':
            return redirect(reverse('resultado', args=['1']))

    return render(request, template_name, {'form': form})


def resultado(request, etapa):
    ETAPAS = {
        '1': 'Ideaçãosss',
        '2': 'Pré-operação',
        '3': 'Operação',
        '4': 'Tração',
        '5': 'Expansão',
    }
    template_name = 'resultado.html'
    return render(request, template_name, {'nome_etapa': ETAPAS[etapa]})
open
