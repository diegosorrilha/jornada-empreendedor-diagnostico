import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse

from proll_service.core.models import Establishment, Assessment

logger = logging.getLogger(__name__)

def get_establishments():
    establishments = Establishment.objects.all()

    return establishments




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


def save_data(request):
    # User.evaluated_items

    # Assessment.id
    # Assessment.created_at
    # Assessment.evaluator # User.id
    # Assessment.establishment_id # Establishment.id
    # Assessment.room
    # Assessment.evaluated_items

    # Establishment.id
    # Establishment.name


    evaluated_items = {
        'Teto': 'conforme',
        'Luminária': 'não se aplica',
        'Luz': 'não conforme',
        'photo_Luz': 'base64'
    }

    for k, v in evaluated_items.items():
        if not k.startswith('photo'):
            print(f'{k}: {v}')

    print('================')

    print(f'vai salvar data {request.POST}')

    print('================')

    return JsonResponse({'message': "Updated with SUCCESS"}, status=200)


def home(request):
    logger.info('iniciando')
    print('iniciando')


    template_name = 'home.html'

    assessment = Assessment.objects.last()

    establishments = get_establishments()
    items = get_items()

    if request.method == 'POST':
        print(request.POST)

    print(request.GET)


    # form = DiagnosticoForm1()
    # return render(request, template_name, {'form': form})

    return render(request, template_name, {
        'assessment': assessment,
        'items': items,
        'establishments': establishments
    })
