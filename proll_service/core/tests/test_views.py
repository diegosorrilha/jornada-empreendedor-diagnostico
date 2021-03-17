import pytest
from django.test import Client
from django.urls import reverse

from ..django_assertions import assert_template_used, assert_contains, assert_is_instance, assert_redirects
from ..forms import DiagnosticoForm1


@pytest.fixture
def resp_home(client: Client):
    resp = client.get(reverse('home'))
    return resp


@pytest.fixture
def resp_resultado(client: Client):
    resp = client.get(reverse('resultado', args=['1']))
    return resp


def test_home_status_code(resp_home):
    resp = resp_home
    assert resp.status_code == 200


def test_home_template_used(resp_home):
    resp = resp_home
    assert_template_used(resp, 'home.html')


def test_home_contains_title(resp_home):
    resp = resp_home
    assert_contains(resp, '<title>Diagnóstico - Jornada do Empreendedor de Startups</title>')
    assert_contains(resp, '>Diagnóstico | Jornada do Empreendedor</h1>')


def test_home_has_form_1_on_context(resp_home):
    resp = resp_home
    assert_is_instance(resp.context['form'], DiagnosticoForm1)


def test_home_redireciona_para_resultado_com_etapa_1_em_caso_de_venda_zero(client: Client):
    data = {'tipo_empresa': 'b2b', 'qtd_venda': '0'}
    resp = client.post(reverse('home'), data)
    assert_redirects(resp, reverse('resultado', args=['1']))


def test_resultado_status_code(resp_resultado):
    resp = resp_resultado
    assert resp.status_code == 200


def test_resultado_template_used(resp_resultado):
    resp = resp_resultado
    assert_template_used(resp, 'resultado.html')


def test_resultado_contains_title(resp_resultado):
    resp = resp_resultado
    assert_contains(resp, '<title>Diagnóstico - Jornada do Empreendedor de Startups | Resultado</title>')
    assert_contains(resp, '>Diagnóstico | Jornada do Empreendedor</h1>')


def test_resultado_exibe_ideacao(client: Client):
    resp = client.get(reverse('resultado', args=['1']))
    assert_contains(resp, 'Resultado: Ideação')
