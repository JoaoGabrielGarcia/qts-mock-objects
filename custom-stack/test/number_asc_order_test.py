import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_six_drawn_numbers_with_mock_stack(mocker):
    stack = mocker.create_autospec(CustomStack, instance=True)
    stack.limit = 6
    stack.is_empty.side_effect = [False] * 6 + [True]
    stack.pop.side_effect = [42, 7, 60, 13, 35, 2]

    assert NumberAscOrder().sort(stack) == [2, 7, 13, 35, 42, 60]
    assert stack.is_empty.call_count == 7
    assert stack.pop.call_count == 6


def test_sort_six_drawn_numbers_in_real_stack():
    stack = CustomStack(6)
    for number in [42, 7, 60, 13, 35, 2]:
        stack.push(number)

    assert NumberAscOrder().sort(stack) == [2, 7, 13, 35, 42, 60]
    assert stack.is_empty()


def test_sort_empty_six_position_stack_with_mock(mocker):
    stack = mocker.create_autospec(CustomStack, instance=True)
    stack.limit = 6
    stack.is_empty.return_value = True

    assert NumberAscOrder().sort(stack) == []
    stack.is_empty.assert_called_once_with()
    stack.pop.assert_not_called()


def test_sort_rejects_non_stack():
    with pytest.raises(TypeError):
        NumberAscOrder().sort(None)
