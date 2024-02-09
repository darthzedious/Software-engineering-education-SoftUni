def words_sorting(*args):
    words = {word: sum(map(ord, word)) for word in args}
    result_str = []

    if not sum(words.values()) % 2 == 0:
        for word in sorted(words.items(), key=lambda x: -x[1]):
            result_str.append(f"{word[0]} - {word[1]}")
    else:
        for word in sorted(words.items(), key=lambda x: x[0]):
            result_str.append(f"{word[0]} - {word[1]}")

    return "\n".join(result_str)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
