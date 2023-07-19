def type_check(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for el in args:
                if not isinstance(el, data_type):
                    return "Bad Type"

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def times2(num, num2):
    return num * num2
print(times2(2, 5))
print(times2('Not A Number'))
