from collections import deque

volews = deque(input().split())
consonants = deque(input().split())

words_to_find = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}


while volews and consonants:
    current_volew = volews.popleft()
    current_consonants = consonants.pop()

    for word in words_to_find:
        words_to_find[word] = words_to_find[word].replace(current_volew, "")

        words_to_find[word] = words_to_find[word].replace(current_consonants, "")

        if not words_to_find[word]:
            print(f"Word found: {word}")
            break
    else:
        continue

    break

else:
    print("Cannot find any word!")

if volews:
    print(f"Vowels left: {' '.join(volews)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")





