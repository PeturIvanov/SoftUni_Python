import os
import string

root_path = os.path.dirname(os.path.abspath(__file__))

file_name = "text.txt"

text_file_path = os.path.join(root_path, file_name)

output_text = os.path.join(root_path, "output.txt")

with open(text_file_path, "r+") as file:

    text_content = [line for line in file.read().split("\n") if line]

with open(output_text, "w") as output:

    for i, line in enumerate(text_content):

        punctuation_marks_count = len([el for el in line if el in string.punctuation])

        letters_count = len([char for char in line if char.isalpha()])

        output.writelines(f"Line {i + 1}: {line} ({letters_count})({punctuation_marks_count})\n")


