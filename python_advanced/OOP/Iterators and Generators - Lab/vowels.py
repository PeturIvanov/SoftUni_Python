class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.vowels_in_text = [char for char in self.text if char.lower() in self.vowels]
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx == len(self.vowels_in_text):
            self.current_idx = -1
            raise StopIteration

        return self.vowels_in_text[self.current_idx]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
