"""
symbolic.py

A calculator that supports symbolic computation.
"""


import sympy

from calc.keyboard import Keyboard
from calc.screen import Screen
from calc.memory import Memory


class SingleHandler():

    def handle(self, expression):
        operator = None
        operand = None
        error = None
        try:
            tokens = expression.split(" ")
            operator = tokens[0]
            operand = int(tokens[1])
        except Exception as exception:
            error = "Invalid expression"

        return operator, operand, error


class SymbolicCalculator():
    
    vendor = "Python"
    model = "symbolic"

    keyboard = Keyboard()
    screen = Screen()
    memory = Memory()
    handler = SingleHandler()

    def get_expression(self):
        return self.keyboard.get_input("Expression: ")

    def evaluate_expression(self, expression):
        operator, operand, error = self.handler.handle(expression)
        if error:
            self.screen.print("Error", error)
            self.memory.write({"error": error})
            exit(1)
        else:
            return operator, operand
    
    def print(self, operator, operand, result):
        self.screen.print("Operator", operator)
        self.screen.print("Operand", operand)
        self.screen.print("Result", result)

    def write(self, operator, operand, result):
        operation = {
            "operator": operator,
            "operand": operand,
            "result": result
        }
        self.memory.write(operation)

    def calculate(self, operator, operand):
        if operator == "sqrt":
            result = self.sqrt(operand)
            self.print(operator, operand, result)
            self.write(operator, operand, result)
        else:
            self.screen.print("Error", "invalid operator")
            self.memory.write({"error": "invalid operator"})
            exit(1)

    def sqrt(self, operand):
        return sympy.sqrt(operand)
