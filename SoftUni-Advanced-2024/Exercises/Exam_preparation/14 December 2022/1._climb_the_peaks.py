from collections import deque

daily_food = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(x) for x in input().split(", ")])

peaks_conquered = []
all_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
days = 1

while days < 8:
    food = daily_food.pop()
    stamina = daily_stamina.popleft()
    
    days += 1
    counter = 0

    combination = food + stamina

    for key, value in all_peaks.items():
        counter += 1
        if combination >= value:
            peaks_conquered.append(key)
            all_peaks.pop(key)

        if counter > 0:
            break
        else:
            continue

    if not all_peaks:
        break

if not all_peaks:
    print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_conquered:
    print("Conquered peaks:")
    print(*peaks_conquered, sep="\n")

