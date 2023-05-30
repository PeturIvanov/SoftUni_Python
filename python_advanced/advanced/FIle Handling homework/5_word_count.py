import os
import re


def write_text(file_to_write):
    with open(file_to_write, "w") as file:
        file.writelines(input())


def read_file(file_to_read):
    try:
        with open(file_to_read, "r") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("File doesn't exist.")
        exit(0)


root_path = os.path.dirname(os.path.abspath(__file__))

words_file_name = "words.txt"

words_file_path = os.path.join(root_path, words_file_name)

# Write the words that have to be found.
write_text(words_file_name)

words_list = read_file(words_file_path).split()

text_file_name = " text.txt"

text_file_path = os.path.join(root_path, text_file_name)

# Write the text.
write_text(text_file_name)

text_content = read_file(text_file_path)

words_count = {}

for word in words_list:
    words_in_text = re.findall(r"\w+", text_content)

    words_count[word] = words_in_text.count(word)

sorted_words_count = sorted(words_count.items(), key=lambda x: -x[1])

output_file = os.path.join(root_path, "output.txt")

with open(output_file, "w") as result:
    result.writelines([f"{w} - {c}\n" for w, c in sorted_words_count])
