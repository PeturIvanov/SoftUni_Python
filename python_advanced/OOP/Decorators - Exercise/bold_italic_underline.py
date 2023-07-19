def make_bold(function):
    open_format = "<b>"
    close_format = "</b>"
    def wrapper(*args):
        return f"{open_format}{function(*args)}{close_format}"

    return wrapper


def make_italic(function):
    open_format = "<i>"
    close_format = "</i>"
    def wrapper(*args):
        return f"{open_format}{function(*args)}{close_format}"

    return wrapper


def make_underline(function):
    open_format = "<u>"
    close_format = "</u>"
    def wrapper(*args):
        return f"{open_format}{function(*args)}{close_format}"

    return wrapper


@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))

