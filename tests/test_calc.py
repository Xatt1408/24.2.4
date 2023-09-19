import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_add_success(self):
        assert self.calc.adding(self, 1, 1) ==2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 5) == 20

    def test_division_success(self):
        assert self.calc.division(self, 35, 7) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 12, 4) == 8

    def teardown(self):
        print('Выполнение метода Teardown')