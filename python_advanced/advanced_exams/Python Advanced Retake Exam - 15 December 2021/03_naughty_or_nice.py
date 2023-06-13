def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_kids = []
    naughty_kids = []
    result = []

    def place_kids():
        if len(kids) == 1:
            if kid_type == "Naughty":
                naughty_kids.append(kids[0])

            else:
                nice_kids.append(kids[0])

            santa_list.remove(kids[0])

    for data in args:
        number, kid_type = data.split("-")

        kids = [info for info in santa_list if info[0] == int(number)]

        place_kids()

    for kid_name, kid_type in kwargs.items():
        kids = [info for info in santa_list if info[1] == kid_name]

        place_kids()

    if nice_kids:
        result.append(f"Nice: {', '.join([k[1] for k in nice_kids])}")

    if naughty_kids:
        result.append(f"Naughty: {', '.join([k[1] for k in naughty_kids])}")

    if santa_list:
        result.append(f"Not found: {', '.join([k[1] for k in santa_list])}")

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))