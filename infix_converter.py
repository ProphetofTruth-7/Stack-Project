class InfixtoPostfixConverter:
    def __init__(self):
        self.stack = Stack()
        self.output = []