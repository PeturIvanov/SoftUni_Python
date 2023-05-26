def math_operations(*float_numbers, **data):
    operation_counter = 0

    for num in float_numbers:
        if operation_counter == 0:
            data["a"] += num

        elif operation_counter == 1:
            data["s"] -= num

        elif operation_counter == 2:
            if data["d"] != 0 and num != 0:
                data["d"] /= num

        elif operation_counter == 3:
            data["m"] *= num

        if operation_counter == 3:
            operation_counter = 0
        else:
            operation_counter += 1

    sorted_result = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{key}: {value:.1f}" for key, value in sorted_result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))
