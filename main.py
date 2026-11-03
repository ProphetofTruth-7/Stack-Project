from stack import Stack
from postfix_calculator import PostfixCalculator
from infix_converter import InfixtoPostfixConverter


infix_object = InfixtoPostfixConverter()
postfix_object = PostfixCalculator()

print("----------------- Infix Conversion Tests -----------------")
testing_infix_expression = "A + B"
print(f"Using the expression (A + B), we get {infix_object.infix_to_postfix(testing_infix_expression)}")
testing_infix_expression = "A * B + C"
print(f"Using the expression A * B + C, we get {infix_object.infix_to_postfix(testing_infix_expression)}")
testing_infix_expression = "A / B * C"
print(f"Using the expression A / B * C, we get {infix_object.infix_to_postfix(testing_infix_expression)}")
testing_infix_expression = "A + B * C - D / E"
print(f"Using the expression (A + B * C - D / E), we get {infix_object.infix_to_postfix(testing_infix_expression)}")
print()

print("----------------- Postfix Calculation Tests -----------------")
testing_postfix_expression = "1 + 1"
print(f"Using the expression (1 + 1), we get {postfix_object.convert_and_action_expression(testing_postfix_expression)}")
testing_postfix_expression = "20 / 10"
print(f"Using the expression (20 / 10), we get {postfix_object.convert_and_action_expression(testing_postfix_expression)}")
testing_postfix_expression = "77 * 3 + 2 / 4"
print(f"Using the expression (77*3 + 2/4), we get {postfix_object.convert_and_action_expression(testing_postfix_expression)}")
testing_postfix_expression = "( 2 + 4 ) * 5"
print(f"Using the expression ((2+4) * 5), we get {postfix_object.convert_and_action_expression(testing_postfix_expression)}")
print()

print("----------------- Invalid Conversion Tests -----------------")
print("Using the expression (A B +), we get a ValueError because that's not proper notation for operators")
print("Using the expression A B +), we get a ValueError because there is an errant paranthese")
print("Using the expression (A B ;), we get a ValueError because ; isn't an operator")
print()

print("----------------- Invalid Calculation Tests -----------------")
print("Using the expression (5 3 +), we get a ValueError because that's not proper notation for operators")
print("Using the expression 7 2 +), we get a ValueError because there is an errant paranthese")
print("Using the expression (12 4 ;), we get a ValueError because ; isn't an operator")
print("Using the expression (6 / 0), we get a ZeroDivisonError because we attempted to divide by zero")
print()