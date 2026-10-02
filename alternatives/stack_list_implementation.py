# Often preferred over the linked list implementation because of ease of implementation, less memory usage and better performance
class Stack:
    def __init__(self) -> None:
        self.__items: list[int] = []

    def push(self, value: int) -> None:
        self.__items.append(value)

    def pop(self) -> int | None:
        if self.is_empty():
            return None
        return self.__items.pop()

    def is_empty(self) -> bool:
        return len(self.__items) == 0
