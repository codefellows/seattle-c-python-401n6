# By Reference vs By Value
import copy

meal1 = ['bread', 'cheese']

# meal2 = meal1

# meal2 = ['bread', 'cheese']

# print(f'Original Meal 1: {meal1}')
# print(f'Original Meal 2: {meal2}')
# print('Appending to Meal1')
# meal1.append('turkey')
# meal2.append('ham')
# print(f'New Meal 1: {meal1}')
# print(f'New Meal 2: {meal2}')
# print(id(meal1), id(meal2))

meal2 = copy.copy(meal1)

print(f'Original Meal 1: {meal1}')
print(f'Original Meal 2: {meal2}')
print('Appending to Meal1')
meal1.append('turkey')
meal2.append('ham')
print(f'New Meal 1: {meal1}')
print(f'New Meal 2: {meal2}')
print(id(meal1), id(meal2))
