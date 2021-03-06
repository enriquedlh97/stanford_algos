"""
This file tests the helper functions used in the grade school integer multiplication algorithm. The main function is
tested in the test_integer_multiplication.py file, where all main algorithms are tested.
"""

import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import initialize_row_results, \
    get_row_results, sum_row_results


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

tests_get_row_results = [(123, 456, [['1', '3', '6', '8'], ['9', '1', '2', '0'], ['4', '5', '6', '0', '0']]),
                         (1, 2, [['2']]),
                         (12, 21, [['4', '2'], ['2', '1', '0']]),
                         (213, 127, [['1', '4', '9', '1'], ['4', '2', '6', '0'], ['2', '1', '3', '0', '0']]),
                         (1279, 2137, [['1', '9', '2', '3', '3'], ['1', '4', '9', '5', '9', '0'],
                                       ['4', '2', '7', '4', '0', '0'], ['2', '1', '3', '7', '0', '0', '0']]),
                         (3333, 1111, [['3', '3', '3', '3'], ['3', '3', '3', '3', '0'],
                                       ['3', '3', '3', '3', '0', '0'], ['3', '3', '3', '3', '0', '0', '0']]),
                         (11, 15674, [['1', '5', '6', '7', '4'], ['1', '5', '6', '7', '4', '0']]),
                         (139, 15674, [['1', '4', '1', '0', '6', '6'], ['4', '7', '0', '2', '2', '0'],
                                       ['1', '5', '6', '7', '4', '0', '0']]),
                         (0, 2, [['0']]),
                         (0, 123, [['0', '0', '0']]),
                         (7645, 0, [['0', '0', '0', '0']])
                         ]

tests_sum_row_results = [([['1', '3', '6', '8'], ['9', '1', '2', '0'], ['4', '5', '6', '0', '0']], 56088),
                         ([['2']], 2),
                         ([['4', '2'], ['2', '1', '0']], 252),
                         ([['1', '4', '9', '1'], ['4', '2', '6', '0'], ['2', '1', '3', '0', '0']], 27051),
                         ([['1', '9', '2', '3', '3'], ['1', '4', '9', '5', '9', '0'],
                           ['4', '2', '7', '4', '0', '0'], ['2', '1', '3', '7', '0', '0', '0']], 2733223),
                         ([['3', '3', '3', '3'], ['3', '3', '3', '3', '0'],
                           ['3', '3', '3', '3', '0', '0'], ['3', '3', '3', '3', '0', '0', '0']], 3702963),
                         ([['1', '5', '6', '7', '4'], ['1', '5', '6', '7', '4', '0']], 172414),
                         ([['1', '4', '1', '0', '6', '6'], ['4', '7', '0', '2', '2', '0'],
                           ['1', '5', '6', '7', '4', '0', '0']], 2178686),
                         ([['0']], 0),
                         ([['0', '0', '0']], 0),
                         ([['0', '0', '0', '0']], 0)
                         ]


@pytest.mark.parametrize("zero_padding, answer", tests_initialize_row_results)
def test_initialize_row_results(zero_padding, answer):
    assert initialize_row_results(zero_padding) == answer


@pytest.mark.parametrize("digit_one, digit_two, answer", tests_get_row_results)
def test_get_row_results(digit_one, digit_two, answer):
    assert get_row_results(digit_one, digit_two) == answer


@pytest.mark.parametrize("row_results, answer", tests_sum_row_results)
def test_sum_row_results(row_results, answer):
    assert sum_row_results(row_results) == answer
