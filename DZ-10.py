from colorama import init, Fore, Style
from functools import wraps

def color_decorator(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(color, end='')
            result = func(*args, **kwargs)
            print(Style.RESET_ALL, end='')
            return result
        return wrapper
    return decorator


@color_decorator(Fore.RED)
def print_message(message):
    print(message)

print_message("Этот текст будет выводиться красным")

#######################################################

def some_function(func):
    @wraps(func)
    def wrapper(a, b):
        if type(a) == type(b):
            print("Типы аргументов одинаковые")
            return func(a, b)
        else:
            print(f"Типы аргументов разные. {type(a)} и {type(b)}")
            return None
    return wrapper

@some_function
def test_type(a, b):
    c = a + b
    return c

print(test_type(2, 5))  
print(test_type(2, '5'))  
