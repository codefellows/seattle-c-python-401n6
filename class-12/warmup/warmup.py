# Given nested lists of integers, write some code that will add 2 to each one.
#
# Input:
#
# [[1, 2, 3] , [4, 5, 6]]
#
# Output:
#
# [[3, 4, 5], [6, 7, 8]]

# A few potential ways to accomplish this

def add_two1(nums):
    # [ [1, 2, 3] , [4, 5, 6] ]
    for lst in nums:
        i = 0
        for num in lst:
            num += 2
            lst[i] = num
            i += 1
    return nums


def add_two2(nums):
    for lst in nums:
        for i, num in enumerate(lst):
            lst[i] = num + 2
    return nums


def add_two3(nums):
    return [[num + 2 for num in lst] for lst in nums]


if __name__ == '__main__':
    list_of_list1 = [[1, 2, 3], [4, 5, 6]]
    list_of_list2 = [[1, 2, 3], [4, 5, 6]]
    list_of_list3 = [[1, 2, 3], [4, 5, 6]]
    print(add_two1(list_of_list1))
    print(add_two2(list_of_list2))
    print(add_two3(list_of_list3))
