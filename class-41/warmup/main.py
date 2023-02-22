# Given a list of objects, with an age property, and a target age, find the age that is closest in age to the target age
# Input:
# 	{age:47,...}, {age:23,...}, {age: 17}
# 	29
# Output: 23
# Feature Tasks
# Iterate through collection of objects finding the one with the closest age.
#
# Expected function with a return of the age
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def find_age_list(people, target_age):
    closest_age_so_far = people[0]["age"]

    for peeps in people:
      candidate_age = peeps["age"]
      candidate_distance = abs(candidate_age - target_age)
      closest_distance_so_far = abs(closest_age_so_far - target_age)
      if candidate_distance < closest_distance_so_far:
        closest_age_so_far = candidate_age
    return closest_age_so_far


def find_age_ll(ll, target_age):
    current = ll.head
    closest_age_so_far = current.value["age"]

    while current:
      candidate_age = current.value["age"]
      candidate_distance = abs(candidate_age - target_age)
      closest_distance_so_far = abs(closest_age_so_far - target_age)
      if candidate_distance < closest_distance_so_far:
        closest_age_so_far= candidate_age
      current = current.next
    return closest_age_so_far

if __name__ == '__main__':
    folks = [{"age": 47}, {"age": 23}, {"age": 17}]
    age = 20
    print(f'The closest age to {age} is : {find_age_list(folks, age)}')

    node1 = Node({"age": 17})
    node2 = Node({"age": 23}, node1)
    node3 = Node({"age": 47}, node1)
    ll1 = LinkedList(node3)
    age = 12
    print(f'The closest age to {age} is : {find_age_ll(ll1, age)}')
