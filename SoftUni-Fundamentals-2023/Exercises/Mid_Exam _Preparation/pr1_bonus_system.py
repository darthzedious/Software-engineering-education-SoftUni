from math import ceil
number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendances = 0
for student in range(1, number_of_students + 1):
    attendance = int(input())
    total_bonus = attendance / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendances = attendance
print(f"Max Bonus: {ceil(max_bonus)}.\n"
      f"The student has attended {max_attendances} lectures.")
