# Write a function that will look at a parameter
# if it is divisible by 3 return fizz
# if divisible by 5 return buzz
# if divisible by 3 and 5 return fizzbuzz
# if not divisible by either, return the value

# def fizzbuzz_function(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     if number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return number

def fizzbuzz_function(number):
    word = ''
    if number % 3 == 0:
        word = 'Fizz'
    if number % 5 == 0:
        word += 'Buzz'

    return word or number
