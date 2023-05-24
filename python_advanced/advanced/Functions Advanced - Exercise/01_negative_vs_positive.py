def negative_numbers(numbers):
    sum_negative_nums = 0
    for n in numbers:
        if n < 0:
            sum_negative_nums += n

    return sum_negative_nums


def positive_numbers(numbers):
    sum_positive_nums = 0
    for n in numbers:
        if n > 0:
            sum_positive_nums += n

    return sum_positive_nums


def biggest_abs_value(numbers):
    if positive_numbers(numbers) > abs(negative_numbers(numbers)):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


list_of_numbers = [int(x) for x in input().split()]
print(negative_numbers(list_of_numbers))
print(positive_numbers(list_of_numbers))
print(biggest_abs_value(list_of_numbers))
