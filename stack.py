class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot remove from empty Stack")
        return self.items.pop()