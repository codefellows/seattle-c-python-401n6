import builtins

_print = builtins.print
_input = builtins.input


def alter():
    builtins.print = _input
    builtins.input = _print


def alter_back():
    builtins.print = _print
    builtins.input = _input


if __name__ == '__main__':

    user_name = _input('What is your name: ')
    _print(user_name)

    alter()

    user_name = input('What is your name: ')
    print(user_name)

    alter_back()
    user_name = _input('What is your name: ')
    _print(user_name)
