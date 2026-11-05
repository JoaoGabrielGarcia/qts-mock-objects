import pytest

from src.custom_stack_class import CustomStack, StackEmptyException, StackFullException


def test_empty_stack():
    stack = CustomStack(2)

    assert stack.is_empty()
    assert stack.size() == 0
    with pytest.raises(StackEmptyException):
        stack.pop()
    with pytest.raises(StackEmptyException):
        stack.top()


def test_push_top_and_pop_in_reverse_order():
    stack = CustomStack(2)

    stack.push(10)
    stack.push(20)

    assert not stack.is_empty()
    assert stack.size() == 2
    assert stack.top() == 20
    assert stack.pop() == 20
    assert stack.top() == 10
    assert stack.pop() == 10
    assert stack.is_empty()


def test_push_to_full_stack_raises_without_changing_it():
    stack = CustomStack(1)
    stack.push(10)

    with pytest.raises(StackFullException):
        stack.push(20)

    assert stack.size() == 1
    assert stack.top() == 10
