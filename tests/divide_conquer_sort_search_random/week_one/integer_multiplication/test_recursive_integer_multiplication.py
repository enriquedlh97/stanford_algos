import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import split_digit

tests_initialize_row_results = [('12', (1, 2)),
                                ('123', (12, 3)),
                                ('1234', (12, 34)),
                                ('12345', (123, 45)),
                                ('123456', (123, 456)),
                                ('1234567', (1234, 567)),
                                ('12345678', (1234, 5678)),
                                ('123456789', (12345, 6789)),
                                ('12345678910', (123456, 78910))
                                ]


@pytest.mark.parametrize("number, answer", tests_initialize_row_results)
def test_split_digit(number, answer):
    assert split_digit(number) == answer
