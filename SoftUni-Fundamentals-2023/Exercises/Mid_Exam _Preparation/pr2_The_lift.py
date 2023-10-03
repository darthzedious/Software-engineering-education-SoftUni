people_waiting_for_lift = int(input())
wagon = input().split(" ")
people_on_the_current_wagon = 0
people_on_the_lift = 0
no_more_people = False
new_list = []
for new in wagon:
    new_list.append(int(new))
for i in range(len(new_list)):
    while new_list[i] < 4:
        new_list[i] += 1
        people_on_the_current_wagon += 1
        if people_on_the_lift + people_on_the_current_wagon == people_waiting_for_lift:
            no_more_people = True
            break
    people_on_the_lift += people_on_the_current_wagon
    if no_more_people:
        break
    people_on_the_current_wagon = 0
if people_waiting_for_lift > people_on_the_lift:
    print(f"There isn't enough space! {people_waiting_for_lift  - people_on_the_lift} people in a queue!")
    print(" ".join(str(x) for x in new_list))
elif people_waiting_for_lift < len(new_list) * 4 and any(w < 4 for w in new_list):
    print("The lift has empty spots!")
    print(" ".join(str(x) for x in new_list))
elif all(w == 4 for w in new_list) and no_more_people:
    print(" ".join(str(x) for x in new_list))
