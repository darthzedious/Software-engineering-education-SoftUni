targets = [int(target) for target in input().split()]
count_of_shot_targets = 0
while True:
    command = input()
    if command == "End":
        print(f"Shot targets: {count_of_shot_targets} -> {' '.join(str(target) for target in targets)}")
        break
    target_index = int(command)
    if target_index <= len(targets) - 1:
        if targets[target_index] >= 0:
            for target in range(0, len(targets)):
                if target != target_index and targets[target] >= 0:
                    if targets[target] > targets[target_index]:
                        targets[target] -= targets[target_index]
                    else:
                        targets[target] += targets[target_index]

        targets[target_index] = -1
        count_of_shot_targets += 1
