expression = input()
stack = []

for i, el in enumerate(expression):
    if el == "(":
        stack.append(i)
    elif el == ")":
        start_index = stack[-1]
        end_index = i + 1
        print(expression[start_index:end_index])
        stack.pop()
