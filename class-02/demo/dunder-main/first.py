# import second
from second import print_second


def print_name():
    print(f'First Module Name: {__name__}')


if __name__ == '__main__':
    # This will be __main__
    print_name()

    # This will be second
    print_second()
