import random


def roller(num):
    # returned in a tuple
    return_numbers = []
    for number in range(num):
        return_numbers.append(random.randint(1, 6))
    return_numbers = tuple(return_numbers)
    return return_numbers


def score_roller(dice=roller(6)):
    # run through calculate score
    # return the score
    print(dice)


if __name__ == '__main__':
    roller1 = roller(2)
    score_roller()
    score_roller(roller1)
