import pytest
from masterpiece.models import Masterpiece


@pytest.fixture
def access_db(db):
    pass


@pytest.fixture(scope='module')
def create_obj(django_db_blocker):
    with django_db_blocker.unblock():
        Masterpiece.objects.create(
            name='Creation of Adam',
            author='Michelangelo',
            price='100.99'
        )
