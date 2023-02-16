# Given a LL of single digit, non zero numbers, add one to the number "represented" by th eh LL.

# 4->2->3 Happy Path
# 4->2->4

# 9->9->9
# 1->0->0->0

# 9->8->9
# 9->9->0

# Brute Force
# define  counter
# def method

# assign the head to a variable
# traverse through the ll till the end
# check if value is 9.
# if it is not, add one to value and done.
# if it is 9, make it a 0, and subtract 1 from counter

# 1->9->8->9->-9

# reversed

# 9->9->8->9->-1
# 0->0->9
# re-reverse the ll


# Inputs and Outputs
# Singly linked link-list, the same

# Visual
# reverse the ll
# 1->9->8->9->-9

# reversed

# 9->9->8->9->-1
# 0->0->9->9->-1
# reverse it again

# Algo
# def the method that taking the ll

# set a boolean to true
# reverse
# assign the ll to a variable
# traverse through the ll until we get to the end or non 9
# if 9 and not last node make 0 make boolean var true
# if not then add 1 and break
# if 9 and last node, make 0 and add a node with value of 1

# reverse

# Big o space o(3n) = o(n), space o(1)

# 3->9->9
# Carryover = True
# 0->0->3
# Current = 3
# current.value = 4
# 4->0->0


def ll_add_one(self):
    self.reverse()
    current = self.head
    while current:
        if current.value == 9 and current.next is not None:
            current.value = 0
            current = current.next
        elif current.value < 9:
            current.value += 1
            break
        if current.next is None:
            current.value = 0
            node = Node(1)
            current.next = node
    self.reverse()



