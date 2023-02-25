# Given a ll of numbers, sum the numbers
# Warmup
def sum_values(ll):
    current = ll.head
    total = 0
    while current:
        total += current.value
        current = current.next
    return total

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): # List 2, 3, 4
                # -> (2) -> (3) -> (4)
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_



if __name__ == '__main__':
    def gen():
        for i in range(10):
            yield i

    def gen2():
        i = 0
        while True:
            yield i
            i += 1




    num_gen = gen2()
    try:
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
        print(next(num_gen))
    except StopIteration:
        print('Done')
    print(next(num_gen))
