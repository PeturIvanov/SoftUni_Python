def age_assignment(*names, **kwargs):
    result = ""
    for name in sorted(names):
        result += f"{name} is {kwargs[name[0]]} years old.\n"

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))

