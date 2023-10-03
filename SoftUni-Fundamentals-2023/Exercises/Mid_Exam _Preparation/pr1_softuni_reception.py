first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students_count = int(input())
hours = 0
combined_employees = first_employee + second_employee + third_employee
working_hour = True
while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        working_hour = False
        continue
    students_count -= combined_employees
print(f"Time needed: {hours}h.")
