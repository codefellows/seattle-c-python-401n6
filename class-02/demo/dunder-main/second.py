# importing the function print_name from the file first.py
# from first import print_name


# this will result in print first
def print_second():
    print(f'First Module Name: {__name__}')


# What will this result in?
print(f'The __name__ in second is: {__name__}')
