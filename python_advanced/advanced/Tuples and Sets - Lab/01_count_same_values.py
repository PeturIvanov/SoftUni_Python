numbers = [float(n) for n in input().split()]

numbers_data = {}

for num in numbers:
    if num not in numbers_data:
        number_count = numbers.count(num)
        numbers_data[num] = number_count

for key, value in numbers_data.items():
    print(f"{key:.1f} - {value} times")
