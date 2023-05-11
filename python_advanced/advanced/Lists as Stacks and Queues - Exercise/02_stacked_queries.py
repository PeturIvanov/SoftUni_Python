queries_count = int(input())

stack = []

for _ in range(queries_count):
    data = input().split()
    query_type = data[0]

    if query_type == "1":
        number_to_push = int(data[-1])
        stack.append(number_to_push)

    elif query_type == "2":
        if stack:
            stack.pop()

    elif query_type == "3":
        if stack:
            print(max(stack))

    elif query_type == "4":
        if stack:
            print(min(stack))


print(*(reversed(stack)), sep=", ")
