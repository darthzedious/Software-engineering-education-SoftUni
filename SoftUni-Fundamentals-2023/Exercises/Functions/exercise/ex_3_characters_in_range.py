def characters_in_range(first: str, last: str) -> list:
    characters = []
    for char in range(ord(first) + 1, ord(last)):
        characters. append(chr(char))
    return characters


first_character = input()
second_character = input()
final_result = characters_in_range(first_character, second_character)
print(" ".join(final_result))
