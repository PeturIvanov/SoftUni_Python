clothes = [int(cloth) for cloth in input().split()]
rack_capacity = int(input())

rack_count = 0

clothes_sum = 0

while clothes:
    if clothes_sum + clothes[-1] <= rack_capacity:
        clothes_sum += clothes.pop()
    elif clothes_sum + clothes[-1] > rack_capacity:
        rack_count += 1
        clothes_sum = 0

    if clothes_sum == rack_capacity:
        rack_count += 1
        clothes_sum = 0

if clothes_sum != 0:
    rack_count += 1
print(rack_count)
