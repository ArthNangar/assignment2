import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
    assert addition(1,3) == 4

def test_subtraction():
    assert subtraction(5,2) == 3

def test_multiplication():
     assert multiplication(5,5) == 25

def test_division_positive():
     assert division(5,5) == 1

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)