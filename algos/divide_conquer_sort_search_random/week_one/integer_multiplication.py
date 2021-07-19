"""
Assignment:

    In this programming assignment you will implement one or more of the integer multiplication algorithms described in
    lecture.

    To get the most out of this assignment, your program should restrict itself to multiplying only pairs of
    single-digit numbers.  You can implement the grade-school algorithm if you want, but to get the most out of the
    assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

    So: what's the product of the following two 64-digit numbers?

    3141592653589793238462643383279502884197169399375105820974944592

    2718281828459045235360287471352662497757247093699959574966967627

    [TIP: before submitting, first test the correctness of your program on some small test cases of your own devising.
    Then post your best test cases to the discussion forums to help your fellow students!]

    [Food for thought: the number of digits in each input number is a power of 2.  Does this make your life easier?
    Does it depend on which algorithm you're implementing?]

    The numeric answer should be typed in the space below.  So if your answer is 1198233847, then just type 1198233847
    in the space provided without any space / commas / any other punctuation marks.

    (We do not require you to submit your code, so feel free to use any programming language you want --- just type the
    final numeric answer in the following space.)
"""


def grade_school_integer_multiplication_brute_force(digit_one, digit_two):
    """ Grade school integer multiplication algorithm, brute force approach



    :param digit_one: Integer value
    :param digit_two: Integer value
    :return: Integer value corresponding to the product of digit_one and digit_two
    """

    row_results = get_row_results(digit_one, digit_two)

    final_result = sum_row_results(row_results)

    return final_result


def sum_row_results(row_results):
    """ Helper function to compute the overall row sum



    :param row_results: Two-dimensional array containing the results of each row of the product.
    :return: Final product resulting from summing the elements from each row in the row_results array.
    """

    final_result = []
    remainder = 0

    for int_idx in reversed(range(len(row_results[-1]))):
        current_digit = 0
        for row_idx in range(len(row_results)):
            adjusted_index = int_idx - (len(row_results[-1]) - len(row_results[row_idx]))
            if adjusted_index >= 0:
                current_digit += int(row_results[row_idx][adjusted_index]) + remainder
                remainder = 0

        final_result.insert(0, str(current_digit)[-1])
        if str(current_digit)[:-1]:
            remainder = int(str(current_digit)[:-1])
        else:
            remainder = 0

        if int_idx == 0 and remainder > 0:
            final_result.insert(0, str(remainder))

    print(final_result)

    return int("".join(final_result))


def get_row_results(digit_one, digit_two):
    """ Helper function to compute row results



    :param digit_one: Integer value
    :param digit_two: Integer value
    :return: Two-dimensional array containing the results of each row of the product
    """
    top_number = "".join(["", str(max(digit_one, digit_two))])
    bottom_number = "".join(["", str(min(digit_one, digit_two))])

    row_results_array = []

    for bottom_idx in reversed(range(len(bottom_number))):
        row_result = initialize_row_results(len(bottom_number) - (bottom_idx + 1))
        remainder = 0
        for top_idx in reversed(range(len(top_number))):
            result = "".join(["", str(int(bottom_number[bottom_idx]) * int(top_number[top_idx]) + remainder)])
            row_result.insert(0, result[-1])

            if result[:-1]:
                remainder = int(result[:-1])
            else:
                remainder = 0

            if top_idx == 0 and remainder > 0:
                row_result.insert(0, str(remainder))

        row_results_array.append(row_result)

    return row_results_array


# Time: O(z), where z is the number of zeroes to be added
# Space: O(z)
def initialize_row_results(zero_padding):
    """ Helper function to initialize zeros in row results

    This helper function adds the required zeroes at the end of the initial row result needed for adequately summing all
    results.

    For example, when multiplying 456 * 123 in the grade school algorithm we would get something as follows:

                                                        4 5 6
                                                        1 2 3
                                                    _________
                                                      1 3 6 8
                                                      9 1 2
                                                    4 5 6
                                                    _________
                                                    5 6 0 8 8

    What this function does is, it adds the zeroes needed at the end of each row result to be able to directly sum each
    row. So that we get something like this.

                                                        4 5 6
                                                        1 2 3
                                                    _________
                                                      1 3 6 8
                                                      9 1 2 0
                                                    4 5 6 0 0
                                                    _________
                                                    5 6 0 8 8

    The important thing is to note that the zeroes are added at the beginning.  So, in this case, three arrays are
    initialized, each corresponding to the result of each row. The first one ahs no zeroes, the second one has one zero
    and the third one has two zeroes. So we would get something like this.

                                                row one: []
                                                row two: ['0']
                                                row three: ['0', '0']

    The function receives a value indicating the number of zeroes to add to the array. The zeroes are added (as
    character types) and then each array is returned.

    This algorithm takes O(z) time, where z is the number of zeroes that need to be added. And it also takes O(z) space
    for the same reason.

    :param zero_padding: Integer value corresponding to the number of zeros to add to initial row result.
    :return: Initial empty array containing zeroes.
    """
    row_result = []
    for _ in range(zero_padding):
        row_result.append("0")

    return row_result


def recursive_integer_multiplication(digit_one, digit_two):
    pass


def karatsuba_integer_multiplication(digit_one, digit_two):
    pass
