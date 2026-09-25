from node import Node


# FIFO data structure
class Queue:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.__first: Node | None = new_node
        self.__last: Node | None = new_node
        self.__length = 1

    def print_queue(self) -> None:
        current = self.__first
        while current is not None:
            print(current.value)
            current = current.next

    def enqueue(self, value: int) -> None:
        new_node = Node(value)

        if self.__first is None:
            self.__first = new_node
            self.__last = new_node
        else:
            assert self.__last is not None, "Queue corruption detected: first is set but last is None"

            self.__last.next = new_node
            self.__last = new_node

        self.__length += 1

    def dequeue(self) -> Node | None:
        if self.__first is None:
            return None

        temp = self.__first
        self.__first = self.__first.next
        temp.next = None

        if self.__first is None:
            self.__last = None

        self.__length -= 1

        return temp
