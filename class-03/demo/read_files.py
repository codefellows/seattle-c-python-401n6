# file = open('spam.txt')
# print(file)
# print('Is the file closed', file.closed)
# file.close()
# print('Is the file closed', file.closed)

# with open("spam.txt") as file:
#     for word in file:
#         for letter in word:
#             print(letter)

    # print(file.read())
# print('Is the file closed', file.closed)

# print(dir(file))
# print(help(file))

# with open('brain.jpg', 'rb') as f:
#     content = f.read()
#     # print(content)
#
# for pixel in content[:128]:
#     print(type(content))
#
# with open('brain2.jpg', 'wb') as f2:
#     f2.write(content)

new_list = ["John", 36]

content = "My name is {}, I'm {}".format(*new_list)

print(content)
