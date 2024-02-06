from collections import deque

seats = input().split(", ")
numbers1 = deque([int(x) for x in input().split(", ")])
numbers2 = deque([int(x) for x in input().split(", ")])

matches = 0
rotations = 0
taken_seats = []

while True:
    if matches == 3:
        break
    if rotations == 10:
        break

    rotations += 1

    number1 = numbers1.popleft()
    number2 = numbers2.pop()

    combination = number1 + number2
    ascii_combination = chr(number1 + number2)
    seat_to_check1 = f"{number1}{ascii_combination}"
    seat_to_check2 = f"{number2}{ascii_combination}"

    if seat_to_check1 in seats and seat_to_check1 not in taken_seats:
        matches += 1
        taken_seats.append(seat_to_check1)

    if seat_to_check2 in seats and seat_to_check2 not in taken_seats:
        matches += 1
        taken_seats.append(seat_to_check2)

    if seat_to_check1 not in seats and seat_to_check2 not in seats:
        numbers1.append(number1)
        numbers2.appendleft(number2)

print(f"Seat matches: {', '.join(x for x in taken_seats)}")
print(f"Rotations count: {rotations}")
