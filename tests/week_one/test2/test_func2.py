from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import func2

import pytest

tests = [(1, 2, -1),
         (3, 4, -1),
         (5, 6, -1),
         ]


@pytest.mark.parametrize("a, b, answer", tests)
def test_func2(a, b, answer):
    assert func2(a, b) == answer
