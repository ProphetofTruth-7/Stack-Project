from stack import Stack


airport_queue = Stack()

airport_queue.push("Flight 101")
airport_queue.push("Flight 102")
airport_queue.push("Flight 104")
airport_queue.push("Flight 107")
print(airport_queue.items)

print()
print(f"Removing {airport_queue.peek()}")
airport_queue.pop()
print()

print(airport_queue.items)
print(f"There are {airport_queue.size()} flights in the queue")
print()