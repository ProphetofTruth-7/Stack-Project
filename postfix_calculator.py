from stack import Stack
from infix_converter import InfixtoPostfixConverter

class PostfixCalculator(self, expression):
    def __init__(self):
        self.converter = InfixtoPostfixConverter()

    def convert_and_action_expression(self, expression):
        postfix_expression = self.converter.infix_to_postfix(expression)
        return self.evaluate_expression(postfix_expression)

    def evaluate_expression(self, converted_expression):
        calculation_stack = Stack()

        for current_token in converted_expression.split():
            if token.isalnum():
                calculation_stack.push(current_token)
            else:
                right_operand = value_stack.pop()
                left_operand = value_stack.pop()

                result = self.calculate(left_operand, current_token, right_operand)
                value_stack.push(result)
        return value_stack.pop()  #Should be the final, calculated answer

    def calculate(self, left_operand, operator, right_operand):
        if operator == "+":
            return left_operand + right_operand
        if operator == "-":
            return left_operand - right_operand
        if operator == "*":
            return left_operand * right_operand
        if operator = "/":
            return left_operand / right_operand