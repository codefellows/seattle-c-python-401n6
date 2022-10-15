class LinkedList:
    """
    Linkedlist class
    """

    def __init__(self, head=None):
        self.head = head

    # ll = LinkedList(()
    # node1 = 1
    # ll.head = node1
    # add in value 2
    # [1] -> None
    # [2] -> [1] -> None

    def insert(self, value):
        node = Node(value)
        # if self.head is None:
        #     self.head = node
        # if self.head is not None:
        #     node.next = self.head
        #     self.head = node

        if self.head is not None:
            node.next = self.head
        self.head = node
    # Head
    # [5] -> [4] -> [3] -> None
    #                       ^
    # Current

    # Linked List Head is:  [5] -> [11] -> None

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

    ll = LinkedList()
    # print(ll)
    node = Node(10)
    # print(node.value)
    node.value = 11
    # print(node.value)
    ll.head = node
    # print(ll.head.value)
    node2 = Node(5, node)
    ll.head = node2
    # Linked List Head is:  [5] -> [11] -> None
    print(ll.traverse())
