from collections import deque


def climb_peaks(food_portions, stamina):
    peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
    conquered_peaks = []

    for _ in range(7):
        daily_food = food_portions.pop()
        daily_stamina = stamina.popleft()
        total = daily_food + daily_stamina

        for peak, difficulty in peaks.items():
            if total >= difficulty:
                conquered_peaks.append(peak)
                del peaks[peak]
                break

    return conquered_peaks


def main():
    food_input = input().split(', ')
    stamina_input = input().split(', ')

    food_portions = [int(portion) for portion in food_input]
    stamina = deque([int(stam) for stam in stamina_input])

    conquered_peaks = climb_peaks(food_portions, stamina)

    if len(conquered_peaks) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    else:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

    if conquered_peaks:
        print("Conquered peaks:")
        for peak in conquered_peaks:
            print(peak)


if __name__ == "__main__":
    main()
