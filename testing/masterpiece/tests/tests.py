import pytest
from django.shortcuts import reverse
from masterpiece.models import Masterpiece
from masterpiece.forms import MasterpieceModelForm


def test_listview_get_test(client, access_db, create_obj):
    resp = client.get(
        reverse('list')
    )
    assert resp.context_data['object_list'][0].name == 'Creation of Adam'
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


def test_createview_post_test(client, access_db):
    resp = client.post(
        reverse('create'),
        data={'name': 'Creation of Adam', 'author': 'Michelangelo', 'price': '100.99'}
    )
    assert resp.status_code == 302
    obj = Masterpiece.objects.first()
    assert isinstance(obj, Masterpiece)
    assert resp.url == reverse('list')


@pytest.mark.parametrize(
    'api_resp,result', [('{"data":[["jade","Satou","Accountant","Tokyo","28th Nov 08","$162,700"]]}','jadeSatou'),('{"data":[["jozz","Satou","Accountant","Tokyo","28th Nov 08","$162,700"]]}','jozzSatou')]
)
def test_buyer_list_view(api_resp, result, client, access_db, requests_mock):
    requests_mock.get('https://bit.ly/2nkSGF1', text=api_resp)
    resp = client.get(
        reverse('buyer-list')
    )
    assert resp.status_code == 200
    assert resp.context_data['object_list'][0].name == result
