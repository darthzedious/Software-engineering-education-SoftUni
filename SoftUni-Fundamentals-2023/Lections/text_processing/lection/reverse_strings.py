while True:
    text = input()
    if text == "end":
        break
    reverse_text = text[::-1]
    print(f"{text} = {reverse_text}")
