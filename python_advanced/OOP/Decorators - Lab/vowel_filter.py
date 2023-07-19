def vowel_filter(function):
    vowels = "aeoiu"
    def wrapper():
        return [el for el in function() if el in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())