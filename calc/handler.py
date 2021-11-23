"""
handler.py

A two operands handler.
"""


class Handler():

    def handle(self, expression):
        operator = None
        operand_1 = None
        operand_2 = None
        error = None
        try:
            tokens = expression.split(" ")
            operator = tokens[1]
            operand_1 = int(tokens[0])
            operand_2 = int(tokens[2])
        except Exception as exception:
            error = "Invalid expression"

        return operator, operand_1, operand_2, error

