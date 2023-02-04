# Write a function that takes 2 linked lists, of single digit, positive numbers, and add the "numbers"
# represented by the linked list.
#
# ll1: [1]->[0]->[0]-> None :100
# ll2: [2]->[2]->[2]-> None :222
# 100 + 222 = 322

def ad_ll(ll1, ll2):
    ll1_num, ll2_num = '',''
    current1, current2 = ll1.head, ll2.head
    if not current1 and not current2:
        return 0
    while current1 or current2:
        if current1:
            ll1_num += str(current1.value)
            current1 = current1.next
        if current2:
            ll2_num += str(current2.value)
            current2 = current2.next
    return int(ll1_num) + int(ll2_num)
