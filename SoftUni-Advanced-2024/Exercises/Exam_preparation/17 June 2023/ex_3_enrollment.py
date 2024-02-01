def gather_credits(number_credits: int, *args):
    gathered_credits = 0
    courses = []

    for course, credits in args:
        if number_credits > gathered_credits:
            if course not in courses:
                courses.append(course)
                gathered_credits += credits
        else:
            break

    if gathered_credits >= number_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}."'\n'f"Courses: {', '.join(x for x in sorted(courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {number_credits-gathered_credits} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
