import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import split_digit

tests_initialize_row_results = [('12', (10, 2)),
                                ('123', (120, 3)),
                                ('1234', (1200, 34)),
                                ('12345', (12300, 45)),
                                ('123456', (123000, 456)),
                                ('1234567', (1234000, 567)),
                                ('12345678', (12340000, 5678)),
                                ('123456789', (123450000, 6789)),
                                ('12345678910', (12345600000, 78910))
                                ]


@pytest.mark.parametrize("number, answer", tests_initialize_row_results)
def test_split_digit(number, answer):
    assert split_digit(number) == answer
