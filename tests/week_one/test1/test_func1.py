from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import func1
import pytest

tests = [(1, 2, 3),
         (3, 4, 7),
         (5, 6, 11),
         ]


@pytest.mark.parametrize("a, b, answer", tests)
def test_func1(a, b, answer):
    assert func1(a, b) == answer
