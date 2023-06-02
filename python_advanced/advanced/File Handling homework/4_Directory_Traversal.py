import os


def directory_files(dir_name, level=0):

    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)

        if os.path.isfile(file_path):
            extension = file_name.split(".")[-1]

            if extension not in extensions_data:
                extensions_data[extension] = []

            extensions_data[extension].append(file_name)

        elif os.path.isdir(file_path) and level < 1:
            directory_files(file_path, level + 1)


directory = input()

extensions_data = {}

directory_files(directory)

sorted_extensions = sorted(extensions_data.items(), key=lambda x: x[0])

with open("txt_files/report.txt", "w") as file:
    for extension, files in sorted_extensions:
        file.write(f".{extension}\n")
        file.write(''.join([f"---{file}\n" for file in sorted(files)]))



