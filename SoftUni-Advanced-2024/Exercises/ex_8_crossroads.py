from collections import deque

green_light = int(input())
free_window = int(input())
green_window = green_light
cars_passed = 0
total_green_light = green_window + free_window

crossroad = deque()
while True:
    command = input()
    if command == "END":
        print(f"Everyone is safe.\n {cars_passed} total cars passed the crossroads.")
        break

    if command != "green":
        for char in command:
            crossroad.append(char)

        if len(crossroad) < green_window:
            green_window -= len(crossroad)

            crossroad.clear()
            cars_passed += 1

        elif len(crossroad) > green_window:
            if len(crossroad) <= total_green_light:
                total_green_light -= len(crossroad)
                crossroad.clear()
                green_window = 0
                cars_passed += 1
            else:
                for char in range(total_green_light):
                    crossroad.popleft()
                if crossroad:
                    print(f"A crash happened!\n{command} was hit at {crossroad[0]}.")
                    break
    elif command == "green":
        green_window = green_light

