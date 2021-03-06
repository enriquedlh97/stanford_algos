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


# Time: O(b * t), where b is the number of digits in the bottom number and t the number of digits in the top number
# Space: O(b * t)
def grade_school_integer_multiplication_brute_force(digit_one, digit_two):
    """ Grade school integer multiplication algorithm, brute force approach

    This is the main function fo the grade school integer multiplication algorithm. It essentially just calls helper
    functions to handle all the computations.

    :param digit_one: Integer value
    :param digit_two: Integer value
    :return: Integer value corresponding to the product of digit_one and digit_two
    """

    # Time: O(b * t), where b is the number of digits in the bottom number and t the number of digits in the top number
    # Space: O(b * t)
    row_results = get_row_results(digit_one, digit_two)

    # Time: O(b * t), where b is the number of digits in the bottom number and t the number of digits in the top number
    # Space: O(b * t)
    final_result = sum_row_results(row_results)

    return final_result


# Time: O(b * t), where b is the number of digits in the bottom number and t the number of digits in the top number
# Space: O(b * t)
def sum_row_results(row_results):
    """ Helper function to compute the overall row sum

    This helper function sums the numbers contain in each row array, resulting in the final product.

    :param row_results: Two-dimensional array containing the results of each row of the product.
    :return: Final product resulting from summing the elements from each row in the row_results array.
    """

    final_result = []
    remainder = 0

    # This for loop takes O(t) time, where t is the number of elements in the top digit
    for int_idx in reversed(range(len(row_results[-1]))):
        current_digit = 0
        # This inner for loop takes O(b) time, where b is the number of elements in the bottom digit, corresponding to
        # the total number fo rows
        for row_idx in range(len(row_results)):
            # The index is adjusted so that the same value can be applied to all rows and be a valid index
            adjusted_index = int_idx - (len(row_results[-1]) - len(row_results[row_idx]))
            if adjusted_index >= 0:
                current_digit += int(row_results[row_idx][adjusted_index]) + remainder
                remainder = 0

        # The insertion method in python takes O(l) time, where l is the length of the array. To improve this to
        # constant time it would be better to use the collections.deque which is implemented as a doubly linked
        # list, essentially making the insertion at the front an O(1) time operation.
        final_result.insert(0, str(current_digit)[-1])
        # Slicing a string, in this case result[:-1] is an O(k^2) time operation in python. This could be improved
        # by just checking if len(result) > 1. Nevertheless, this result is going to have at most 2 elements, making
        # this an O(1) time operation
        if str(current_digit)[:-1]:
            remainder = int(str(current_digit)[:-1])
        else:
            remainder = 0

        # This makes sure that the last remainder for the las row in the row_Results_array is added to the final result
        if int_idx == 0 and remainder > 0:
            final_result.insert(0, str(remainder))

    return int("".join(final_result))


# Time: O(b * t), where b is the number of digits in the bottom number and t the number of digits in the top number
# Space: O(b * t)
def get_row_results(digit_one, digit_two):
    """ Helper function to compute row results

    This helper function works by iterating first over each number of the bottom digit. Because of how the algorithm is
    set up, the bottom digit is always going to be bigger than the top digit. Then, for each number in the bottom digit,
    the algorithm iterates over each number in the top digit.

    At each step from the outer loop, the row solution is initialized with the corresponding zeroes. Then at each step
    of the inner loop, the current number from the bottom digit is multiplied with the current number from the top
    digit. This is just a single digit multiplication. The "units" or right most number from this result is added ti the
    rwo results array, the left most element or number that are not apr of the units are saved as remainder to be added
    in the next product.

    When both for loops are over, the two-dimensional array row_results_Array contains the row solutions and is returned

    :param digit_one: Integer value
    :param digit_two: Integer value
    :return: Two-dimensional array containing the results of each row of the product
    """
    # Casting an integer to a string takes O(s) time, where s is the number of characters in the digit.
    # Since the concatenation is executed for just two elements (the digit as a string and the "") it will take
    # O(1) time. This applies for both the top and bottom numbers.
    top_number = "".join(["", str(max(digit_one, digit_two))])
    bottom_number = "".join(["", str(min(digit_one, digit_two))])

    row_results_array = []

    # The outer loop iterates over each element from the bottom digit, taking O(b) time, where b is the number of
    # elements int he bottom digit
    for bottom_idx in reversed(range(len(bottom_number))):
        # Here the helper function for initializing the row results is called. This function takes O(z) time and space,
        # where z is the number of zeroes to be added. z = O(b) since z can be computed as b - 1
        row_result = initialize_row_results(len(bottom_number) - (bottom_idx + 1))
        remainder = 0
        # The inner loop iterates over each element from the top digit, taking O(t) time, where t is the number of
        # elements in the top digit
        for top_idx in reversed(range(len(top_number))):
            # Casting an integer to a string takes O(p) time, where p is the number of characters in the digit resulting
            # from the product. In this case, since only single digits are multiplied, this step takes O(1) time
            # Since the concatenation is executed for just two elements (the digit as a string and the "") it will take
            # O(1) time.
            result = "".join(["", str(int(bottom_number[bottom_idx]) * int(top_number[top_idx]) + remainder)])
            # The insertion method in python takes O(l) time, where l is the length of the array. To improve this to
            # constant time it would be better to use the collections.deque which is implemented as a doubly linked
            # list, essentially making the insertion at the front process an O(1) time operation.
            row_result.insert(0, result[-1])
            # Slicing a string, in this case result[:-1] is an O(k^2) time operation in python. This could be improved
            # by just checking if len(result) > 1. Nevertheless, this result is going to have at most 2 elements, making
            # this an O(1) time operation. For more information see
            # https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice/35181399
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


