import pytest
from django.shortcuts import reverse
from .models import Masterpiece
from .forms import MasterpieceModelForm


@pytest.mark.django_db
def test_masterpiece_listview():
    obj = Masterpiece.objects.create(
        name='Creation of Adam',
        author='Michelangelo',
        price='100.99'
    )
    assert obj


def test_listview_get_test(client):
    resp = client.get(
        reverse('list')
    )
    assert resp.status_code == 200


def test_modelform_test():
    data = MasterpieceModelForm(
        data={
            'name': 'Creation of Adam',
            'author': 'Michelangelo',
            'price': '100.99',
        }
    )
    assert data.is_valid()


def test_createview_get_test(client):
    resp = client.get(reverse('create'))
    assert resp.status_code == 200
    assert isinstance(resp.context_data.get('form'), MasterpieceModelForm)


@pytest.mark.django_db
def test_createview_post_test(client):
    resp = client.post(
        reverse('create'),
        data={'name': 'Creation of Adam', 'author': 'Michelangelo', 'price': '100.99'}
    )
    assert resp.status_code == 302
    obj = Masterpiece.objects.first()
    assert isinstance(obj, Masterpiece)
    assert resp.url == reverse('list')
