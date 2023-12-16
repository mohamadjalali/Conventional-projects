import pytest
from app.models import inventory


@pytest.fixture
def ssd_values():
    return {
        'name': 'SU800 Internal',
        'manufacturer': 'ADATA',
        'total': 20,
        'allocated': 10,
        'capacity_gb': 256,
        'interface': 'SATA III'
    }


@pytest.fixture
def ssd(ssd_values):
    return inventory.SSD(**ssd_values)



def test_create(ssd, ssd_values):
    for attr_name in ssd_values:
        assert getattr(ssd, attr_name) == ssd_values.get(attr_name)



def test_repr(ssd):
    assert ssd.category in repr(ssd)
    assert str(ssd.capacity_gb) in repr(ssd)
    assert ssd.interface in repr(ssd)


