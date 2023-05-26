def func_executor(*funcs):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in funcs])


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
 (make_upper, ("Python", "softUni")),
 (make_lower, ("PyThOn",)),
))
