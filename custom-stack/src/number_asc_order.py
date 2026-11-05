from src.custom_stack_class import CustomStack


class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list[int]:
        if not isinstance(stack, CustomStack):
            raise TypeError("stack deve ser uma CustomStack")

        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
