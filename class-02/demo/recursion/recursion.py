def factorial(n):
    """
    This function will return the factorial sum
    of the n provided: n -> number
    :param n:
    :return: sum of n factorial
    """
    # Base Case
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(3))
    # 2 * factorial(2-1) -> 1 factorial(1)
        # 2 * (1)
    # 3 * factorial(3-1) -> 2 factorial(2)
        # 3 * 2 -> 6

# 3 * factorial(2 * factorial(1 * 1)))

# return 1
# 2 * factorial(2-1) -> 2
# 3 * factorial(3-1) -> 6
# ....
# 115 * factorial(115-1)
# 116 * factorial(116-1)
# 117 * factorial(117-1)
# 118 * factorial(118-1)
# 119 * factorial(119-1)
