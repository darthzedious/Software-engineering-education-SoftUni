text = input()
removed_vowels = [char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(removed_vowels))
