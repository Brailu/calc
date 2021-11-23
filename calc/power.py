"""
power.py

A power calculator.
"""


from calc.keyboard import Keyboard
from calc.screen import Screen
from calc.memory import Memory
from calc.handler import Handler
from calc.basic import BasicCalculator


class PowerCalculator(BasicCalculator):

    model = "power"

    def calculate(self, operator, operand_1, operand_2):
        if operator == "^" or operator == "**":
            result = self.power(operand_1, operand_2)
            self.print(operator, operand_1, operand_2, result)
            self.write(operator, operand_1, operand_2, result)
        elif operator == "sqrt":
            result = self.sqrt(operand_1)
            self.print(operator, operand_1, operand_2, result)
            self.write(operator, operand_1, operand_2, result)
        else:
            super().calculate(operator, operand_1, operand_2)

    def power(self, operand_1, operand_2):
        return operand_1 ** operand_2
