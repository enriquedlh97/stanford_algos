import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import grade_school_integer_multiplication, \
    recursive_integer_multiplication, karatsuba_integer_multiplication


tests_integer_multiplication = [(),
                                ]

@pytest.mark.skip(reason="Just a test")
@pytest.mark.parametrize("zero_padding, answer", tests_initialize_row_results)
def test_initialize_row_results(zero_padding, answer):
    assert initialize_row_results(zero_padding) == answer


