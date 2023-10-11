def memory_game(elements):
    moves = 0
    while True:
        guess = input().split(" ")
        if "end" in guess:
            print("Sorry you lose :(")
            return " ".join(elements)
        first_element = int(guess[0])
        second_element = int(guess[1])
        if len(elements) <= 0:
            return f"You have won in {moves} turns!"
        elif elements[first_element] == elements[second_element]:
            removed_elements = elements[first_element]
            if first_element > second_element:
                elements.pop(first_element)
                elements.pop(second_element)
                moves += 1
            else:
                elements.pop(second_element)
                elements.pop(first_element)
                moves += 1
            print(f"Congrats! You have found matching elements - {removed_elements}!")
        elif first_element == second_element or first_element not in range(len(elements)) or second_element\
                not in range(len(elements)):
            moves += 1
            elements.insert(len(elements) // 2, "-{}a".format(moves))
            elements.insert(len(elements) // 2, "-{}a".format(moves))
            print("Invalid input! Adding additional elements to the board")
        elif elements[first_element] != elements[second_element]:
            print("Try again!")
            moves += 1


sequence_of_elements = input().split(" ")
print(memory_game(sequence_of_elements))
