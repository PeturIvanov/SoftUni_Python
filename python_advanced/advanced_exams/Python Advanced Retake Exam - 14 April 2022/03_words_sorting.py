def words_sorting(*words):
    unsorted_dict = {}

    for word in words:
        unsorted_dict[word] = sum([ord(char) for char in word])

    if sum(unsorted_dict.values()) % 2 == 0:
        unsorted_dict = sorted(unsorted_dict.items(), key=lambda x: x[0])

    else:
        unsorted_dict = sorted(unsorted_dict.items(), key=lambda x: -x[1])

    return '\n'.join([f"{word} - {value}" for word, value in unsorted_dict])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
