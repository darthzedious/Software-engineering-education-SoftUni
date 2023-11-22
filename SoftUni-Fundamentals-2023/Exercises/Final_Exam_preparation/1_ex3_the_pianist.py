music = {}
number_of_pieces = int(input())
for song in range(number_of_pieces):
    piece, composer, key = input().split("|")
    music[piece] = [composer, key]
while True:
    command = input()
    if command == "Stop":
        break
    if "Add" in command:
        cmd, piece, composer, key = command.split("|")
        if piece not in music.keys():
            music[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif "Remove" in command:
        cmd, piece = command.split("|")
        if piece not in music.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            music.pop(piece)
            print(f"Successfully removed {piece}!")
    elif "ChangeKey" in command:
        cmd, piece, new_key = command.split("|")
        if piece not in music.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            music[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
for piece, info in music.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")
