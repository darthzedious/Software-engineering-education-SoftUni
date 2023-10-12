list_of_employees = list(map(int, input(). split()))
factor = int(input())
employee_happyness_after = [emp * factor for emp in list_of_employees]

filtered = list(filter(lambda x: x >= (sum(employee_happyness_after) / len(employee_happyness_after)), employee_happyness_after))
if len(filtered) >= len(employee_happyness_after)/2:
    print(f"Score: {len(filtered)}/{len(employee_happyness_after)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employee_happyness_after)}. Employees are not happy!")
