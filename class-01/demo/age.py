def get_age(age):
    # new_age = age + 50
    # List
    ages = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    # Tuple
    # ages = (1, 2, 3, 4, 5)
    # ages = (1, 2)
    # print('my age is ' + age)
    # print('my age is ' + str(age))
    # print(f'my age is {new_age}. I was {age} this year!')
    # print('{},{},{},{},{}'.format(*ages))

    # for age in ages:
    #     print(age)

    # name = 'Mark'
    # for letter in name:
    #     print(letter)

    print(ages)
    ages.append(6)
    print(set(ages))

# age = 1
# age = 2
# age = 3

if __name__ == '__main__':
    get_age(21)
