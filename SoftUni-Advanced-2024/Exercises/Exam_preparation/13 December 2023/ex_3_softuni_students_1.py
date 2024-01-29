def softuni_students(*args, **kwargs):

    invalid_students = set()
    course_data = {}
    final_data = []

    for course_id, course in kwargs.items():  # creating a dict with a list of values => /value[0] = course/
        # and /value[1] = list of students in the course/
        for info in args:
            stud_id, username = info

            if stud_id == course_id:

                if course_id not in course_data.keys():
                    course_data[course_id] = [course, [username]]
                else:
                    course_data[course_id][1].append(username)

            elif stud_id != course_id and username not in course:
                invalid_students.add(username)

    for key, value in course_data.items(): # sorting the usernames of students inside the list in the values => value[1]
        value[1] = sorted(value[1])
        course_data[key][1] = value[1]

    #sorted_by_name = list(pair) for pair in sorted(course_data.items(), key=lambda x: (x[1][0][0], x[1][1])) =>
    # it would look like this if i wanted to return it as a list of lists not as dict
    sorted_by_name = dict(sorted(course_data.items(), key=lambda x: (x[1][0][0], x[1][1])))  # sorting the courses

    for id, data in sorted_by_name.items():  # adding the needed data in a separate list to return it later

        for name in data[1]:
            final_data.append(f"*** A student with the username {data[1][data[1].index(name)]} has successfully finished the course {data[0]}!")

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


print(softuni_students(
    ('id_4', 'John'),
    ('id_4', 'Alice'),
    ('id_4', 'Bob'),
    ('id_4', 'Eve'),

    id_4='Course 1'
))