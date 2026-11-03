import unittest
from infix_converter import InfixtoPostfixConverter


class TestInfixConverter(unittest.TestCase):

    def setUp(self):
        self.test_converter = InfixtoPostfixConverter()

    def test_valid_1(self):
        expression = "A + B"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B +")
    def test_valid_2(self):
        expression = "A + B * C"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B C * +")
    def test_valid_3(self):
        expression = "( A + B ) * C"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B + C *")
    def test_valid_4(self):
        expression = "A * B + C / D"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B * C D / +")
    def test_valid_5(self):
        expression = "( A + B ) * ( C - D )"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B + C D - *")
    def test_valid_6(self):
        expression = "A + B * C - D / E"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B C * + D E / -")
    def test_valid_7(self):
        expression = "( A + B * ( C - D ) ) / E"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B C D - * + E /")
    def test_valid_8(self):
        expression = "A + ( B - C ) * D"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B C - D * +")
    def test_valid_9(self):
        expression = "A - B + C"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B - C +")
    def test_valid_10(self):
        expression = "A * B / C"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B * C /")
    def test_robustness(self):
        expression = "( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( ( A + B ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )"
        self.assertEqual(self.test_converter.infix_to_postfix(expression), "A B +")
    def test_malformed_1(self):
        with self.assertRaises(ValueError):
            expression = "A + B )"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_2(self):
        with self.assertRaises(ValueError):
            expression = "A + B ; C"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_3(self):
        with self.assertRaises(ValueError):
            expression = "+ A B"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_4(self):
        with self.assertRaises(ValueError):
            expression = "A + * B"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_5(self):
        with self.assertRaises(ValueError):
            expression = "A B + C"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_6(self):
        with self.assertRaises(ValueError):
            expression = "A + ) B * C ("
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_7(self):
        with self.assertRaises(ValueError):
            expression = "( A + B"
            self.test_converter.infix_to_postfix(expression)
    def test_malformed_8(self):
        with self.assertRaises(ValueError):
            expression = "A + B )"
            self.test_converter.infix_to_postfix(expression)
            

if __name__ == "__main__":
    unittest.main()