from stack import Stack

class InfixtoPostfixConverter:

    OPERATOR_SET = {"+", "-", "*", "/", "^"}
    PRECEDENCE_SET = {"+":1, "-":1, "*":2, "/":2, "^":3}

    def infix_to_postfix(self, expression: str):
        output = []
        operator_stack = Stack()

        tokens = expression.split()

        for token in tokens:
            if token in OPERATOR_SET:
                print("AMONGUS")
            else:
                print("NADA")


    expression = "A + B * C - D"
    print(infix_to_postfix(expression))