# @ TODO: Compute time and space complexity of recursive int multiplication
def recursive_integer_multiplication(digit_one, digit_two):
    """ Recursive integer multiplication

    This algorithm works by dividing the digit_one into  a and b, which essentially represent the left and right halves
    of the number. The same is done for the second digit where it is divided into b and c.

    Then, the products a * c, a * d, b * c and b * d are computed.

    Finally, the resulting product is computing using the following formula:

    10^(n) * ac + 10^(n/2) * (ad + bc) + bd

    Here, n is the number of digits that the input number have. For that reason, the algorithm only works for input
    digits that are a power of 2 and both input digits have to be of the same size.

    The algorithm is called recursively on the  a * c, a * d, b * c and b * d until only single-digit products are being
    computed.

    :param digit_one: Integer
    :param digit_two: Integer
    :return: Integer corresponding to the product of the two input digits
    """
    # Cast digits to strings. Casting to string takes O(n) time, where n is the length of the digit
    digit_one = str(digit_one)
    digit_two = str(digit_two)

    # Define exponent n.
    n = max(len(digit_one), len(digit_two))

    # Handle base case when both digit_one and digit_two are single number digits. For more information see
    # https://stackoverflow.com/questions/35180377/time-complexity-of-string-slice/35181399
    if len(digit_one) == len(digit_two) == 1:
        # Casting to int takes O(n) time, where n is the length of the digit
        return int(digit_one) * int(digit_two)

    # Define x in terms of a and b. This is an O(n^2) time operation
    a, b = split_digit(digit_one)
    # Define y in terms of c and d. This is an O(n^2) time operation
    c, d = split_digit(digit_two)
    # Compute a * c
    ac = recursive_integer_multiplication(a, c)
    # Compute a * d
    ad = recursive_integer_multiplication(a, d)
    # Compute b * c
    bc = recursive_integer_multiplication(b, c)
    # Compute b * d
    bd = recursive_integer_multiplication(b, d)
    # Compute x * y
    xy = pow(10, n) * ac + pow(10, n // 2) * (ad + bc) + bd

    return xy


# Time: O(n^2), where n is the number of digits in the input number
# Space: O(n), this is because copies are created
def split_digit(number):
    """ Helper function to split numbers

    This helper function is used to split a number in half

    :param number: Integer to be split
    :return: Input integer split in half, returns left_number and right_number
    """
    # Get number of digits in right side
    right_size = len(number) // 2
    # Get right and left numbers
    if right_size == 0:
        right_number = int(number)
        left_number = 0
    else:
        # Slicing a string is an O(n^2) time operation in python where n is the length of the string.
        right_number = int(str(number)[-right_size:])
        left_number = int(str(number)[:-right_size])

    return left_number, right_number


# @TODO: Finish documentation for karatsuba
# @ TODO: Compute time and space complexity of karatsuba
def karatsuba_integer_multiplication(digit_one, digit_two):
    """

    :param digit_one:
    :param digit_two:
    :return:
    """
    # Handle base case
    if digit_one < 10 and digit_two < 10:
        return digit_one * digit_two

    # Get exponent
    n = max(len(str(digit_one)), len(str(digit_two)))

    # Define function for handling odd exponent n
    nby2 = round(n / 2)

    # Get a, b, c and d
    a = digit_one // (10 ** nby2)
    b = digit_one % (10 ** nby2)

    c = digit_two // (10 ** nby2)
    d = digit_two % (10 ** nby2)

    # 1. Compute a * c, this is computed recursively
    ac = karatsuba_integer_multiplication(a, c)

    # 2. Compute b * d, this is computed recursively
    bd = karatsuba_integer_multiplication(b, d)

    # 3. Compute (a + b) * (c + d)
    ab_times_cd = karatsuba_integer_multiplication(a + b, c + d)

    # 4. Compute 3. - 2. - 1. = ad + bc
    ad_plus_bc = ab_times_cd - bd - ac

    # 5. Execute 10^(n) * ac + 10^(n/2) * (ad + bc) + bd
    result = (10 ** (2 * nby2)) * ac + (10 ** nby2) * ad_plus_bc + bd

    return result


if __name__ == "__main__":
    tests_integer_multiplication = [
                                    (3141592653589793238462643383279502884197169399375105820974944592,
                                     2718281828459045235360287471352662497757247093699959574966967627,
                                     8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)
                                    ]

    for test_num, test in enumerate(tests_integer_multiplication):
        digit_one, digit_two, answer = test[0], test[1], test[2]
        result = recursive_integer_multiplication(digit_one, digit_two)

        if result == answer:
            print("Test {}: Passed".format(test_num))
        else:
            print("Test {}: Failed".format(test_num))
