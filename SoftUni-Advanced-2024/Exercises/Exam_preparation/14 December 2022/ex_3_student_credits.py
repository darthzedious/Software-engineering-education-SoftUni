from collections import defaultdict


def students_credits(*args):
    diyan_data = defaultdict(float)
    result = []

    for info in args:
        course_name, max_credits, max_test_points, diyan_points = info.split("-")

        diyan_credits = float(max_credits) * (float(diyan_points) / float(max_test_points))
        diyan_data[course_name] = diyan_credits

    sorted_data = sorted(diyan_data.items(), key=lambda x: -x[1])
    total_credits = sum(diyan_data.values())

    for course_name, diyan_credits in sorted_data:
        result.append(f"{course_name} - {diyan_credits:.1f}\n")

    if total_credits >= 240:
        return f"Diyan gets a diploma with {total_credits:.1f} credits.\n{''.join(str(x) for x in result)}"
    else:
        credits_needed = 240 - total_credits
        return f"Diyan needs {credits_needed:.1f} credits more for a diploma.\n{''.join(str(x) for x in result)}"

print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
