# > Given 2 linked lists, write a function that returns the count of duplicate values
#
# Sample Data - Input od LL
# 1 -> 3 -> 8 -> 13 -> None
# 2 -> 3 -> 8 -> 23 -> None
#      ^    ^
# 3 and 8
# return 2 Int
# 2 possible solutions to review.
# First
# O(n^2) - Time
# O(1) - Space
# Second
# O(2n) also seen as O(n) - Time
# O(n) - Space

# Algo
# define the function and take in the 2 LL
# Assign the ll heads to variables
# define a counter and set to 0

# check if either head is None: return 0

# loop through the 1st ll
    # loop through the 2nd LL
    # compare value of ll1 to the value of ll2
    # if same increase the counter
    # traverse to next node
# traverse to next node
# after first loop set reset head of ll2
# return counter


# 1 -> 3 -> 8 -> 13 -> None
#           ^ - Current1
# 2 -> 3 -> 8 -> 23 -> None
#                     ^  - Current1
# count = 2

def duplicate_ll(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head
    count = 0
    if not current1 or not current2:
        return 0

    while current1:
        while current2:
            if current1.value == current2.value:
                count += 1
            current2 = current2.next
        current1 = current1.next
        current2 = ll2.head
    return count


def duplicate_ll2(ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head
    list1 = []
    count = 0
    while current1:
        list1.append(current1.value)

    while current2:
        if current2.value in list1:
            count += 1
    return count
