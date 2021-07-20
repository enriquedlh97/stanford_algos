import pytest
from algos.divide_conquer_sort_search_random.week_one.integer_multiplication import \
    grade_school_integer_multiplication_brute_force, recursive_integer_multiplication, karatsuba_integer_multiplication

tests_integer_multiplication = [(123, 456, 56088),
                                (1, 2, 2),
                                (12, 21, 252),
                                (213, 127, 27051),
                                (1279, 2137, 2733223),
                                (3333, 1111, 3702963),
                                (11, 15674, 172414),
                                (139, 15674, 2178686),
                                (0, 2, 0),
                                (0, 123, 0),
                                (7645, 0, 0),
                                (3141592653589793238462643383279502884197169399375105820974944592,
                                 2718281828459045235360287471352662497757247093699959574966967627,
                                 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)
                                ]

@pytest.mark.skip(reason="Should not be run because...")
@pytest.mark.parametrize("digit_one, digit_two, answer", tests_integer_multiplication)
def test_grade_school_integer_multiplication_brute_force(digit_one, digit_two, answer):
    assert grade_school_integer_multiplication_brute_force(digit_one, digit_two) == answer


@pytest.mark.parametrize("digit_one, digit_two, answer", tests_integer_multiplication)
def test_recursive_integer_multiplication(digit_one, digit_two, answer):
    assert recursive_integer_multiplication(digit_one, digit_two) == answer
