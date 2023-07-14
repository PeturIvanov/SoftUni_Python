class sequence_repeat:
    def __init__(self, sequence, num):
        self.sequence = sequence
        self.result_length = num
        self.current_index = -1
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1

        if self.current_count == self.result_length:
            raise StopIteration

        if self.current_index == len(self.sequence):
            self.current_index = 0

        self.current_count += 1

        return self.sequence[self.current_index]

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

