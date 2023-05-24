def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]
    if command == "even":
        return [n for n in numbers if n % 2 == 0]
    elif command == "odd":
        return [n for n in numbers if n % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
