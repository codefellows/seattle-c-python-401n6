# Write a function to determine if a sentence is a panagram.
# A panagram is a sentence or expression using every letter of the
# alphabet at least once.  Return 'True' or 'False'
#
#
# > The quick brown fox jumps over the lazy sleeping dog. -> True
# > Five quacking Zephyrs jolt my wax bed. -> True
# > The quick brown fox ->
#
# An 'A' or an 'a' will count as 1.
#
# You CANNOT use the string library


def is_pangram1(word):
    ALPHA = "abcdefghijklmnopqrstuvwxyz"
    for char in ALPHA:
        if char not in word.lower():
            return False
      return True


def is_panagram2(word):
    for num in range(97, 123):
        if chr(num) not in word.lower():
            return False
    return True
