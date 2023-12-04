import pytest
from app.models.inventory import Resource



@pytest.fixture
def resource_values():
    return {
        'name': 'Parrot',
        'manufacturer': 'Pirates A-Hoy',
        'total': 100,
        'allocated': 50
    }


@pytest.fixture
def resource(resource_values):
    return Resource(**resource_values)


def test_create_resource(resource_values, resource):
    print(resource.__dict__)
    for attr_name in resource_values:
        assert getattr(resource, attr_name) == resource_values[attr_name]


def test_create_invalid_total_type(resource_values, resource):
    with pytest.raises(TypeError):
        Resource('Parrot', 'Pirates A-Hoy', 9.5, 4)


def test_create_invalid_allocated_type(resource_values, resource):
    with pytest.raises(TypeError):
        Resource('Parrot', 'Pirates A-Hoy', 10, 4.4)


def test_create_invalid_total_value(resource_values, resource):
    with pytest.raises(ValueError):
        Resource('Parrot', 'Pirates A-Hoy', -10, 4)

