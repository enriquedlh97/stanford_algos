import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import initialize_row_results, \
    get_row_results, sum_row_results, grade_school_integer_multiplication


tests_initialize_row_results = [(0, []),
                                (1, ['0']),
                                (2, ['0', '0']),
                                (3, ['0', '0', '0']),
                                (4, ['0', '0', '0', '0']),
                                (10, ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']),
                                (13, ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']),
                                (20, ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
                                      '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']),
                                ]

tests_get_row_results = [(),
                         ]

tests_sum_row_results = [(),
                         ]

tests_integer_multiplication = [(),
                                ]


@pytest.mark.parametrize("zero_padding, answer", tests_initialize_row_results)
def test_tests_initialize_row_results(zero_padding, answer):
    assert initialize_row_results(zero_padding) == answer
