def number_increment(nums):
    def increase():
        return [el + 1 for el in nums]

    return increase()


print(number_increment([1, 2, 3]))

