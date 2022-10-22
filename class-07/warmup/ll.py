# - Write a function that takes a linked_list with single letters as
# values, and returns all the letters in a single string.
# `[p] -> [y] -> [t] -> [h] -> [o] -> [n] -> None`
# - returns 'python'

def concat_letters(ll):
    # set the ll.head to a variable
    current = ll.head  # -> Reference a node
    # create string to hold char values
    return_string = ""
    # traverse the ll
    while current:
        # error correction here
        # concat the values
        return_string += current.value
        # move to the next node
        current = current.next
    # return the string
    return return_string
