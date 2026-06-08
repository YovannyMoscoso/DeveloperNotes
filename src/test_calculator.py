import pytest

from calculator import add, substract, multiply, divide 

class TestAdd:

    def test_add_positive(self):
        assert(add(2,3)== 5)

    def test_add_negative(self):
        assert(add(-2,-3)== -5)

    def test_add_zero(self):
        assert(add(0,0)== 0)


class TestSubstract:

    def test_substract_positive(self):
        assert(substract(2,3)== -1)

    def test_substract_negative(self):
        assert(substract(-2,-3)== 1)

    def test_substract_zero(self):
        assert(substract(0,0)== 0)

class TestMultiply:

    def test_multiply_positive(self):
        assert(multiply(2,3)== 6)

    def test_multiply_negative(self):
        assert(multiply(-2,-3)== 6)

    def test_multiply_zero_by_a_number(self):
        assert(multiply(1000,0)== 0)

    def test_multiply_zeros(self):
        assert(multiply(0,0)== 0)

class TestDivide:

    def test_divide_positive(self):
        assert(divide(10,5)== 2)

    def test_divide_negative(self):
        assert(divide(-10,-5)== 2)
        
    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
