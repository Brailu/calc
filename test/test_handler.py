"""
test_handler.py

Test case for Handler class.
"""


from unittest import TestCase
from calc.handler import Handler


class TestHandler(TestCase):

    def setUp(self):
        self.handler = Handler()

    def test_returns_operator_and_operands(self):
        expression = "2 + 4"
        operator, operand_1, operand_2, error = self.handler.handle(expression)
        self.assertEqual(operator, "+")
        self.assertEqual(operand_1, 2)
        self.assertEqual(operand_2, 4)
        self.assertIsNone(error)

    def test_returns_error(self):
        expression = "bogus"
        operator, operand_1, operand_2, error = self.handler.handle(expression)
        self.assertIsNotNone(error)

    def tearDown(self):
        self.handler = None
