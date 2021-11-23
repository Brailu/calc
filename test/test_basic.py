"""
test_basic.py

Test case for BasicCalculator class.
"""


from unittest import TestCase
from calc.basic import BasicCalculator


class TestBasicCalculator(TestCase):

    def setUp(self):
        self.basic_calculator = BasicCalculator()

    def tearDown(self):
        self.basic_calculator = None

    def test_sums_two_operands(self):
        self.assertEqual(self.basic_calculator.sum(2, 2), 4)

    def test_subtract_two_operands(self):
        self.assertEqual(self.basic_calculator.subtract(2, 2), 0)
    
    def test_multiply_two_numbers(self):
        self.assertEqual(self.basic_calculator.multiply(2, 2), 4)

    def test_divide_two_numbers(self):
        self.assertEqual(self.basic_calculator.divide(2, 2), 1)

    def test_get_expression(self):
        pass

    def test_returns_operator_and_operands_on_valid_expression(self):
        expression = "2 + 4"
        operator, operand_1, operand_2 = self.basic_calculator.evaluate_expression(expression)
        self.assertEqual(operator, "+")
        self.assertEqual(operand_1, 2)
        self.assertEqual(operand_2, 4)
    
    def test_exits_when_invalid_expression(self):
        expression = "bogus"
        with self.assertRaises(SystemExit):
            self.basic_calculator.evaluate_expression(expression)

    def test_calculate(self):
        pass

    def test_exits_when_dividing_by_zero(self):
        expression = "2 / 0"
        operator, operand_1, operand_2 = self.basic_calculator.evaluate_expression(expression)
        with self.assertRaises(SystemExit):
            self.basic_calculator.calculate(operator, operand_1, operand_2)
