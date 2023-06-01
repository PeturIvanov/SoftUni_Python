import os

root_path = os.path.dirname(os.path.abspath(__file__))

while True:
    input_data = input().split("-")

    command = input_data[0]

    if command == "End":
        break

    file_name = input_data[1]

    file_path = os.path.join(root_path, f"txt_files/{file_name}")

    if command == "Create":
        with open(file_path, "w"):
            pass

    elif command == "Add":

        content = input_data[2]

        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":

        old_string = input_data[2]
        new_string = input_data[3]

        try:
            with open(file_path, "r+") as file:
                file_content = file.read()
                file_content = file_content.replace(old_string, new_string)

                file.seek(0)
                file.write(file_content)

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(file_path)

        except FileNotFoundError:
            print("An error occurred")

