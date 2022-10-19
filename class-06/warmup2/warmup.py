# Given a linked_list, write a function that will traverse the linked list and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)->None expected return (13)

def largest_value(ll):
    current = ll.head
    largest = current.value
    while current:
        if current.value > largest:
            largest = current.value
        current = current.next

    return largest
