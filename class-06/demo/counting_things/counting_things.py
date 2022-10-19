from collections import Counter

fruit = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']

fruit_counter = Counter(fruit)

print(fruit_counter.most_common())

# fruit_map = {}
# for piece in fruit:
#     current_count = fruit_map.get(piece, 0)
#     fruit_map[piece] = current_count + 1
#
# print(fruit_map)
#
# most_common_count = 0
# most_common_fruit = None
#
# for fruit_name in fruit_map:
#     if fruit_map[fruit_name] > most_common_count:
#         most_common_count = fruit_map[fruit_name]
#         most_common_fruit = fruit_name
#
# print(most_common_fruit)
