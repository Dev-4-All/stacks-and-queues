from queue import Queue

from stack import Stack

# Queue

# creation
my_queue = Queue(1)
my_queue.print_queue()

print()

# enqueue
my_queue.enqueue(2)
my_queue.print_queue()

print()

# dequeue
print(my_queue.dequeue().value) # type: ignore[union-attr]
print(my_queue.dequeue().value) # type: ignore[union-attr]
print(my_queue.dequeue())

print()

# Stack

# creation
my_stack = Stack(2)
my_stack.print_stack()

print()

# push
my_stack.push(1)
my_stack.print_stack()

print()

# pop
print(my_stack.pop().value) # type: ignore[union-attr]
print(my_stack.pop().value) # type: ignore[union-attr]
print(my_stack.pop())
