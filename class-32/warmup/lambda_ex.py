# Regular Function
def this_function(y):
    return y

# lambda Function
x = lambda x:x+1

# Regular Sum
def sum_total(num1, num2, num3):
    return num1 + num2 + num3

new_sum = lambda num1, num2, num3: num1 + num2 + num3

larger = lambda num1, num2: a if num1>num2 else b

print('Regular')
print(this_function(5))
print('Lambda')
print(x(5))

