class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_count = 0
        self.current_num = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num += self.step
        if self.current_count == self.count:
            self.current_count = 0
            self.current_num = 0 - self.step
            raise StopIteration

        self.current_count += 1
        return self.current_num

numbers = take_skip(10, 5)
for number in numbers:
    print(number)



