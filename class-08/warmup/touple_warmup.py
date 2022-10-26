# given a tuple of int. Write a function that returns a list of int's squared

# define a function that takes in a tuple
# (1, 2, 3, 4, 5)
#               ^
# squares = [1, 4, 9, 16, 25]
def square_tuple1(tpl):
    squares = []

    # iterate though the tuple and square each int and append to squares list
    for num in tpl:
        # squared_num = num * num
        # squares.append(squared_num)
        squares.append(num * num)

    # return the list squared
    return squares


def square_tuple2(tpl):
    return [num * num for num in tpl]


if __name__ == '__main__':
    info = input("Enter Sometjhing >")
    sq_return1 = square_tuple1((1, 2, 3, 4, 5))
    assert sq_return1 == [1, 4, 9, 16, 25]
    sq_return2 = square_tuple2((1, 2, 3, 4, 5))
    assert sq_return2 == [1, 4, 9, 16, 25]
