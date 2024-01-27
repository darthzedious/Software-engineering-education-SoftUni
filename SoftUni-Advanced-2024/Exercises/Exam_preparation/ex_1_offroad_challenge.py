from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
amount_of_fuel_needed = deque(int(x) for x in input().split())

altitudes_n = 0
altitudes = []

while initial_fuel:

    fuel = initial_fuel.pop()
    additional_consum = additional_consumption_index.popleft()
    fuel_needed = amount_of_fuel_needed.popleft()

    check = fuel - additional_consum

    if check >= fuel_needed:
        altitudes_n += 1
        altitudes.append(f"Altitude {altitudes_n}")
        print(f"John has reached: Altitude {altitudes_n}")

    else:
        if len(altitudes) == 0:
            print(f"John did not reach: Altitude {altitudes_n + 1}")
            print(f"John failed to reach the top.\nJohn didn't reach any altitude.")

        if altitudes:
            print(f"John did not reach: Altitude {altitudes_n + 1}")
            print(f"John failed to reach the top. \nReached altitudes: {', '.join(altitudes)}")
        break

if len(altitudes) == 4:
    print(f"John has reached all the altitudes and managed to reach the top!")
