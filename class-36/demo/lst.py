# Given a list and an int, where each index in the list is a LL, write a function that deletes all nodes
# where the node value is greater than the given int.



# [ll1, ll2]
# ll1 10->19->2->None
# ll2 43->9->12->None

# def function that take in the lst and an int
def delete_over(lst, num):
    # iterate through the lst
    for ll in lst:

        # set a variable to the head of the ll
        current = ll.head
        # set a variable of at head to be true
        at_head = True

        # 1st loop deals with the head, head true
        while at_head  and ll.head:
            # is current > int and next = none
            if not ll.head.next and ll.head.value > num:
                # head to none
                ll.head = None

            # elif head > int
            elif ll.head.value > num:
                # head current.next
                ll.head = current.next
                # current.next None
                current.next = None
            # else current < int
            else:
                # at head to false
                at_head = False
                # current = current.next
                current = current.next
                # prev = current
                previous = current

        # check for current
        while current:
            # if current > value
            if current.value > num:
                # set prev .next to current .next
                previous.next = current.next
                # prev to current

            # current to next
            current = current.next

