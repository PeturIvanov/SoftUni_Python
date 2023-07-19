class store_results:

    file_log = "result.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = f"Function '{self.func.__name__}' was called. Result: {self.func(*args, **kwargs)}"

        with open(self.file_log, "a") as file:
            file.write(log_string + "\n")




@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)

