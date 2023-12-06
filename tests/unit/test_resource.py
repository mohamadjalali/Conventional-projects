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


@pytest.mark.parametrize("total,allocated", [(10, -5), (10, 20)])
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(ValueError):
        Resource('name', 'manu', total, allocated)


def test_total(resource):
    assert resource.total == resource._total


def test_allocated(resource):
    assert resource.allocated == resource._allocated


def test_available(resource, resource_values):
    assert resource.available == resource.total - resource.allocated
    

def test_categoryt(resource):
    assert resource.category == 'resource'


def test_str_repr(resource):
    assert str(resource) == resource.name


def test_repr_repr(resource):
    assert repr(resource) == '{} ({} - {}): total={}, allocated={}'.format(
        resource.name, resource.category, resource.manufacturer,
        resource.total, resource.allocated
    )


def test_claim(resource):
    n = 2
    orginal_allocated = resource.allocated
    orginal_available = resource.available
    orginal_total = resource.total
    resource.claim(n)
    assert resource.allocated == orginal_allocated + n
    assert resource.available == orginal_available - n
    assert resource.total == orginal_total



@pytest.mark.parametrize("value", [-1, 0, 1_500])
def test_claim_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)



def test_purchased(resource):
    n = 2
    orginal_total = resource.total
    orginal_allocated = resource.allocated
    resource.purchased(n)
    assert resource.total == orginal_total + n
    assert resource.allocated == orginal_allocated


@pytest.mark.parametrize("value", [-1, 0])
def test_purchased_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.purchased(value)



def test_freeup(resource):
    n = 2
    orginal_allocated = resource.allocated
    orginal_total = resource.total
    resource.freeup(n)
    assert resource.allocated == orginal_allocated - n
    assert resource.total == orginal_total



@pytest.mark.parametrize("value", [-1, 0, 1_500])
def test_freeup_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.freeup(value)



def test_died(resource):
    n = 2
    orginal_total = resource.total
    orginal_allocated = resource.allocated
    resource.died(n)
    assert resource.total == orginal_total - n
    assert resource.allocated == orginal_allocated - n


@pytest.mark.parametrize("value", [-1, 0, 1_500])
def test_died_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.died(value)

