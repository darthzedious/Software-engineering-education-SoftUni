def concatenate(*args, **kwargs):
    phrase = "".join(args)

    for key, value in kwargs.items():
        phrase = phrase.replace(key, value)

    return phrase


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
