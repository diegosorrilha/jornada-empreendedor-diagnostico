import pytest
from django.test import Client
from django.urls import reverse

from ..django_assertions import assert_template_used, assert_contains


@pytest.fixture
def resp_home(client: Client):
    resp = client.get(reverse('home'))
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
