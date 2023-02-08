# Possible Solutions for Part 1

def is_ascending1(lst):
    if len(lst) < 1:
        return False
    previous = None
    for num in lst:
        if previous is None:
            previous = num
        elif num < previous:
            return False
        else:
            previous = num
    return True

#[3, 2, 1]
#    ^
# previous: 3

# [1, 2, 3]
#        ^
# previous: 3

def is_ascending2(lst):
    if len(lst) < 1:
        return False
    for idx, num in enumerate(lst):
        if idx == 0:
            pass
        elif num < lst[idx-1]:
            return False
    return True

def is_ascending3(lst):
    if len(lst) < 1:
        return False
    previous = lst[0]
    for number in lst:
        if  number < previous:
            return False
        previous = number
    return True

# Possible Solution for part 2
def is_sorted(ll):
    if not ll.head:
        return False
    ascending = True
    descending = True
    current = ll.head
    while current.next and (ascending or descending):
        cv = current.value
        nv = current.next.value
        if nv < cv:
            ascending = False
        if nv > cv:
            descending = False
        current = current.next
    return ascending or descending
