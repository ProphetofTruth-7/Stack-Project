from stack import Stack

class InfixtoPostfixConverter:

    OPERATOR_SET = {"+", "-", "*", "/", "^"}
    PRECEDENCE_SET = {"+":3, "-":3, "*":2, "/":2, "^":1}

    def infix_to_postfix(self, expression: str):
        output = []
        operator_stack = Stack()

        tokens = expression.split()

        for current_token in tokens:
            if current_token not in self.OPERATOR_SET and current_token not in ("(", ")"):
                output.append(current_token)
            elif current_token == "(":
                operator_stack.push(current_token)
            elif current_token == ")":
                while not operator_stack.is_empty() and operator_stack.peek() != "(":
                    output.append(operator_stack.pop())
                if operator_stack.is_empty(): # Only checks after the loop clears out everything. If the stack is empty, then there was no proper paranthesis handling
                    raise ValueError("Incorrect closing paranthesis")
                operator_stack.pop()  # Removes the ( from the stack last, ensuring it doesn't affect future work
            else:
                while not operator_stack.is_empty() and current_token in self.OPERATOR_SET:   #The current_token is compared with each operator in the stack until it is of greater/equal predence to the operator. Then it is added to the stack
                    if self.PRECEDENCE_SET[operator_stack.peek()] <= self.PRECEDENCE_SET[current_token]:
                        output.append(operator_stack.pop())
                    else:
                        break
                operator_stack.push(current_token)

        while not operator_stack.is_empty():
            top = operator_stack.pop()
            if top == "(":
                raise ValueError("Mismatched parentheses")
            output.append(top)
        return " ".join(output)


converter = InfixtoPostfixConverter()
expression = "(A+B) - D * C"
print(converter.infix_to_postfix(expression))