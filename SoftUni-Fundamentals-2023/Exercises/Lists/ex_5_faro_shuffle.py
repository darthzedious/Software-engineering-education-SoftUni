deck_of_cards = input().split(" ")
number_of_shuffles = int(input())
for i in range(number_of_shuffles):
    deck = []
    middle_part = len(deck_of_cards)//2
    left_part = deck_of_cards[:middle_part]
    right_part = deck_of_cards[middle_part:]
    for j in range(len(right_part)):
        deck.append(left_part[j])
        deck.append(right_part[j])
    deck_of_cards = deck
print(deck_of_cards)
