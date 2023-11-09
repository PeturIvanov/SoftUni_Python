import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Student


# add_student first solution
def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )

    student = Student(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )

    student.save()

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


# add_students()
# print(Student.objects.all())


# add_student second solution
def add_student_second_solution():
    students_data = (
        {'student_id': 'FC5204B',
         'first_name': 'John',
         'last_name': 'Doe',
         'birth_date': '1995-05-15',
         'email': 'john.doeb@university.com'
         },
        {'student_id': 'FE0054B',
         'first_name': 'Jane',
         'last_name': 'Smith',
         'email': 'jane.smithb@university.com'
         },
    )

    for record in students_data:
        Student.objects.create(**record)


# add_student_second_solution()
# print(Student.objects.all())


def get_students_info():
    students_info = []

    for student_record in Student.objects.all():
        students_info.append(
            f"Student №{student_record.student_id}:"
            f" {student_record.first_name}"
            f" {student_record.last_name};"
            f" Email: {student_record.email}"
        )

    return '\n'.join(students_info)


# print(get_students_info())


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        new_email = student.email.replace('university.com', 'uni-students.com')
        student.email = new_email

    Student.objects.bulk_update(students, ['email'])


# update_students_emails()
#
# for student in Student.objects.all():
#     print(student.email)


def truncate_students():
    Student.objects.all().delete()


# truncate_students()
# print(Student.objects.all())
# print(f"Number of students: {Student.objects.count()}")






























