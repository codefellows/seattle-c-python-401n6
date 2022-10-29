# Write a function that takes a list and sums the total of odd values


# [1, 4, 5, 8] = 6 (odd values)

def sum_odds_list(lst):
    sum_odd_values = 0
    # for num in lst:
    #     if num % 2 == 1:
    #         sum_odd_values += num

    return sum([x for x in lst if x % 2 == 1])
    # return sum_odd_values


# [1] -> [4] -> [5] -> [8] -> None    odds = 6   evens = 12
#                              ^
# even
def sum_odds_ll(ll, cmd):
    sum_values = 0 # 4 + 8 = 12
    current = ll.head
    while current:
        if current.value % 2 == 1 and cmd == "odd":
            sum_values += current.value
        elif current.value % 2 == 0 and cmd == "even":
            sum_values += current.value
        current = current.next
    return sum_values


if __name__ == '__main__':
    print(sum_odds_list([1, 4, 5, 8]))
