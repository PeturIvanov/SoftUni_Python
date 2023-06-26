def gather_credits(needed_credits, *args):
    total_credits = 0
    enrolled_courses = []
    print(*args)

    if needed_credits == 0:
        return f"Enrollment finished! Maximum credits: {total_credits}." \
               f"\nCourses: {', '.join(sorted(enrolled_courses))}"

    for course_name, course_credits in args:
        if course_name not in enrolled_courses:
            enrolled_courses.append(course_name)

            total_credits += course_credits

        if total_credits >= needed_credits:
            return f"Enrollment finished! Maximum credits: {total_credits}." \
                   f"\nCourses: {', '.join(sorted(enrolled_courses))}"

    return f"You need to enroll in more courses!" \
               f" You have to gather {needed_credits - total_credits} credits more."



print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))