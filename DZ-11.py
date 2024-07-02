import functools

######### Залание 1
print("#"*8, "Залание 1", "#"*8)
print()

resistor_series = {
    'E6': [100, 150, 220, 330, 470, 680],
    'E12': [100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820],
    'E24': [100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910],
    'E48': [100, 105, 110, 115, 120, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953],
    'E96': [100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976]
}

def pick_resistors(resistance) :
    if not (100 <= resistance <= 999) :
        return None

    def closest_values(series) :
        min_diff = min(map(lambda r : abs(r - resistance), series))
        return tuple(filter(lambda r : abs(r - resistance) == min_diff, series))

    return {key : closest_values(series) for key, series in resistor_series.items()}


print(pick_resistors(112))
print(pick_resistors(549))

######### Залание 2
print("#"*8, "Залание 2", "#"*8)
print()
def deck():
    suits = ['черви', 'бубны', 'пики', 'трефы']
    for suit in suits:
        for rank in range(2, 15):
            yield (rank, suit)


for card in list(deck()):
    print(card)

print(list(deck())[::13])

######### Залание 3
print("#"*8, "Залание 3", "#"*8)
print()


def math_function_resolver(func, *args, res_to_str=False) :
    results = [round(func(x)) for x in args]
    if res_to_str :
        return list(map(str, results))
    return results


print(math_function_resolver(lambda x : 0.5 * x + 2, *range(1, 10)))
print(math_function_resolver(lambda x : -0.5 * x + 2, *range(1, 10)))
print(math_function_resolver(lambda x : 2.72 ** x, *range(1, 10), res_to_str=True))

######### Залание 4
print("#"*8, "Залание 4", "#"*8)
print()

def repeat(num_times=2) :
    def decorator(func) :
        def wrapper(*args, **kwargs) :
            for _ in range(num_times) :
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(6)
def testing_function() :
    print('python')

testing_function()


######### Залание 5
print("#"*8, "Залание 5", "#"*8)
print()

def logger(func) :
    @functools.wraps(func)
    def wrapper(*args, **kwargs) :
        func_name = func.__name__
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        defaults = func.__defaults__ if func.__defaults__ is not None else ()
        default_args = dict(zip(arg_names[-len(defaults) :], defaults))
        all_args = {**default_args, **kwargs}
        all_args.update(zip(arg_names, args))
        if func.__kwdefaults__ :
            all_args.update(func.__kwdefaults__)
        args_str = ", ".join(
            [f"{k}={v}" for k, v in all_args.items()]
        )

        try :
            result = func(*args, **kwargs)
            print(f"{func_name}({args_str}) -> {result}")
            return result
        except Exception as e :
            print(f"{func_name}({args_str}) .. {e.__class__.__name__}: {str(e)}")
    return wrapper

@logger
def div_round(num1, num2, *, digits=0) :
    return round(num1 / num2, digits)

print(div_round(1, 3, digits=2))
print(div_round(7, 2))
print(div_round(5, 0))
