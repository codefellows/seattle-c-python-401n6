# print("let's do something totally wrong. See if you can spot me in the output!")
# print("Too many parentheses"))

# print("More wrongness. Do I get printed?")
# print("Who has ever "messed up" quotations marks?")

# print("What happens now? Do you see me printed?")
# value = 1/0
# print('after')

# try:
#     print("Divide by Zero again", 1/0)
# except ZeroDivisionError:
#     print("don't divide by zero")
# print('after')

# try:
#     print("Divide by Zero again", 1/ "spam")
# except:
#     print("don't divide by zero")
# print('after')

# try:
#     spam = 'junk' / 2
# except ZeroDivisionError:
#     print("Don't divide by zero")
# except Exception as e:
#     print("Generic message to the user")
#     print(e)

# print("Attempt to create a message")
# try:
#     message = "nothing" + "wrong" + "here"
# except TypeError:
#     print("Unable to create the message")
# else:
#     print("The message was a success")


# print("prepare for some breakage")
# try:
#     value = str(True) + "junk"
# except TypeError as e:
#     print(f'There was an issue. The error was {e}!')
# else:
#     print(f'Smooth sailing. The value is {value}')
# finally:
#     print("clean up on isle 13")

age = 20

if age < 21:
    raise ValueError("Invalid age - Gotta be 21 for this Party!")
