def my_func(x, y):
    try:
        res = x ** y
    except TypeError:
        return "enter a float number and a negative power"
    return res


print(my_func(4.5, -2))
