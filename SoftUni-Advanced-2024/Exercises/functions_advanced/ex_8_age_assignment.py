def age_assignment(*args, **kwargs):
    data = []

    for name, age in kwargs.items():
        for person in args:
            if person.startswith(name):
                data.append(f"{person} is {age} years old.")

    return "\n".join(sorted(data))


print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
