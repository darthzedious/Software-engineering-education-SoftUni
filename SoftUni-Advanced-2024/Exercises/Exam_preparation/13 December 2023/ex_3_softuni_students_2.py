def softuni_students(*args, **kwargs):
    invalid_students = set()
    course_data = {}
    final_data = []

    for course_id, course in kwargs.items():
        for info in args:
            stud_id, username = info

            if stud_id == course_id:

                if course not in course_data.keys():
                    course_data[course] = [username]
                else:
                    course_data[course].append(username)
            else:
                invalid_students.add(username)

    for key, value in course_data.items():
        value = sorted(value)
        course_data[key] = value

    sorted_by_name = dict(sorted(course_data.items(), key=lambda x: x[1]))

    for id, data in sorted_by_name.items():

        for name in data:
            final_data.append(f"*** A student with the username {name} has successfully finished the course {id}!")

            if name in invalid_students:
                invalid_students.remove(name)

    sorted_invalid_students = list(sorted(invalid_students))

    if invalid_students:
        final_data.append(f'!!! Invalid course students: {", ".join(sorted_invalid_students)}')

    return "\n".join(final_data)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
