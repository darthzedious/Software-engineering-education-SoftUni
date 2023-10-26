deck_of_cards = input().split(", ")
command_number = int(input())

for n in range(command_number):
    command = input()
    order = command.split(", ")[0]
    if order == "Add":
        card_name = command.split(", ")[1]
        if card_name in deck_of_cards:
            print("Card is already in the deck")
        else:
            deck_of_cards.append(card_name)
            print("Card successfully added")
    elif order == "Remove":
        card_name = command.split(", ")[1]
        if card_name not in deck_of_cards:
            print("Card not found")
        else:
            deck_of_cards.remove(card_name)
            print("Card successfully removed")
    elif order == "Remove At":
        index = int(command.split(", ")[1])
        if index not in range(len(deck_of_cards)):
            print("Index out of range")
        else:
            deck_of_cards.pop(index)
            print("Card successfully removed")
    elif order == "Insert":
        index = int(command.split(", ")[1])
        card_name = command.split(", ")[2]
        if index not in range(len(deck_of_cards)):
            print("Index out of range")
        else:
            if card_name in deck_of_cards:
                print("Card is already added")
            else:
                deck_of_cards.insert(index, card_name)
                print("Card successfully added")
print(", ".join(deck_of_cards))
