import pytest
from app.models import inventory

"""All classes in this file must be verified by Mohammad Jalalnia"""

@pytest.fixture
def storage_values():
    return {
        'name': 'Core i9-12950HX Processor',
        'manufacturer': 'Intel',
        'total': 15,
        'allocated': 5,
        'capacity_gb': 512
    }


@pytest.fixture
def storage(storage_values):
    return inventory.Storage(**storage_values)


def test_create_storage(storage, storage_values):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values.get(attr_name)



@pytest.mark.parametrize(
    'capacity_gb, exception', [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
)
def test_create_invalid_capacity_gb(capacity_gb, exception, storage_values):
    storage_values['capacity_gb'] = capacity_gb
    with pytest.raises(exception):
        inventory.Storage(**storage_values)


def test_repr(storage):
    assert storage.category in repr(storage)
    assert str(storage.capacity_gb) in repr(storage)

