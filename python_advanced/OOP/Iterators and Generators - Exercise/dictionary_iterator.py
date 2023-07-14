from typing import Dict

class dictionary_iter:
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.keys):
            self.index = -1
            raise StopIteration

        return self.keys[self.index], self.values[self.index]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
