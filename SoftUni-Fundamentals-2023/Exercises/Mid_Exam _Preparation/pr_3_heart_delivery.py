neighbourhood = [int(house) for house in input().split("@")]
current_jump = 0
command = input()
while command != "Love!":
    order, index = command.split()
    index = int(index)
    current_jump += index
    if current_jump not in range(len(neighbourhood)):
        current_jump = 0
    if neighbourhood[current_jump] == 0:
        print(f"Place {current_jump} already had Valentine's day.")
    else:
        neighbourhood[current_jump] -= 2
        if neighbourhood[current_jump] == 0:
            print(f"Place {current_jump} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {current_jump}.")

failed_houses = [i for i in neighbourhood if i > 0]
if sum(neighbourhood) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_houses)} places.")
