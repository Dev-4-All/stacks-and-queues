from node import Node


# LIFO data structure
class Stack:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.__top: Node | None = new_node
        self.__height = 1

    def print_stack(self) -> None:
        current = self.__top
        while current is not None:
            print(current.value)
            current = current.next

    def push(self, value: int) -> None:
        new_node = Node(value)

        if self.__top is None:
            self.__top = new_node
        else:
            new_node.next = self.__top
            self.__top = new_node

        self.__height += 1

    def pop(self) -> Node | None:
        if self.__top is None:
            return None
        
        temp = self.__top
        self.__top = self.__top.next
        temp.next = None

        self.__height -= 1

        return temp
