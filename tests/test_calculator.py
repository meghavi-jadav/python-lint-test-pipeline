"""
Test module for the Calculator class.
"""

import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to provide a Calculator instance."""
    return Calculator()

def test_add(calc):
    """Test the addition method."""
    assert calc.add(10, 5) == 15

def test_subtract(calc):
    """Test the subtraction method."""
    assert calc.subtract(10, 5) == 5

def test_multiply(calc):
    """Test the multiplication method."""
    assert calc.multiply(10, 5) == 50

def test_divide(calc):
    """Test the division method."""
    assert calc.divide(10, 2) == 5.0

def test_divide_by_zero(calc):
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)
