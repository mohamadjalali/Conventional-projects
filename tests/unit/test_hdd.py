import pytest
from app.models import inventory



@pytest.fixture
def hdd_values():
    return  {
            'name': 'Blue WD10EZEX',
            'manufacturer': 'Western Digital',
            'total': 20,
            'allocated': 8,
            'capacity_gb': 1024,
            'size': '3.5"',
            'rpm': 5400
        }


@pytest.fixture
def hdd(hdd_values):
    return inventory.HDD(**hdd_values)



def test_create(hdd, hdd_values):
    for attr_name in hdd_values:
        assert getattr(hdd, attr_name) == hdd_values.get(attr_name)


@pytest.mark.parametrize('size', ['2.5', '5.26"'])
def test_create_invalid_size(hdd_values, size):
    hdd_values['size'] = size
    with pytest.raises(ValueError):
        inventory.HDD(**hdd_values)


@pytest.mark.parametrize(
    'rpm, exception',
    [
        ('120', TypeError),
        (100, ValueError),
        (60_000, ValueError),
        (-150, ValueError),
    ]
)
def test_create_invalid_rpm(hdd_values, rpm, exception):
    hdd_values['rpm'] = rpm
    with pytest.raises(exception):
        inventory.HDD(**hdd_values)


def test_repr(hdd):
    assert hdd.category in repr(hdd)
    assert hdd.size in repr(hdd)
    assert str(hdd.rpm) in repr(hdd)
    assert str(hdd.capacity_gb) in repr(hdd)
