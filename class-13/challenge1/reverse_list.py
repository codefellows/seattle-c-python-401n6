# Code challenge 1:
#  - Given a list, reverse the list. In place, no built in methods / functions

# Given List: [1, 2, 5, 3, 4]
#                    ^
# Given List: [4, 3, 5, 2, 1]
def reverse_list(lst):
    # Iterate though the list upto the 1/2 point
    for i in range(len(lst) // 2):
        # swap front and back

        lst[i], lst[- 1 - i] = lst[-1 - i], lst[i]
    return lst


# Code challenge 2:
#  - Refactor the code to take in a linked_list

def reverse_ll(ll):
    # Input: None <- [1] <- [2] <- [3] <- [4] X None
    # current                                    ^
    # temp_next                                 ^
    # Current: None
    # Previous: 4
    # temp_next = None

    current = ll.head
    previous = None

    while current:
        temp_next = current.next
        current.next = previous
        previous = current
        current = temp_next
    ll.head = previous

    return ll

















if __name__ == '__main__':
    print(reverse_list([1, 2, 3, 4]))
    print(reverse_list([1, 2, 3, 4, 5]))
    print(reverse_list([1]))
    print(reverse_list(['1', '2', 3, 4, '5']))
