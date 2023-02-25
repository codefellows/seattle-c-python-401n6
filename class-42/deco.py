from functools import wraps
from time import sleep

def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        oring_val = func(*args, **kwargs)
        return f"Yo Mamma Says: {oring_val}"
    return wrapper

def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)
    return wrapper

def high_class(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        oring_val = func(*args, **kwargs)
        return f"It is with a Great Honor that I say: : {oring_val}"
    return wrapper


@yo_mamma_decorator
@high_class
@procrastinate

def just_sayin(txt):
    return txt

if __name__ == '__main__':
    print(just_sayin("I love Star Wars"))
