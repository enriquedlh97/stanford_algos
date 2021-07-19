import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import \
    grade_school_integer_multiplication_brute_force, recursive_integer_multiplication, karatsuba_integer_multiplication


tests_integer_multiplication = [(),
                                ]


@pytest.mark.skip(reason="Just a test")
# @pytest.mark.parametrize("zero_padding, answer", tests_integer_multiplication)
def test_initialize_row_results(zero_padding, answer):
    assert grade_school_integer_multiplication_brute_force(zero_padding) == answer
