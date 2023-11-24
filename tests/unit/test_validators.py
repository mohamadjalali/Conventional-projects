from app.utils.validators import validate_integer
import pytest



class TestIntegerValidator:

    def test_valid(self):
        validate_integer('arg', 9, 0, 20, 'custom min msg', 'custom max msg')
    
    
    def test_type_error(self):
        with pytest.raises(TypeError):
            validate_integer('arg', 2.7)
    
    
    def test_min_std_err_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 6, 100)
        assert 'arg' in str(ex.value)
        assert '100' in str(ex.value)

    
    def test_max_std_err_msb(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 20, max_value=15)
        assert 'arg' in str(ex.value)
        assert '15'  in str(ex.value)
    
    
    def test_min_custom_error_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', -2, 0, 20, custom_min_message="custom min")
        assert str(ex.value) == "custom min"
    
    
    def test_max_custom_error_msg(self):
        with pytest.raises(ValueError) as ex:
            validate_integer('arg', 25, 0, 20,custom_max_message="custom max")
        assert str(ex.value) == "custom max"
