characters = input().split(", ")

characters_and_digits = {char: ord(char) for char in characters}
print(characters_and_digits)
