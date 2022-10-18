class LinkedList:
    """
    Linkedlist class
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        # print(ll)
        # ll.__str__()
        # "{ a } -> { b } -> { c } -> None"
        # traverse the linked list
        return_string = ''
        current = self.head
        while current:
            # temp = " { " + current.value + " } -> "
            return_string += f'{{ {current.value} }} -> '
            current = current.next
        return_string += "None"
        return return_string

    def insert(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        pass
        # take in a value
        # traverse the ll
        # check if the parameter is the same as the value
        # return true if there, false if not
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head  # 5
        while current is not None:
            # Do a thing
            print(current.value)
            current = current.next
        return current


class Node:
    """
    Node Class
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__ == '__main__':
    node3 = Node("c")
    node2 = Node("b", node3)
    node1 = Node("a", node2)
    ll = LinkedList(node1)
    # print(ll)

    print(ll.includes('d'))
