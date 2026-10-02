from stack_list_implementation import Stack


# This implementation is rarely used (Bad performance and may introduce unnecessary bugs)
class Queue:
    def __init__(self) -> None:
        self.__stack_in = Stack()
        self.__stack_out = Stack()

    def enqueue(self, value: int) -> None:
        self.__stack_in.push(value)

    # Amortized TC = O(1)
    def dequeue(self) -> int | None:
        if self.__stack_out.is_empty():
            while not self.__stack_in.is_empty():
                item = self.__stack_in.pop()
                assert item is not None, "stack_in is broken"
                self.__stack_out.push(item)

        return self.__stack_out.pop()
