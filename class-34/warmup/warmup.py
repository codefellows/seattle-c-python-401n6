# Given the following list
# list=[3, 5, 75, 15, 2, 5, 3, 8, 15, 3, 5]
# remove all numbers not divisible by 3/5/ 3 and 5

my_list=[3, 5, 75, 15, 2, 5, 3, 8, 15, 3, 5]
removed = False
print(my_list)
list_range = len(my_list)
for i in range(list_range):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        my_list.pop(i)
        print(my_list)
        removed = True
    if i != 0 and True:
        list_range -=1
        removed = False
