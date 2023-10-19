distance_to_the_pokemon = list(map(int, input().split()))
lst_of_removed_el = []
while True:
    if len(distance_to_the_pokemon) <= 0:
        break
    element = int(input())
    removed_el = 0
    if element < 0:
        removed_el = distance_to_the_pokemon.pop(0)
        distance_to_the_pokemon.insert(0, distance_to_the_pokemon[-1])
    elif element > len(distance_to_the_pokemon) - 1:
        removed_el = distance_to_the_pokemon.pop()
        distance_to_the_pokemon.append(distance_to_the_pokemon[0])
    else:
        removed_el = distance_to_the_pokemon.pop(element)
    for el in range(len(distance_to_the_pokemon)):
        if distance_to_the_pokemon[el] <= removed_el:
            distance_to_the_pokemon[el] += removed_el
        else:
            distance_to_the_pokemon[el] -= removed_el
    lst_of_removed_el.append(removed_el)
print(sum(lst_of_removed_el))
