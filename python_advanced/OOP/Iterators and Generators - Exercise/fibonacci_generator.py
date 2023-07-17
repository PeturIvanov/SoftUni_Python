def fibonacci():
    fib1 = 0
    fib2 = 1

    while True:
        yield fib1
        fib1 = fib1 + fib2
        fib1 , fib2 = fib2, fib1

generator = fibonacci()
for i in range(5):
    print(next(generator))

