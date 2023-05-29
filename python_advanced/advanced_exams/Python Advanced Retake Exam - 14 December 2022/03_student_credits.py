def students_credits(*courses_info):
    total_credits = 0
    student_data = {}

    for course in courses_info:

        course_name, max_credits, max_test_points, student_points =\
            [int(el) if el.isdigit() else el for el in course.split("-")]

        course_credits = max_credits * (student_points / max_test_points)

        student_data[course_name] = course_credits

        total_credits += course_credits

    sorted_courses = sorted(student_data.items(), key=lambda x: -x[1])

    new_line = "\n"

    if total_credits >= 240:

        return f"Diyan gets a diploma with {total_credits:.1f} credits.{new_line}" \
               f"{new_line.join([f'{course} - {credit:.1f}' for course, credit in sorted_courses])}"

    else:
        return f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.{new_line}" \
                f"{new_line.join([f'{course} - {credit:.1f}' for course, credit in sorted_courses])}"



print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)