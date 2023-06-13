from collections import deque

volews = deque(input().split())
consonants = deque(input().split())

words_to_find = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

flag = False

while volews and consonants and not flag:
    current_volew = volews.popleft()
    current_consonants = consonants.pop()

    for word in words_to_find.keys():

        if current_volew in word:
            words_to_find[word] = words_to_find[word].replace(current_volew, "")

        if current_consonants in word:
            words_to_find[word] = words_to_find[word].replace(current_consonants, "")

        if not words_to_find[word]:
            print(f"Word found: {word}")
            flag = True
            break

if not flag:
    print("Cannot find any word!")

if volews:
    print(f"Vowels left: {' '.join([char for char in volews])}")

if consonants:
    print(f"Consonants left: {' '.join([char for char in consonants])}")





