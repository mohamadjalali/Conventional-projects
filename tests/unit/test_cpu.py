import pytest
from app.models import inventory



@pytest.fixture
def cpu_values():
    return {
        'name': 'Core i9-12950HX Processor',
        'manufacturer': 'Intel',
        'total': 100,
        'allocated': 50,
        'cores': 16,
        'socket': 'LGA 1200',
        'power_watts': 250
    }


@pytest.fixture
def cpu(cpu_values):
    return inventory.CPU(**cpu_values)


def test_create_cpu(cpu, cpu_values):
    for attr_name in cpu_values:
        assert getattr(cpu, attr_name) == cpu_values.get(attr_name)



@pytest.mark.parametrize(
    'cores, exception', [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
)
def test_create_invalid_cores(cores, exception, cpu_values):
    cpu_values['cores'] = cores
    with pytest.raises(exception):
        inventory.CPU(**cpu_values)



@pytest.mark.parametrize(
    'power_watts, exception', [(10.5, TypeError), (-1, ValueError), (0, ValueError)]
)
def test_create_invalid_power_watts(power_watts, exception, cpu_values):
    cpu_values['power_watts'] = power_watts
    with pytest.raises(exception):
        inventory.CPU(**cpu_values)


def test_repr(cpu):
    assert cpu.name in repr(cpu)
    assert cpu.category in repr(cpu)
    assert cpu.socket in repr(cpu)
    assert str(cpu.cores) in repr(cpu)

