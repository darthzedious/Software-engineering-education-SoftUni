def memory_game(elements):
    while True:
        moves = 0
        matching_elements_found = 0
        guess = input().split(" ")
        if "end" in guess:
            print("Sorry you lose :(")
            print(elements)
            break

        if elements[int(guess[0])] == elements[int(guess[1])]:
            elements.remove([int(guess[0])]), elements.remove([int(guess[1])])
            matching_elements_found += 1
            print(f"Congrats! You have found matching elements - {matching_elements_found}!")
            continue
        else:
            print("Try again!")



        moves += 1
    return elements


sequence_of_elements = input().split(" ")
print(memory_game(sequence_of_elements))
