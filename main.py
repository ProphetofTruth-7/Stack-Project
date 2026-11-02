from stack import Stack


airport_queue = Stack()

airport_queue.push("Flight 101")
airport_queue.push("Flight 102")
print(airport_queue.items)

print(f"Removed {airport_queue.pop()}")

print(airport_queue.items)