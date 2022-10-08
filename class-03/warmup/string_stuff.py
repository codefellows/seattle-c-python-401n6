
def get_single_char(string):
    new_string = ''
    for char in string:
        if char.lower() not in new_string:
            new_string += char.lower()
    return new_string


# print(get_single_char('This is the string I am looking for'))
new_list = 'strings of stuffs'
# print(*new_list)
new_list = set(new_list)
print("".join(new_list))
