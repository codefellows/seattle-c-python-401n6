# [ll1, ll2, ll3]
#               ^
# ll1 - 5->9->9->None
#                 ^
# ll2 - 2->1->1->None
#
# ll3 - 1->4->1->None
# total sum = 951
# list_number = '141'

def add_ll(lst):
    total_sum = 0
    for ll in lst:
        current = ll.head
        list_number = ''
        while current:
            list_number += str(current.value)
            current = current.next
        total_sum += int(list_number)
    return total_sum
