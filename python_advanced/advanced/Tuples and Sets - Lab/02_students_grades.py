number_of_students = int(input())

students_data = {}

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)

    if name not in students_data:
        students_data[name] = []
    students_data[name].append(grade)

for key, value in students_data.items():
    avg = sum(value) / len(value)
    print(f"{key} -> {' '.join([str(f'{n:.2f}')for n in value])} (avg: {avg:.2f})")

