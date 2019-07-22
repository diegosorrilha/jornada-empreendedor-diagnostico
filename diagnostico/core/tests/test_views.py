from django.test import Client

from ..django_assertions import assert_template_used


def test_home_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_home_template_used(client: Client):
    resp = client.get('/')
    assert_template_used(resp, 'home.html')
