array_with_strings = input().split(" ")
array_with_integers = []
for el in array_with_strings:
    array_with_integers.append(int(el))
while True:
    command = input().split(" ")
    order = command[0]
    if order == "end":
        break
    if order == "swap":
        if 0 <= int(command[1]) < len(array_with_integers):
            array_with_integers[int(command[1])], array_with_integers[int(command[2])] =\
                array_with_integers[int(command[2])], array_with_integers[int(command[1])]

    elif order == "multiply":
        array_with_integers[int(command[1])] = array_with_integers[int(command[1])] *\
                                                    array_with_integers[int(command[2])]
    elif order == "decrease":
        for element in range(len(array_with_integers)):
            array_with_integers[element] = array_with_integers[element] - 1
print(", ".join(str(x) for x in array_with_integers))
