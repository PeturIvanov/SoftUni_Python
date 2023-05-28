numbers_dictionary = {}

number_as_string = input()

while number_as_string != "Search":
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")

    number_as_string = input()

searched_key_number = input()

while searched_key_number != "Remove":
    try:
        print(numbers_dictionary[searched_key_number])

    except KeyError:
        print("Number does not exist in dictionary")

    searched_key_number = input()

number_to_remove = input()

while number_to_remove != "End":
    try:
        del numbers_dictionary[number_to_remove]

    except KeyError:
        print("Number does not exist in dictionary")

    number_to_remove = input()

print(numbers_dictionary)
