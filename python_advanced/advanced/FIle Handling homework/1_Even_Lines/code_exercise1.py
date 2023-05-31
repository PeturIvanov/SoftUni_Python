import os
import re

root_path = os.path.dirname(os.path.abspath(__file__))

file_name = "even_lines_.txt"

file_path = os.path.join(root_path, file_name)

pattern = r"[\.\,\?\-\!]"

with open(file_path, "r") as file:
    file_content = file.read()
    file_content = re.sub(pattern, "@", file_content)

for i, line in enumerate(file_content.split("\n")):
    if i % 2 == 0:
        print(*[el for el in line.split()[::-1]])

