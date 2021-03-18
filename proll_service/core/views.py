import logging

from django.shortcuts import render, redirect
from django.urls import reverse

# from .forms import DiagnosticoForm1

logger = logging.getLogger(__name__)


def get_items():
    items = {
        'Quarto': [
            'Teto',
            'Luminária',
            'Luz de emergência',
            'Detector de incêndio',
            'Saídas de ar',
            'Cano',
            'Ar condicionado',
            'Paredes e divisórias',
            'Ventilador',
            'Cortinas/biombo',
            'Cano Hidráulico',
            'Câmera',
            'Interruptor de luz e campainha',
            'Vidros',
            'Esquadrias',
            'Grades',
            'Porta (batente, maçanetas, saídas de ar)',
            'Eletrônicos (telefone, TV e outros)',
            'Régua de gases',
            'Quadro de força',
            'Placas',
            'Extintor de incêndio',
            'Dispensadores',
            'Lavatório',
            'Prateleira',
            'Quadro',
            'Piso',
            'Mobiliários',
            'Mesa de refeição',
            'Criado-mudo',
            'Escada',
            'Cama (grades, pés, colchão)',
            'Poltrona',
            'Rodapé',

        ],
        'Banheiro': [
            'Teto',
            'Saída de ar',
            'Luminária',
            'Pared',
            'Rejuntes',
            'Chuveiro',
            'Dispensadores (papel, sabonete e álcool em gel)',
            'Pia',
            'Torneira',
            'Sifão',
            'Porta (batente, maçanetas, saídas de ar)',
            'Piso',
            'Rodapé',
            'Ralo',
            'Lixeira',
        ],
    }

    return items


def home(request):
    logger.info('iniciando')
    print('iniciando')
    template_name = 'home.html'
    items = get_items()

    if request.method == 'POST':
        print(request.POST)

    print(request.GET)


    # form = DiagnosticoForm1()
    # return render(request, template_name, {'form': form})

    return render(request, template_name, {'items': items})
