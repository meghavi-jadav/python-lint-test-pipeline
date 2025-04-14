import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
  return Calculator()

def test_add(calc):
  assert calc.add(10, 5) == 15

def test_substract(calc):
  assert calc.subtract(10, 5) == 5
  
def test_multiply(calc):
  asserct calc.multiply(10, 5) == 50

def test_divide(calc):
  assert calc.divide(10, 2) == 5.0

def test_divide_by_zero(calc):
  with pytest.raises(ValueError, match="Cannot divide by zero"):
    calc.divide(10, 0)
  
