n = int(input())
reservations = set()
for _ in range(n):
    code = input()
    reservations.add(code)
reservations_copy = reservations.copy()

guest_came = input()
while guest_came != "END":
    reservations_copy.remove(guest_came)
    guest_came = input()

print(len(reservations_copy))
for guest in sorted(reservations_copy):
    print(guest)
