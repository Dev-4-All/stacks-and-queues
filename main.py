from stack import Stack

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
