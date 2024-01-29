def softuni_students(*args, **kwargs):
    invalid_students = set()
    course_data = {}
    final_data = []

    for course_id, course in kwargs.items():
        for info in args:
            stud_id, username = info

            if stud_id == course_id:

                if course_id not in course_data.keys():
                    course_data[course_id] = [course, [username]]
                else:
                    course_data[course_id][1].append(username)

            elif stud_id != course_id and username not in course:
                invalid_students.add(username)

    sorted_by_name = dict(list(pair) for pair in sorted(course_data.items(), key=lambda x: (x[1][0][0], x[1][1])))

    for id, data in sorted_by_name.items():
        counter_step = 0
        for name in data[1]:
            final_data.append(f"*** A student with the username {data[1][data[1].index(name)]} has successfully finished the course {data[0]}!")
            if name in invalid_students:
                invalid_students.remove(name)

        if len(data[1]) > counter_step:
            counter_step += 1

    sorted_invalid_students = list(sorted(invalid_students))

    if invalid_students:
        final_data.append(f'!!! Invalid course students: {", ".join(sorted_invalid_students)}')

    return "\n".join(final_data)
