import pytest
from app.calc import Calculator

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.divide(10, 0)
