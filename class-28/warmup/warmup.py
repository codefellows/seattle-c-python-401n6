# A dictionary to hold the letter scores
POINTS = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
    'z': 10
}


# cabbage
def scrabble_score(word):
    # define a variable to hold the total score
    score = 0
    if not word:
        return score

    for letter in word.lower():
        if letter.isalpha():
            score += POINTS[letter]

    # return the score
    return score


def scrabble_score2(word):
    return sum(POINTS[letter] for letter in "".join(word.lower()))
    # return sum(POINTS[letter] for letter in word.lower())


if __name__ == '__main__':
    print(scrabble_score('Cabbage!'))  # -> 14
    print(scrabble_score2('cabbage'))  # -> 14
