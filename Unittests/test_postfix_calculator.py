import unittest
from postfix_calculator import PostfixCalculator

class TestPostfixCalculator(unittest.TestCase):

    def setUp(self):
        self.test_calculator = PostfixCalculator()

    def test_valid_1(self):
        expression = "5 + 3"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 8)
    def test_valid_2(self):
        expression = "8 - 2 + 3"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 9)
    def test_valid_3(self):
        expression = "3 * 8 + 5"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 29)
    def test_valid_4(self):
        expression = "6 / 2 + 3"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 6.0)
    def test_valid_5(self):
        expression = "5 + 8 - 3"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 10)
    def test_valid_6(self):
        expression = "( 5 + 3 ) * 8"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 64)
    def test_valid_7(self):
        expression = "( 2 * 3 ) + 8 - 6"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 8)
    def test_valid_8(self):
        expression = "( 8 + 2 ) - ( 3 * 6 )"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), -8)
    def test_valid_9(self):
        expression = "( 35 + 27 ) * 3"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 186)
    def test_valid_10(self):
        expression = "23 / ( 30 * 15 )"
        self.assertEqual(self.test_calculator.convert_and_action_expression(expression), 23/(30*15))
    def test_invalid_1(self):
        with self.assertRaises(ValueError):
            expression = "3 4 +"
            self.test_calculator.convert_and_action_expression(expression)
    def test_invalid_2(self):
        with self.assertRaises(ValueError):
            expression = "5 +"
            self.test_calculator.convert_and_action_expression(expression)
    def test_invalid_3(self):
        with self.assertRaises(ZeroDivisionError):
            expression = "8 / 0"
            self.test_calculator.convert_and_action_expression(expression)
    def test_invalid_4(self):
        with self.assertRaises(ValueError):
            expression = "25 - 23 +"
            self.test_calculator.convert_and_action_expression(expression)
    def test_invalid_5(self):
        with self.assertRaises(ValueError):
            expression = "20 ; ( 29 * 9 )"
            self.test_calculator.convert_and_action_expression(expression)
    def test_invalid_6(self):
        with self.assertRaises(ValueError):
            expression = "3 + 4 2"
            self.test_calculator.convert_and_action_expression(expression)
        


if __name__ == "__main__":
    unittest.main()